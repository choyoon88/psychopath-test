import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import sys

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

# data = stats.get_all_values()

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
     "b. There is a scar on your face",
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

print("Welcome to the Psychopath Test")
print("See if you are a psychopath or not")
username = input("Enter your name: ").capitalize()
while username.strip() == "":
    username = input("Invalid input. Please enter your name: ")
print(f"Hello, {username}!")

user_country = input("Enter your country name: ").capitalize()
while not user_country.strip():
    user_country = input("Invalid input. Please enter your country: ")


print(f"\nWelcome, {username} from {user_country}!")
print(f"Let us see if you are a psychopath from {user_country}\n")
print("=================================================")
print("WARNING: This is not a verified psychopath test.")
print("This is only for entertainment purpose.")
print("=================================================\n")
print("INSTRUCTION:")
print("You will be given 6 questions with 5 answer options each.")
print("Select the one that comes to your mind straight away.")
print("DO NOT OVER THINK!")


start = input("\npress Enter to contiune...")

psycho_answers_first = ['d', 'd', 'd', 'd', 'a', 'a']
psycho_answers_second = ['d', 'e', 'd', 'd', 'a', 'a']
user_answers = []


def start_test():
    """
    Starting the test
    """
    i = 0
    for question in questions:
        print('\n------------------------------------------------------------')
        print(question)
        print('------------------------------------------------------------')

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
        print(f"{user_country} should be warned!")


def update_answer_sheet(data):
    """
    Update user's answer on the user-answers spreadsheet
    """
    answer_worksheet = SHEET.worksheet('user-answers')
    answer_worksheet.append_row(data)
    print("Your answers has been successfully updated on the shreadsheet")


def update_stats_sheet():
    """
    Increment +1 on each selected answer for each question
    to gather a statistic result of the total number of answers
    for each questions.
    """
    stats_worksheet = SHEET.worksheet('answers-stats')
    row_map = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6}

    for ind, answer in enumerate(user_answers):
        cell = stats_worksheet.cell(row=row_map[answer], col=ind+2)
        cell.value = int(cell.value) + 1
        stats_worksheet.update_cell(row_map[answer], ind+2, cell.value)


def menu():
    """
    Show the selections to action after the test is done.
    """
    print("\nMENU")
    print("A - Restart Test")
    print("B - Show Test Statistics")
    print('C - End Test')
    action = input("Enter A, B or C: ").capitalize()

    while action not in ['a', 'b', 'c', 'A', 'B', 'C']:
        print("/nInvalid input.")
        action = input("Enter A, B or C: ").capitalize()

    if action == 'A':
        print("\nRestarting Test...")
        start_test()
        check_answers()
        update_answer_sheet(user_answers)
        update_stats_sheet()
    elif action == 'B':
        print("\nWelcome to Psychotest statistics.")
        print("Check how many people choose the answers for each question.")
        test_result = SHEET.worksheet('answers-stats').get_all_values()
        pprint(test_result)
    elif action == 'C':
        print("/nTest Ending. Good bye")
        sys.exit()


start_test()
check_answers()
update_answer_sheet(user_answers)
update_stats_sheet()
menu()

# if user_answers in (psycho_answers_first, psycho_answers_second):
#     print(f"\n{username}... You are a psychopath")
#     print(f"{country} should be warned!")
# else:
#     print(f"\n{username}... You might not be a psychopath")
#     print(f"People in {country} are safe... for now!")

# if answer == 'a':
#     cell_to_update = 'B2'
#     current_val = stats_worksheet.acell(cell_to_update).value
#     new_val = int(current_val) + 1
#     stats_worksheet.update_acell(cell_to_update, new_val)
