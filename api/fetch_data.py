import requests

def fetch_pharmacy_data(api_url, token):
    """
    Fetch pharmacy data from the external API.
    """
    headers = { "Authorization": f"Bearer {token}" }

    form_data = {
        'area_id': "63",
        'per_page': "200"
    }
    

    response = requests.post(api_url, headers=headers , data=form_data)

    if response.status_code == 200:
        return response.json()
    else:
        return None