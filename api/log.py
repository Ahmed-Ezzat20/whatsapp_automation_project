import requests

def login(endpoint_url: str) -> dict:
    """
    Login to the specified endpoint using username and password
    
    Args:
        username (str): User's username
        password (str): User's password
        endpoint_url (str): The login endpoint URL
        
    Returns:
        dict: Response from the server
    """
    # Prepare the form data
    form_data = {
        'phone': "01000100100",
        'password': "Az@100100"
    }
    
    try:
        # Send POST request with form data
        response = requests.post(endpoint_url, data=form_data)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Return the response as JSON
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Login failed: {str(e)}")
        return None