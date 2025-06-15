class Camp:
    def __init__(self):
        self.walkers_coordinates = {}

    def add_walker(self, walker, coordinate):
        self.walkers_coordinates[walker] = coordinate

    def move_walker(self, walker):
        dx, dy = walker.walk()
        actual_coordinate = self.walkers_coordinates[walker]
        new_coordinate = actual_coordinate.move(dx, dy)
        self.walkers_coordinates[walker] = new_coordinate

    def get_coordinate(self, walker):
        return self.walkers_coordinates[walker]