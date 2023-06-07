import requests


files = {
    'email': (None, "user12345@gmail.com"),
    'password': (None, "user12345"),
    'rememberMe': (None, "true"),
}


def getToken():
    response = requests.post(
        'https://staging.loadzpro.app/v1/users/token/', files=files)
    if response.status_code == 200:
        data = response.json()
        access = data['access']
        return access
    else:
        return refreshToken()


def refreshToken():
    response = requests.post(
        'https://staging.loadzpro.app/v1/users/token/refresh/', files=files)
    if response.status_code == 200:
        data = response.json()
        access = data['access']
        return access
    else:
        print("Token retrieval failed with status code:", response.status_code)
        return None


access_token = getToken()


def make_api_request(access_token):
    url = "https://staging.loadzpro.app/v1/search_loads/"

    headers = {
        "Authorization": f"Bearer {access_token}"}

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()  # Raise an exception for any non-2xx status code
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


api_data = make_api_request(access_token)

if api_data:
    # Process the API data
    print(api_data)
else:
    print("API request failed.")
