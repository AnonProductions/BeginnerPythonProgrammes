operations = {
    1: '+',
    2: '-',
    3: '*',
    4: '/'
}

try:
    # Displaying the possibilities
    for key, value in operations.items():
        print(f"Enter {key} to perform {value} operation")
    user_input = int(input())

    # Taking Numbers from user
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))

    # Logic of the programme
    if user_input == 1:
        print(f"The result is {first_num + second_num}")

    elif user_input == 2:
        print(f"The result is {first_num - second_num}")

    elif user_input == 3:
        print(f"The result is {first_num * second_num}")

    elif user_input == 4:
        print(f"The result is {first_num / second_num}")

    else:
        print("You have entered an invalid input!")

except:
    print("Sorry, the programme can't handle this")