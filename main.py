from api.fetch_data import fetch_pharmacy_data
from automation.whatsapp_bot import WhatsAppBot
from automation.message_utils import load_message_template


def main():
    # Fetch pharmacy data
    API_URL = "https://clusterapp.net/doc/#api-Supplier_-_Marketing-FetchMarketingMedicines"
    CREDENTIALS = {"id": "01155322655", "password": "password"}
    data = fetch_pharmacy_data(API_URL, CREDENTIALS)

    if data and data.get("success"):
        pharmacies = data["pharmacies"]["data"]
        daily_offers = data["dailySupplies"]

        # Initialize WhatsApp bot
        bot = WhatsAppBot()
        bot.login_to_whatsapp()

        for pharmacy in pharmacies:
            phone = pharmacy["phone"]
            context = {
                "pharmacy_name": pharmacy["name"],
                "daily_offers": "\n".join(
                    [f"{offer['medicine_name']} - {offer['price']} EGP" for offer in daily_offers]
                )
            }
            message = load_message_template("automation/templates/message_template.txt", context)
            bot.send_message(phone, message)

        bot.close()
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()
