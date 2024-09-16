# Exercise Tracking Automation

This project automates the process of tracking your workouts and logging the details into a Google Sheet using two APIs:

1. Nutritionix Exercise API - Calculates the calories burned based on the exercise you performed.
2. Sheety API - Logs the exercise details into a Google Sheet for tracking purposes.

## Project Overview

The script prompts the user for details about the exercise they performed and uses the Nutritionix API to retrieve information
such as the duration of the exercise and calories burned. The resulting data is then automatically saved to a Google Sheet via the Sheety API, using either Basic or Bearer Token authentication.

## Setup and Requirements

Make sure you have Python 3.x installed along with the following libraries:

- requests
- datetime
- os

Install the necessary libraries using: `pip install requests`

## Environment Variables

The script requires several environment variables for API authentication and access. You can set these up using a .env file or through your system environment variables.

<br>
| Variable Name       | Description                                        |
|---------------------|----------------------------------------------------|
| `NT_APP_ID`         | Your Nutritionix API App ID                        |
| `NT_APP_KEY`        | Your Nutritionix API App Key                       |
| `NT_SHEETY_ENDPOINT`| The endpoint for your Sheety API                   |
| `NT_USERNAME`       | (For Basic Authentication) Your Sheety API username|
| `NT_PASSWORD`       | (For Basic Authentication) Your Sheety API password|
| `NT_TOKEN`          | (For Bearer Token Authentication) Your Sheety token|

<br>

## Setting Up the Sheety API

You need to create a Google Sheet and set up a Sheety API project to interact with it. Follow the instructions at <a href='https://sheety.co/docs/authentication.html'> Sheety Documentation</a> to set up an endpoint that allows you to log data into your sheet.


## How It Works
- User Input: The script prompts the user to input the exercise they performed (e.g., "ran 5 kilometers" or "biked for 30 minutes").

- API Call to Nutritionix: The input is sent to the Nutritionix Exercise API, which returns detailed information about the workout (e.g., exercise type, duration, and calories burned).

- Data Logging to Google Sheet: The script then logs this data into a Google Sheet using the Sheety API.<br>

The sheet will log the following information for each workout:

- Date
- Time
- Exercise name
- Duration (in minutes)
- Calories burned

## Example Usage

- Clone the repository or download the script.
- Ensure all environment variables are set.
- Run the script: `python main.py`
- Enter the exercise you did. For example: <br>
```vbnet

Tell me what exercise you did:
Ran 5 kilometers

```

- The script will log the exercise details into your Google Sheet automatically.

## Authentication

The script supports both Basic Authentication and Bearer Token Authentication for the Sheety API. <br>
Depending on your Sheety setup, you can switch between the two methods by uncommenting the relevant authentication section.

- Basic Authentication requires the NT_USERNAME and NT_PASSWORD environment variables.
- Bearer Token Authentication uses the NT_TOKEN environment variable.

## References
- <a href='https://sheety.co/docs/authentication.html'>Sheety Authenticsation </a>
- <a href='https://sheety.co/docs'>Sheety Documentation</a>
- <a href='https://requests.readthedocs.io/en/latest/user/authentication/'>Python Request Authentication Guide</a>
- <a href='https://docx.syndigo.com/developers/docs/nutritionix-api-guide'>Nutritionix API Guide</a>
- <a href='https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise'>Nutritionix API Parameters Guide</a>
