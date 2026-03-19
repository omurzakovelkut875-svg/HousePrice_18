import streamlit as st
import requests

st.title('Предсказание цены дома')

api_url = "http://127.0.0.1:8001/predict"


bedrooms = st.number_input("Количество спален", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Количество ванных комнат", min_value=1, max_value=10, value=2)
sqft = st.number_input("Площадь (кв. фут)", min_value=100, max_value=10000, value=1500)
location = st.text_input("Район/город", "Downtown")
year_built = st.number_input("Год постройки", min_value=1800, max_value=2026, value=2000)


house_data = {
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "sqft": sqft,
    "location": location,
    "year_built": year_built
}


if st.button("Предсказать цену"):
    try:
        response = requests.post(api_url, json=house_data, timeout=10)

        if response.status_code == 200:
            result = response.json()

            st.json(result)

        else:

            st.json({"Error": f"Ошибка API: {response.status_code}"})

    except requests.exceptions.RequestException:

        st.json({"Answer": "Approved"})