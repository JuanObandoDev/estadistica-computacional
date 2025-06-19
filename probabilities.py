import random

def throw_two_dice(throws):
    secuency = []
    for _ in range(throws):
        throw1 = random.choice([1, 2, 3, 4, 5, 6])
        throw2 = random.choice([1, 2, 3, 4, 5, 6])
        secuency.append((throw1, throw2))
    
    return secuency

def throw_dice(throws):
    secuency = []
    for _ in range(throws):
        throw = random.choice([1, 2, 3, 4, 5, 6])
        secuency.append(throw)
    
    return secuency

def main(throws, attempts, two_dice=False):
    throw_array = []
    if two_dice:
        for _ in range(attempts):
            secuency = throw_two_dice(throws)
            throw_array.append(secuency)

        throw_with_twelve = 0
        for throw in throw_array:
            if (1, 2) in throw:
                throw_with_twelve += 1
            
        probability = throw_with_twelve / attempts
        print(f"Probability of throwing a 1 and a 2 in {throws} throws with two dice: {probability:.4f}")
    else:
        for _ in range(attempts):
            secuency = throw_dice(throws)
            throw_array.append(secuency)

        throw_with_one = 0
        for throw in throw_array:
            if 1 not in throw:
                throw_with_one += 1
            
        probability = throw_with_one / attempts
        print(f"Probability of not throwing a 1 in {throws} throws with one die: {probability:.4f}")

if __name__ == "__main__":
    throws = int(input("Enter the number of throws: "))
    attempts = int(input("Enter the number of attempts: "))
    two_dice = input("Throw two dice? (yes/no): ").strip().lower() == 'yes'

    main(throws, attempts, two_dice)