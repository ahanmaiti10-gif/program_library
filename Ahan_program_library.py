print('Hello; welcome to my program library!')
while True:
    print('What program would you like to run?:')
    print('1. Beta Program')
    print('2. Dishonest Capacity Calculator')
    print('3. Number Guessing Game')
    print('4. Login System')
    print('5. Word Guessing Game')
    print('6. Probability Simulator')
    print('7. Rock, Paper, Scissors')
    print('8. Calculators')
    print('9. String Repeater')
    print('10. Temperature Converter')
    selection = input('Enter the number of the program you want to run: ') #0 is for exiting the program library

    if selection == '0':
        print('Exiting the program library. Goodbye!')
        break

    elif selection == '1':
        print('Running Beta Program...')

        print('Hello, world')
        print('What is your name?')
        my_name = input('<')
        print('It is good to meet you, ' + my_name)
        print('The length of your name is ' + str(len(my_name)) + ' characters long.')
        print('What is your age?')
        my_age = input('<')
        if my_age == str(round(float(my_age))):
            print('You will be ' + str(int(float(my_age)) + 1) + ' years old next year.')
        else:
            print('You will be ' + str(float(my_age) + 1) + ' years old next year.')
        if float(my_age) < 18:
            print('You are a minor.')
        elif float(my_age) < 65:
            print('You are an adult.')
        else:
            print('You are a senior citizen.')

    elif selection == '2':
        print('Running Dishonest Capacity Calculator...')
        
        print('Enter TB or GB for the advertised unit:')
        unit = input('<')
        if unit == 'TB' or unit == 'tb':
            discrepancy = 1000000000000 / 1099511627776
        elif unit == 'GB' or unit == 'gb':
            discrepancy = 1000000000 / 1073741824
        print('Enter the advertised capacity:')
        advertised_capacity = float(input('<'))
        real_capacity = str(round(advertised_capacity * discrepancy, 2))
        print('The real capacity is ' + real_capacity + ' ' + unit)

    elif selection == '3':
        print('Running Number Guessing Game...')
        import random
        attempts = 0
        print('Please enter the range for the number to guess (e.g., 1-100):')
        lower_bound = int(input('Lower bound: '))
        upper_bound = int(input('Upper bound: '))
        number_to_guess = random.randint(lower_bound, upper_bound)
        print('I have selected a number between ' + str(lower_bound) + ' and ' + str(upper_bound) + '. Can you guess it?')
        while True:
            attempts += 1
            guess = int(input('Your guess: '))
            if guess < number_to_guess:
                print('Too low! Try again.')
            elif guess > number_to_guess:
                print('Too high! Try again.')
            else:
                if attempts == 1:
                    print('Wow! You guessed the number on your first try!')
                else:
                    print('Congratulations! You guessed the number in ' + str(attempts) + ' attempts!')
                break

    elif selection == '4':
        print('Running Login System...')
        print('What will be your difficulty? (easy / medium / hard)')
        difficulty = input('<')
        if difficulty == 'easy':
            user = input('Username: ')
            pass_ = input('Password: ')
            while True:
                print('Enter username:')
                username = input('<')
                print('Enter password:')
                password = input('<')
                if username == user and password == pass_:
                    print('Login successful! Welcome, ' + user + '.')
                    break
                else:
                    print('Login failed. Please try again.')

        elif difficulty == 'medium':
            user = 'admin'
            pass_ = 'password123'
            while True:
                print('Enter username:')
                username = input('<')
                print('Enter password:')
                password = input('<')
                if username == user and password == pass_:
                    print('Login successful! Welcome, admin.')
                    break
                else:
                    print('Login failed. Please try again.')
                    

        elif difficulty == 'hard':
            import random
            user = random.choice(['admin', 'user', 'guest', 'root'])
            pass_ = random.choice(['password123', 'letmein', '123456', 'adminpass'])
            while True:
                print('Enter username:')
                username = input('<')
                if username == user:
                    print(user + ', nter password:')
                    password = input('<')
                    if password == pass_:
                        print('Login successful! Welcome, ' + user + '.')
                        break
                    else:
                        print('Login failed. Please try again.')
                else:
                    print('Login failed. Please try again.')
        
        else:
            print('Please enter a valid difficulty level (easy / medium / hard)')

            break

    elif selection == '5':
        print('Running Word Guessing Game...')
        import random
        words = ['python', 'programming', 'library', 'guessing', 'game']
        word_to_guess = random.choice(words)
        guessed_letters = []
        attempts = 0
        print('I have selected a word. Can you guess it?')
        while True:
            attempts += 1
            display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
            print('Word: ' + ' '.join(display_word))
            print('Do you want to guess the word? (yes/no)')
            if input('<').lower() == 'yes':
                print('Enter your guess for the word:')
                word_guess = input('<').lower()
                if word_guess == word_to_guess:
                    if attempts == 1:
                        print('Incredible! You guessed the word on your first try!')
                    else:
                        print('Congratulations! You guessed the word "' + word_to_guess + '" in ' + str(attempts) + ' attempts!')
                    break   
                else:
                    print('Wrong guess. Try again.')
            else:
                print('Enter a letter to guess:')
                letter_guess = input('<').lower()
                if letter_guess in guessed_letters:
                    print('You already guessed that letter. Try again.')
                elif letter_guess in word_to_guess:
                    guessed_letters.append(letter_guess)
                    print('Good guess!')
                    if all(letter in guessed_letters for letter in word_to_guess):
                        if attempts == 1:
                            print('Amazing! You guessed the word on your first try!')
                        else:
                            print('Congratulations! You guessed the word "' + word_to_guess + '" in ' + str(attempts) + ' attempts!')
                            break

                else:
                    guessed_letters.append(letter_guess)
                    print('Wrong guess. Try again.')

                
    elif selection == '6':
        print('Running Probability Simulator...')
        import random
        print('What event do you want to simulate? (e.g., coin flip, dice roll, card draw)')
        event = input('<')
        print('How many trials do you want to run?')
        trials = int(input('<'))
        if event == 'coin flip':
            outcomes = ['heads', 'tails']
            results = {'heads': 0, 'tails': 0}
            for _ in range(trials):
                outcome = random.choice(outcomes)
                results[outcome] += 1
            print('Results after ' + str(trials) + ' coin flips:')
            print('Heads: ' + str(results['heads']) + ' (' + str(round(results['heads'] / trials * 100, 2)) + '%)')
            print('Tails: ' + str(results['tails']) + ' (' + str(round(results['tails'] / trials * 100, 2)) + '%)')

        elif event == 'dice roll':
            outcomes = [1, 2, 3, 4, 5, 6]
            results = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
            for _ in range(trials):
                outcome = random.choice(outcomes)
                results[outcome] += 1
            print('Results after ' + str(trials) + ' dice rolls:')
            for number in outcomes:
                print(str(number) + ': ' + str(results[number]) + ' (' + str(round(results[number] / trials * 100, 2)) + '%)')

        elif event == 'card draw':
            suits = ['H', 'D', 'C', 'S'] #abbreviations for Hearts, Diamonds, Clubs, Spades
            ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',]
            deck = [rank + ' of ' + suit for suit in suits for rank in ranks]
            results = {card: 0 for card in deck}
            for _ in range(trials):
                card_drawn = random.choice(deck)
                results[card_drawn] += 1
            print('Results after drawing a card from the deck ' + str(trials) + ' times:')
            for card in deck:
                print(card + ': ' + str(results[card]) + ' (' + str(round(results[card] / trials * 100, 2)) + '%)')
            print('*[H, D, C, S] are abbreviations for [Hearts, Diamonds, Clubs, Spades].*')

        else:
            print('Event not recognized. Please enter "coin flip", "dice roll", or "card draw".')

    elif selection == '7':
        print('Running Rock, Paper, Scissors...')
        import random
        choices = ['rock', 'paper', 'scissors']
        player_score = 0
        computer_score = 0
        print('Enter your choice (rock/paper/scissors):')
        while player_score < 2 and computer_score < 2:
            print('\n Choose rock, paper, or scissors')
            user_choise = input('<').lower()
            computer_choice = random.choice(choices)
            if user_choise not in choices:
                print('Invalid choice. Please choose rock, paper, or scissors.')
                continue
            print('You chose: ' + user_choise)
            print('Computer chose: ' + computer_choice)
            if user_choise == computer_choice:
                print('It\'s a tie!')
            elif (user_choise == 'rock' and computer_choice == 'scissors') or (user_choise == 'paper' and computer_choice == 'rock') or (user_choise == 'scissors' and computer_choice == 'paper'):
                print('You win this round!')
                player_score += 1
            else:
                print('Computer wins this round!')
                computer_score += 1
            print('Score - You: ' + str(player_score) + ' Computer: ' + str(computer_score))
        if player_score == 2:
            print('Congratulations! You won the game!')
        else:
            print('Computer wins the game! Better luck next time!')

    elif selection == '8':
        print('Running Calculator...')
        print('Which mode do you want to use? (basic / miscellaneous)')
        choose_mode = input('<')
        if choose_mode == 'basic':
            print('Enter the first number:')
            num1 = float(input('<'))
            print('Enter the operator (+, -, *, /):')
            operator = input('<')
            print('Enter the second number:')
            num2 = float(input('<'))
            if operator == '+':
                result = num1 + num2
                print(str(num1) + ' + ' + str(num2) + ' = ' + str(result))
            elif operator == '-':
                result = num1 - num2
                print(str(num1) + ' - ' + str(num2) + ' = ' + str(result))
            elif operator == '*':
                result = num1 * num2
                print(str(num1) + ' * ' + str(num2) + ' = ' + str(result))
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                    print(str(num1) + ' / ' + str(num2) + ' = ' + str(result))
                else:
                    print('Error: Division by zero is not allowed.')
            else:
                print('Error: Invalid operator. Please enter one of +, -, *, or /.')
        elif choose_mode == 'miscellaneous':
            print('Enter the first number:')
            num1 = float(input('<'))
            print('Enter the operator (sqrt, ^, log):')
            operator = input('<')
            print('Enter the second number:')
            num2 = float(input('<'))
            if operator == 'sqrt':
                if num1 >= 0:
                    result = num1 ** 0.5
                    print('The square root of ' + str(num1) + ' is ' + str(result))
                else:
                    print('Error: Cannot calculate the square root of a negative number.')
            elif operator == '^':
                result = num1 ** num2
                print(str(num1) + ' raised to the power of ' + str(num2) + ' is ' + str(result))
            elif operator == 'log':
                import math
                if num1 > 0 and num2 > 0 and num2 != 1:
                    result = math.log(num1, num2)
                    print('The logarithm of ' + str(num1) + ' to the base ' + str(num2) + ' is ' + str(result))
                else:
                    print('Error: For logarithm, the first number must be greater than 0, the base must be greater than 0 and not equal to 1.')
            else:
                print('Error: Invalid operator. Please enter "sqrt", "^", or "log".')
        else:
            print('Invalid mode. Please enter "basic" or "miscellaneous".')

    elif selection == '9':
        print('Running String Repeater...')
        i = 1
        print('Enter the string you want to repeat:')
        string_to_repeat = input('<')
        print('Enter the number of times to repeat the string:')
        repeat_count = int(input('<'))
        print('Would you like to see the count of each character in the string? (yes/no):')
        see_count = input('<').lower()
        if see_count == 'yes':
            for i in range(repeat_count):
                print(str(i + 1) + '. ' + string_to_repeat)
                i = i + 1
        elif see_count == 'no':
            for i in range(repeat_count):
                print(string_to_repeat)
                i = i + 1
        else:
            print('Invalid input. Please enter "yes" or "no".')

    elif selection == '10':
        print('Running Temperature Converter...')
        print('Enter the temperature you want to convert (e.g., 100C, 212F, 373.15K):')
        temp_input = input('<')
        if temp_input.endswith('C') or temp_input.endswith('c'):
            temp_c = float(temp_input[:-1])
            temp_f = (temp_c * 9/5) + 32
            temp_k = temp_c + 273
            print(str(temp_c) + '°C is equal to ' + str(temp_f) + '°F and ' + str(temp_k) + 'K.')
        elif temp_input.endswith('F') or temp_input.endswith('f'):
            temp_f = float(temp_input[:-1])
            temp_c = (temp_f - 32) * 5/9
            temp_k = temp_c + 273
            print(str(temp_f) + '°F is equal to ' + str(temp_c) + '°C and ' + str(temp_k) + 'K.')
        elif temp_input.endswith('K') or temp_input.endswith('k'):
            temp_k = float(temp_input[:-1])
            temp_c = temp_k - 273
            temp_f = (temp_c * 9/5) + 32
            print(str(temp_k) + 'K is equal to ' + str(temp_c) + '°C and ' + str(temp_f) + '°F.')
        else:
            print('Invalid input. Please enter a temperature in the format of a number followed by C, F, or K (e.g., 100C, 212F, 373.15K).')

    else:
        print('Invalid selection. Please enter a number from 1 to 5.')

    continue_program = input('Do you want to run another program? (yes/no): ')
    if continue_program.lower() != 'yes':
        print('Thank you for using my program library. Goodbye!')
        break
