import random


def generate_random_number(small, big): # generates a random integer value between min and max
    """
    Return a Random integer between two numbers

    :param small: Smaller number
    :type small: int
    :param big: Larger number
    :type big: int
    :return : A random integer
    :rtype: int

    """
    try:
        if small>big:
            raise ValueError(f"Integer between {small}-{big} cannot be generated ")
    except ValueError as ve:
        print(ve)
        # print(f"specified range not valid {small}-{big}")

    else:
        return random.randint(small, big)


def generate_random_operator(): #generates a random mathematical operator
    """
    Return a Random mathematical operator from addition, subtraction and multiplication

    :rtype: mathematical operator
    """
    return random.choice(['+', '-', '*'])


def calculate(num1, num2, operator): #takes two numbers and operator as arguments and performs the operation on the two numbers

    """
    Returns result of a mathematical operation between two numbers

    :param num1: First number
    :type num1: int
    :param num2: Second number
    :type num2: int
    :param operator: a mathematical operator
    :return: result of the mathematical operation
    """
    # If any specified interval is not valid the generate_random_number()
    # will return a none type object which will cause an error in calculate function
    try:
        if (num1 is None) or (num2 is None):
            raise ValueError("Atleast one of the numbers is not a valid type")

    except ValueError as ve:
        print(ve)

    else:
        # return random.randint(small, big)

        problem = f"{num1} {operator} {num2}"
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        return problem, answer

#Runs a maths quiz
def math_quiz():

    """"
    Runs a maths quiz in which the user is presented with a series of maths questions.
    The user is graded based on his answers
    """
    score = 0
    total_questions = 4
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        first_num = generate_random_number(11, 10)
        second_num = generate_random_number(5, 50)

        operation  = generate_random_operator() #operation

        problem , answer = calculate(first_num, second_num, operation)
        print(f"\nQuestion: {problem}")

        try :
            user_answer = int(input("Your answer: "))

        except ValueError :
            print("Invalid input")
        else:
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1 #adding a point to the current score
            else:
                print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()

