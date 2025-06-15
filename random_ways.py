from walker import TraditionalWalker
from camp import Camp
from coordinate import Coordinate
from bokeh.plotting import figure, show

def graph(x, y):
    p = figure(title="Random Walk Simulation", x_axis_label='Steps', y_axis_label='Distance')
    p.line(x, y, legend_label="Average Distance")
    show(p)

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
    average_distances_by_walking = []
    for step in distances:
        distances = simulation(step, attempts, walker_class)
        prom = round(sum(distances) / len(distances), 4)
        maximum = max(distances)
        minimum = min(distances)
        average_distances_by_walking.append(prom)
        print(f'{walker_class.__name__} random walk of {step} steps')
        print(f'Average distance: {prom}, Max distance: {maximum}, Min distance: {minimum}\n')

    graph(distances, average_distances_by_walking)

if __name__ == "__main__":
    distances = [10, 100, 1000, 10000]
    attempts = 100

    main(distances, attempts, TraditionalWalker)