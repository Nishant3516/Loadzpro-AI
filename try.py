import requests


def make_api_request(access_token):
    # Replace with the actual API endpoint URL
    url = "https://staging.loadzpro.app/v1/search_loads/ch_robinson/"

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


access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1MDc5OTUzLCJqdGkiOiJmMWQ3ZGQ4ZmZhZjI0MDZmOGMzMzhkYjc3Mjg3NjE4OCIsInVzZXJfaWQiOjE5fQ.3MTaORy1zj6yUrvZN1EhZWH5mhaG7X9v2LIe6zU4M0E"
api_data = make_api_request(access_token)

if api_data:
    # Process the API data
    print(api_data)
else:
    print("API request failed.")
