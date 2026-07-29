# Rain Alert App

## Description
An automated weather monitoring application that checks the forecast for the upcoming 12 hours. If rain is predicted, it uses the Twilio API to send an SMS/WhatsApp alert, ensuring you never forget your umbrella.

## Features
- Integrates with the OpenWeatherMap API for accurate weather forecasts.
- Uses the Twilio API to send real-time text alerts.
- Formats the 12-hour forecast into a readable message.
- Secure environment variable management for API keys and phone numbers.

## Technologies
- Python 3.x
- 
equests for RESTful API calls.
- 	wilio for SMS/WhatsApp messaging.


## Installation
1. Clone the repository:
   `ash
   git clone https://github.com/yourusername/rain-alert.git
   cd rain-alert
   `
2. Install dependencies:
   `ash
   pip install -r requirements.txt
   `
3. Open main.py and replace the placeholder variables (like YOUR_TWILIO_ACCOUNT_SID, YOUR_OPENWEATHER_APPID) with your actual API keys and phone numbers.

## Usage
Run the script (or set it up on a cron job) to check the weather and send alerts:
`ash
python main.py
`

## Project Structure
- main.py: The main API integration and logic script.
- .env: Environment variables configuration.

## Requirements
- Python 3.9+
- OpenWeatherMap Account (Free Tier)
- Twilio Account

## Future Improvements
- Host the script on a cloud provider (e.g., PythonAnywhere, AWS Lambda) to run daily at 7 AM.
- Support for multiple user locations and phone numbers.

## License
This project is licensed under the MIT License.