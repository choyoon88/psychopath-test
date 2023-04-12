import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('psychopath-test')

stats = SHEET.worksheet('answers-stats')

data = stats.get_all_values()

username = input("Enter your name: ")
while username.strip() == "":
    username = input("Invalid input. Please enter your name: ")
print(f"Hello, {username}!")

country = input("Enter your country name: ")
while not country.strip():
    country = input("Invalid country name. Please enter your country: ")
print(f"\nHello, {username} from {country}.\nLet us see if you are a psychopath from {country}\n")
