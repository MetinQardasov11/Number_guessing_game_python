import random

ten_num_counter = 0
six_num_counter = 0
four_num_counter = 0
number_of_guess = 0
max_number_of_guess = 13
numberTrue_placeTrue = 0
numberTrue_placeFalse = 0


ten_num_list = []
six_choice_list = []
four_choice_list = []

while ten_num_counter < 10:
    ten_num_gen = int(random.random()*100)
    ten_num_list.append(ten_num_gen)
    ten_num_counter += 1


while six_num_counter < 6:
    six_choice = random.choice(ten_num_list)
    six_choice_list.append(six_choice)
    six_num_counter += 1


while four_num_counter < 4:
    four_choice = random.choice(six_choice_list)
    if four_choice_list.count(four_choice) == 0:
        four_choice_list.append(four_choice)
        four_num_counter += 1


print(f'Random ten number: {ten_num_list}')   
print('6 number out of 10 selected: {}'.format(six_choice_list))
print('4 number out of 6 selected:', four_choice_list)


while number_of_guess < max_number_of_guess:
    guess_number = int(input('Input the guess number: '))
    guess_place = int(input('Enter the guess place of number: '))
    print('{} umber of guess left'.format(max_number_of_guess-number_of_guess))
    number_of_guess += 1
    
    number_guess_counter = four_choice_list.count(guess_number)
    try:
        place_guess_counter = four_choice_list.index(guess_number)
    except:
        print('Both of the numbers are false!!!')
    
    
    
    
    if number_guess_counter > 0 and place_guess_counter == guess_place:
        numberTrue_placeTrue += 1
        
    elif (number_guess_counter > 0 and place_guess_counter != guess_place):
        numberTrue_placeFalse += 1
    
    print('True: ',numberTrue_placeTrue)
    print('False: ',numberTrue_placeFalse)