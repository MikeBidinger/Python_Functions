import streamlit as st  # https://streamlit.io/ - This module is not build-in with Python
import requests  # https://pypi.org/project/requests/ - This module is not build-in with Python

st.set_page_config(page_title="API App")

st.title("API App")


def main() -> None:
    url: str = url_selection()
    params: dict = params_selection()
    if url != "":
        response: requests.Response = api_call(url, params)
        show_response(response)


def url_selection() -> str:
    st.subheader("API Selection")
    url: str = st.text_input("Enter the API URL:", placeholder="URL")
    return url


def params_selection() -> dict:
    st.subheader("Parameters Selection")
    params: dict = {}
    params_str: str = st.text_area(
        "Enter the parameters:", placeholder="format=json\nwhere=1=1"
    )
    if params_str != "":
        params_split: list = params_str.split("\n")
        for param in params_split:
            key, value = param.split("=", maxsplit=1)
            params[key] = value
        st.write("Selected parameters:", params)
    return params


def api_call(url: str, params: dict) -> requests.Response:
    return requests.get(url, params)


def show_response(response: requests.Response):
    st.subheader("API Response")
    if response.status_code == 200:
        st.json(response.json(), expanded=False)
    else:
        st.json({"ERROR": response.status_code})


if __name__ == "__main__":
    main()
