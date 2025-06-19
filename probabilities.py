import random

def throw_dice(throws):
    secuency = []
    for _ in range(throws):
        throw = random.choice([1, 2, 3, 4, 5, 6])
        secuency.append(throw)
    
    return secuency

def main(throws, attempts):
    throw_array = []
    for _ in range(attempts):
        secuency = throw_dice(throws)
        throw_array.append(secuency)

    throw_with_one = 0
    for throw in throw_array:
        if 1 not in throw:
            throw_with_one += 1

    probability = throw_with_one / attempts
    print(f"Probability of not throwing a 1 in {throws} throws: {probability:.4f}")

if __name__ == "__main__":
    throws = int(input("Enter the number of throws: "))
    attempts = int(input("Enter the number of attempts: "))

    main(throws, attempts)