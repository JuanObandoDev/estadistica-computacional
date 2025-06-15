from walker import TraditionalWalker
from camp import Camp
from coordinate import Coordinate

def walking (camp, walker, step):
    start = camp.get_coordinate(walker)
    for _ in range(step):
        camp.move_walker(walker)

    return start.distance(camp.get_coordinate(walker))

def simulation(step, attempts, walker_class):
    walker = walker_class("Walker #1")
    origin = Coordinate(0, 0)
    distances = []

    for _ in range(attempts):
        camp = Camp()
        camp.add_walker(walker, origin)
        simulation = walking(camp, walker, step)
        distances.append(round(simulation, 1))

    return distances

def main(distances, attempts, walker_class):
    for step in distances:
        distances = simulation(step, attempts, walker_class)
        prom = round(sum(distances) / len(distances), 4)
        maximum = max(distances)
        minimum = min(distances)
        print(f'{walker_class.__name__} random walk of {step} steps')
        print(f'Average distance: {prom}, Max distance: {maximum}, Min distance: {minimum}\n')

if __name__ == "__main__":
    distances = [10, 100, 1000, 10000]
    attempts = 100

    main(distances, attempts, TraditionalWalker)