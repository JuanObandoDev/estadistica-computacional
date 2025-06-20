import random

def average(x):
    return sum(x) / len(x)

def variance(x):
    avg = average(x)
    sum = 0
    for i in x:
        sum += (i - avg) ** 2

    return sum / len(x)

def standard_deviation(x):
    return variance(x) ** 0.5

if __name__ == "__main__":
    numbers = [random.randint(1, 21) for _ in range(20)]
    avg = average(numbers)
    var = variance(numbers)
    std_dev = standard_deviation(numbers)
    print(f"The average is: {avg:.2f}")
    print(f"The variance is: {var:.2f}")
    print(f"The standard deviation is: {std_dev:.2f}")
    print(f"The numbers are: {numbers}")