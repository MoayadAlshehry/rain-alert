from datetime import datetime
import requests
from twilio.rest import Client

# --- CONFIGURATION (REPLACE THESE PLACEHOLDERS WITH YOUR DETAILS) ---
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"
weather_appid = "YOUR_OPENWEATHER_APPID"
from_number = "YOUR_TWILIO_PHONE_NUMBER"
to_number = "YOUR_PERSONAL_PHONE_NUMBER"
# --------------------------------------------------------------------

if account_sid == "YOUR_TWILIO_ACCOUNT_SID":
    print("Error: Please replace the API placeholders in main.py before running.")
    exit(1)

weather_params = {
    "lat": 18.092451995626632,
    "lon": 42.71950085792554,
    "appid": weather_appid,
    "cnt" : 6
}

try:
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    print(f"Error fetching weather data: {e}")
    exit(1)

weather_ids = [w["weather"][0]["id"] for w in data["list"]]

client = Client(account_sid, auth_token)

if any(w_id < 800 for w_id in weather_ids):
    try:
        message = client.messages.create(
            body="It's going to rain today.",
            from_=from_number,
            to=to_number,
        )
        print(f"Rain alert sent: {message.status}")
    except Exception as e:
        print(f"Failed to send rain alert: {e}")

mesg = ""
for cast in data["list"]:
    time_str = datetime.strptime(cast["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%I %p").lstrip("0")
    mesg += f"{time_str} : {cast['weather'][0]['description']}\n"

try:
    message = client.messages.create(
        body=f"Weather today at location:\n{mesg}",
        from_=from_number,
        to=to_number,
    )
    print(f"Weather forecast sent: {message.status}")
except Exception as e:
    print(f"Failed to send forecast: {e}")
