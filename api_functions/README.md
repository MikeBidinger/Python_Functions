# Python Functions - [api_functions.py](api_functions.py)

Standardized API functions to save up repetitive work and keep code clean within Python scripting.
These all have basic formats and uses, but they can be customized relatively easily to achieve tailored functionalities.

## Content

-   [Authentication](#authentication)
    -   [Basic Authentication](#basic-authentication)
    -   [API Key Authentication](#api-key-authentication)
    -   [Token-Based Authentication](#token-based-authentication)
-   [main.py](#mainpy)

# Authentication

An API may be secured with authentication requirements.
Below are some of the different authentication methods.

## Basic Authentication

Basic authentication is a simple and fast method of HTTP authentication.
To access the API endpoint, the user must send a username and password to the API provider in the authentication header of the request.
The API provider checks the credentials and, in the case of success, grants access to the user.

```python
import requests
import base64

url: str = "https://"

user: str = ""
password: str = ""
credentials: str = f"{user}:{password}"
encoded: bytes = base64.b64encode(credentials.encode("ascii"))
headers: dict[str, str] = {
    "Authorization": f"Basic {encoded}"
}

response: requests.Response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
```

## API Key Authentication

In API key authentication, the API provider assigns a unique key to each client accessing the API.
The client needs to include their API key as part of the request to authenticate themselves.
The API key can be included anywhere in the request, such as the header, body, or query parameters.
It ultimately depends on the API's design and is communicated to the developers via the API documentation.

```python
import requests

url: str = "https://"

api_key: str = ""
headers: dict[str, str] = {
    "Authorization": f"api-key {api_key}"
}

response: requests.Response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
```

## Token-Based Authentication

Token-based authentication—also called bearer authentication—is a popular authentication method that uses an access token to verify a user's identity.

```python
import requests

url: str = "https://"

token: str = "fhu78ej3-fh37-fy67-56ed-56ddgc5dte45"
headers: dict[str, str] = {
    "Authorization": f"Bearer {token}"
}

response: requests.Response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
```

# [main.py](main.py)

> [!NOTE]
> This script uses the module [streamlit](https://streamlit.io/) and [requests](https://pypi.org/project/requests/).
> These modules are not build-in with Python.

This python script contains a Streamlit application where the API GET request can be made.
Here the URL and the parameters for the API request can be entered.

To run the application use the following commands:

1.  Be sure to be located in the correct directory:

```bash
cd path/to/directory
```

2.  Run the Streamlit application:

```bash
streamlit run main.py
```
