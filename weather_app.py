import streamlit as st
import requests

# App title and description
st.set_page_config(page_title="Weather App", page_icon="☀️")
st.title("🌤️ Weather App - CloudCast")
st.write("Get detailed and real-time weather information for any city around the world!")

# Sidebar with instructions
st.sidebar.title("Instructions")
st.sidebar.write("""
- Enter the name of a city in the input box.
- Get real-time weather details and an image representation of the current weather.
""")

# Input city name
city = st.text_input("Enter the name of a city:")

# API details
api_key = "f2cdbc04706dd14f58a7313ad487ee63"

if city:
    # Fetch weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        # Extracting details
        city_name = data['name']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description'].capitalize()
        weather_icon = data['weather'][0]['icon']
        wind_speed = data['wind']['speed']

        # Displaying the details
        st.header(f"Weather in {city_name}")
        st.write(f"**Temperature:** {temperature}°C (Feels like {feels_like}°C)")
        st.write(f"**Weather:** {weather_description}")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Wind Speed:** {wind_speed} m/s")

        # Display weather icon
        icon_url = f"http://openweathermap.org/img/wn/{weather_icon}.png"
        st.image(icon_url, caption="Current Weather Icon")

        # Background image or themed display
        st.markdown("""
        <style>
        .stApp {
            background-image: url('https://source.unsplash.com/1920x1080/?nature,sky');
            background-size: cover;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.error("City not found. Please check the name and try again.")
