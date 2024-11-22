import random
from LifeForm import LifeForm
from Fish import Fish


class Bear(LifeForm):
    def __init__(self):
        super().__init__()
        self.l_turtle.shape('Bear.gif')  # must also register the image with the screen object
        self.starve_tick = 0

    def try_to_eat(self):
        # First determine if the Fish dies out because of overcrowding
        # If there are two or more adjacent Fish, this Fish is no more
        offset_list = [(-1, 1), (0, 1), (1, 1),
                      (-1, 0), (1, 0),
                      (-1, -1), (0, -1), (1, -1)]

        adjacent_fish = []  # collect all the Fish are there one location away from this Bear
        for offset in offset_list:
            # Calculate the adjacent location
            new_x = self.x_pos + offset[0]
            new_y = self.y_pos + offset[1]
            # Check that the location is valid
            if 0 <= new_x < self.world.get_max_x() and 0 <= new_y < self.world.get_max_y():
                # Ask the world if the location is empty
                if not self.world.empty_location(new_x, new_y):
                    # If not empty, ask the world what is the object at the location
                    if isinstance(self.world.look_at_location(new_x, new_y), Fish):
                        # If it is a Fish, add it to the list of adjacent Fish
                        adjacent_fish.append(self.world.look_at_location(new_x, new_y))

        random.shuffle(adjacent_fish)

        if len(adjacent_fish) > 0:
            self.move(adjacent_fish[0].get_x(), adjacent_fish[0].get_y())
            self.world.del_life_form(adjacent_fish[0])
            self.starve_tick = 0
        else:
            self.starve_tick += 1

    def live_a_little(self):
        # move
        self.try_to_move()

        # eat
        self.try_to_eat()

        # breed
        if self.starve_tick >= 12:
            self.world.del_life_form(self)
        elif self.breed_tick >= 3:
            self.try_to_breed()
