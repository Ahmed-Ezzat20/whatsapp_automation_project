import requests

from api.log import login

def fetch_pharmacy_data(api_url):
    """
    Fetch pharmacy data from the external API.
    """
    Login_URL = "https://cluster.designfy.net/api/login"
    
    login_response = login(Login_URL)

    data_token = login_response['data']['token']

    headers = { "Authorization": f"Bearer {data_token}" }

    form_data = {
        'area_id': "63",
        'per_page': "200"
    }
    

    response = requests.post(api_url, headers=headers , data=form_data)

    if response.status_code == 200:
        return response.json()
    else:
        return None