from fastapi import FastAPI
from api.fetch_data import fetch_pharmacy_data
import uvicorn
from api.log import login

app = FastAPI()

API_URL = "https://cluster.designfy.net/api/supplier/marketing"
Login_URL = "https://cluster.designfy.net/api/login"
CREDENTIALS = {"id": "01155322655", "password": "password"}

@app.get("/pharmacies")
def get_pharmacies():
    """
    Fetch pharmacy data from the external API and return it as JSON.
    """

    # Login to the API
    login_response = login(Login_URL)
    
    if not login_response:
        return {"success": False, "error": "Login failed"}
    
    data_token = login_response['data']['token']

    # Fetch pharmacy data
    data = fetch_pharmacy_data(API_URL, data_token)
    if data:
        return {"success": True, "data": data}
    else:
        return {"success": False, "error": "Unable to fetch data"}
    
    
    # Fetch pharmacy data

    # data = fetch_pharmacy_data(API_URL, CREDENTIALS)
    # if data:
    #     return {"success": True, "data": data}
    # else:
    #     return {"success": False, "error": "Unable to fetch data"}
    



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, reload=True)