import random

def average(x):
    return sum(x) / len(x)

if __name__ == "__main__":
    numbers = [random.randint(1, 21) for _ in range(20)]
    avg = average(numbers)
    print(f"The average is: {avg:.2f}")