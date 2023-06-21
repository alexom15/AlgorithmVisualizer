import random

def generate_random_number(start, end):
    random_number = random.randint(start, end)
    print("Random Number:", random_number)

# Usage example
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

generate_random_number(start, end)
