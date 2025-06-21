import random
from statistics import average, standard_deviation

def throw_needles(n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if (x**2 + y**2) ** 0.5 <= 1:
            inside_circle += 1

    return (4 * inside_circle) / n

def estimate(n, attempts=1):
    estimates = []
    for _ in range(attempts):
        estimate_pi = throw_needles(n)
        estimates.append(estimate_pi)

    avg_estimate = average(estimates)
    std_dev_estimate = standard_deviation(estimates)
    print(f"Average estimate of Pi: {avg_estimate:.6f}")
    print(f"Standard deviation of estimates: {std_dev_estimate:.6f}")

    return avg_estimate, std_dev_estimate

def estimate_pi(accuracy, attempts=1):
    n = 1000
    sigma = accuracy

    while sigma >= accuracy / 1.96:
        average, sigma = estimate(n, attempts)
        n *= 2

    return average

if __name__ == "__main__":
    estimate_pi(0.01, 1000)
