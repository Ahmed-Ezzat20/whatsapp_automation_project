from api.fetch_data import fetch_pharmacy_data
from automation.whatsapp_bot import WhatsAppBot
from automation.message_utils import load_message_template


def main():
    API_URL = "https://cluster.designfy.net/api/supplier/marketing"
    data = fetch_pharmacy_data(API_URL)

    if data and data.get("success"):
        pharmacies = data["pharmacies"] 
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
