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

questions = [
    "1) You are looking at a mirror, but unsatisfied, \n\
    Why is that?",
    "2) There is a portrait of a wounded solider. \n\
    Which part of the body is wounded?",
    "3) You are in a dark forest alone in front of a pavilion. \n\
    Suddenly, something passes behind you. What could that might be?",
    "4) You got very thirsty and found a vending machine. \n\
    There is nothing written on the can. \n\
    What is the colour of the liquid you choose?",
    "5) A murderer with a knife is looking for you in the house. \n\
    You are all alone and decides to hide. Where would you hide?",
    "6) You finally decide to kill your enemy you have loathe for 10 years. \n\
    You pick up 5 euro knife instead of 50 euro one from the store. \n\
    Why is that?"]

options = (
    ("a. You do not like of how you look",
     "b. There us a scar on your face",
     "c. You gained weight",
     "d. The mirror is dirty",
     "e. You found a pimple on your face"),
    ("a. Head",
     "b. Leg",
     "c. Arms",
     "d. Eyes",
     "e. Heart"),
    ("a. Wild animal",
     "b. Leaf",
     "c. Person of a different sex",
     "d. Dog",
     "e. Ghost"),
    ("a. Blue",
     "b. Yellow",
     "c. Red",
     "d. No colour",
     "e. Other"),
    ("a. Behind the door",
     "b. Underneath the bed",
     "c. Outside the window",
     "d. Inside the wardrobe",
     "e. Inside the cabinet"),
    ("a. To kill with more pain",
     "b. No need to spend too much money",
     "c. 5 euro one looks sharper",
     "d. Not enough money",
     "e. Advertisement was tempting"),
)

username = input("Enter your name: ").capitalize()
while username.strip() == "":
    username = input("Invalid input. Please enter your name: ")
print(f"Hello, {username}!")

country = input("Enter your country name: ").capitalize()
while not country.strip():
    country = input("Invalid input. Please enter your country: ")

print(f"\nWelcome, {username} from {country}!")
print(f"Let us see if you are a psychopath from {country}\n")
print("=================================================")
print("WARNING: This is not a verified psychopath test.")
print("This is only for entertainment purpose.")
print("=================================================\n")
print("INSTRUCTION:")
print("You will be given 6 questions with 5 answer options each.")
print("Select the one that comes to your mind straight away.")
print("DO NOT OVER THINK!")

start = input("\npress Enter to contiune...")

i = 0
psycho_answers_first = ['d', 'd', 'd', 'd', 'a', 'a']
psycho_answers_second = ['d', 'e', 'd', 'd', 'a', 'a']
user_answers = []

for question in questions:
    print('\n----------------------------------------------------------------')
    print(question)
    print('----------------------------------------------------------------')

    for option in options[i]:
        print(option)
    user_answer = input("Enter a, b, c, d or e: ").lower()

    while user_answer.lower() not in ['a', 'b', 'c', 'd', 'e']:
        user_answer = input("Please answer with a, b, c, d, e: ").lower()
    user_answers.append(user_answer)
    i += 1


def check_answers():
    """
    Check if the user's answer are the same as in the
    two lists of psycho's answer.
    Answers must meet the same alphabet on the same index.
    And count how many same answers were found
    to see if the user is a psychopath
    """
    true_answers = []
    for index, answer in enumerate(user_answers):
        if answer in (psycho_answers_first[index], psycho_answers_second[index]):
            true_answers.append(answer)
    counter = len(true_answers)
    if counter == 0 or counter == 1:
        print(f"\n{username}'s psycho rate is 0! Hooray!")
    elif counter >= 2 and counter <= 4:
        print(f"\n{username}'s psycho rate is a bit high...")
    else:
        print(f"\n{username}... You are a psychopath..")
        print(f"{country} should be warned!")
    print(counter)


print(user_answers)
check_answers()

# if user_answers in (psycho_answers_first, psycho_answers_second):
#     print(f"\n{username}... You are a psychopath")
#     print(f"{country} should be warned!")
# else:
#     print(f"\n{username}... You might not be a psychopath")
#     print(f"People in {country} are safe... for now!")
