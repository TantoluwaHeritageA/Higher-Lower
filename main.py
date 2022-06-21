# Process
# '''
# - print the logo
# - print the name of the celebrity, the profession and country
# - print the vs logo
# - print another name of the celebrity, the profession and country
# - create an input that accepts 'A' or 'B'
# - A represents the first celebrity, B represents second celebrity
# - The question  is to ask who has more followers, target the number of followers
# - compare A followers to B followers, and check if it is correct
# - if it is correct count 1 if it is wrong end game and print the final result
# '''

import random
from art import logo
from art import vs
from game_data import data
print(logo)

# print(
#     f"Compare A: {random_name}, a {random_profession}, from {random_country}")

# print(
#     f"Against B:  {random_name1}, a {random_profession1}, from {random_country1}")




# option 1

def get_data(random_data):
    random_name = data[random_data]['name']
    random_profession = data[random_data]['description']
    random_country = data[random_data]['country']
    return f"{random_name}, a {random_profession}, from {random_country}"

def check_answer(guess, a_followers, b_followers):
  
    if a_followers > b_followers:
        if guess == "A":
            return True
        else:
            return False
    elif b_followers > a_followers:
        if guess == "B":
            return True
        else:
            return False
        
score = 0
continue_game = True
option_b = random.randint(0, len(data))
while continue_game:
    option_a = option_b
    option_b = random.randint(0, len(data))
    while option_a == option_b:
        option_b = random.randint(0, len(data))
        
    print(f"Compare A: {get_data(option_a)}.")
    print(vs)
    print(f"Against B: {get_data(option_b)}.")
    guess = input(
            "Who has more followers? Type 'A' or 'B': ").upper() 
    a_follower_count = data[option_a]['follower_count']
    b_follower_count = data[option_b]['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Your final score: {score}")


# my code

# continue_game = True
# while continue_game:
#     new_range = random.randint(0, len(data))
#     new_follower = data[new_range]['follower_count']
#     user_choice = input(
#         "Who has more followers? Type 'A' or 'B': ").upper()
#     num_of_new_fflw = int(new_follower)
#     num_of_fllw = int(random_follower)
#     num_of_fllw_b = int(random_follower1)
#     if user_choice == "A" and num_of_fllw > num_of_fllw_b:
#         user_choice = num_of_fllw
#         counter += 1
#         print(f" the score is {counter}")
#         print(f"{key_word}{first_option}")
#         print(vs)
#         second_option = data[new_range]['name'] + ", a " + data[new_range]['description'] + ", from " + data[new_range]['country']
#         print(f"{key_word2}{second_option}")
#         if user_choice == "A" and num_of_fllw > num_of_new_fflw:
#             user_choice = num_of_fllw
#             counter += 1
#             print(f" the score is {counter}")
#             print(f"{key_word}{first_option}")
#             print(vs)
#             second_option = data[new_range]['name'] + ", a " + data[new_range]['description'] + ", from " + data[new_range]['country']
        
#         elif user_choice == "A" and num_of_new_fflw > num_of_fllw:
#             user_choice = num_of_new_fflw
#             counter += 1
#             print(f" the score is {counter}")
#             print(f"{key_word}{first_option}")
#             print(vs)
#             second_option = data[new_range]['name'] + ", a " + data[new_range]['description'] + ", from " + data[new_range]['country']
       
#         elif user_choice == "B" and num_of_new_fflw > num_of_fllw:
#             user_choice = num_of_new_fflw
#             print(user_choice)
#             counter += 1
#             print(f" the score is {counter}")
#             print(f"{key_word}{first_option}")
#             print(vs)
#             second_option = data[new_range]['name'] + ", a " + data[new_range]['description'] + ", from " + data[new_range]['country']
#         elif user_choice == "B" and num_of_fllw  > num_of_new_fflw:
#             user_choice = num_of_fllw
#             print(user_choice)
#             counter += 1
#             print(f" the score is {counter}")
#             print(f"{key_word}{first_option}")
#             print(vs)
#             second_option = data[new_range]['name'] + ", a " + data[new_range]['description'] + ", from " + data[new_range]['country']
#         elif user_choice == "A" and num_of_new_fflw < num_of_fllw or user_choice == "B" and num_of_fllw  < num_of_new_fflw:
#            print(f"Your final score is {counter}")
#            continue_game = False
#         # print(user_choice)
#     elif user_choice == "A" and num_of_fllw < num_of_fllw_b:
#         user_choice = num_of_fllw
#         print(f"Your final score is {counter}")
#         continue_game = False
#         # print(user_choice)
#     elif user_choice == "B" and num_of_fllw_b > num_of_fllw:
#         user_choice = num_of_fllw_b
#         counter += 1
#         print(f" the score is {counter}")
#         first_option = second_option
#         print(f"{key_word}{first_option}")
#         print(vs)
#         second_option = data[new_range]['name'] + ", a " + data[new_range]['description'] + ", from " + data[new_range]['country']
#         print(f"{key_word2}{second_option}")
#         if user_choice == "B" and num_of_new_fflw > num_of_fllw_b:
#             user_choice = num_of_new_fflw
#             counter += 1
#             print(f" the score is {counter}")
#             print(f"{key_word}{first_option}")
#             print(vs)
#             second_option = data[new_range]['name'] + ", a " + data[new_range]['description'] + ", from " + data[new_range]['country']
#         elif user_choice == "B" and num_of_fllw_b < num_of_new_fflw:
#             user_choice = num_of_fllw
#             print(f"Your final score is {counter}")
#             continue_game = False
#         # print(user_choice)
#     elif user_choice == "B" and num_of_fllw_b < num_of_fllw:
#         user_choice = num_of_fllw_b
#         print(f"Your final score is {counter}")
#         continue_game = False

        # print(user_choice)

