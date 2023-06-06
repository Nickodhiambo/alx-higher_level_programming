def fizzbuzz():
    """Prints numbers from 1 to 100

    For multiples of three, prints Fizz in place of the number.
    For multiples of five, prints Buzz in place of the number.
    For multiples of three and five, prints FizzBuzz in place of the number.
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(num), end="")
