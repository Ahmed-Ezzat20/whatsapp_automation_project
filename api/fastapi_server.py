from fastapi import FastAPI
from api.fetch_data import fetch_pharmacy_data
import uvicorn
from api.log import login

app = FastAPI()

API_URL = "https://cluster.designfy.net/api/supplier/marketing"

@app.get("/pharmacies")
def get_pharmacies():
    """
    Fetch pharmacy data from the external API and return it as JSON.
    """

    # Fetch pharmacy data
    data = fetch_pharmacy_data(API_URL)
    if data:
        return {"success": True, "data": data}
    else:
        return {"success": False, "error": "Unable to fetch data"}
    



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, reload=True)