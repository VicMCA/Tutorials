for number in range(1, 100):
    if number % 3 == 0 and not number % 5 == 0:
        print("fizz")
    elif not number % 3 == 0 and number % 5 == 0:
        print("buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    else:
        print(number)