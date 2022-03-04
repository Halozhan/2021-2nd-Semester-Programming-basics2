import random

def main():
    random_numbers = list()
    
    count = 0
    while (count<6):
        random_numbers.append(random.randint(1, 45))
        count += 1
    
    for i in random_numbers:
        print(i, end=" ")


if __name__ == "__main__":
    main()