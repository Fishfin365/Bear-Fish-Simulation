from LifeForm import LifeForm


class Fish(LifeForm):
    def __init__(self):
        super().__init__()
        self.l_turtle.shape('Fish.gif')  # must also register the image with the screen object

    def live_a_little(self):
        # First determine if the Fish dies out because of overcrowding
        # If there are two or more adjacent Fish, this Fish is no more
        offsetList = [(-1, 1), (0, 1), (1, 1),
                      (-1, 0), (1, 0),
                      (-1, -1), (0, -1), (1, -1)]

        adjacent_fish = 0  # to count how many Fish are there one location away from this Fish
        for offset in offsetList:
            # Calculate the adjacent location
            new_x = self.x_pos + offset[0]
            new_y = self.y_pos + offset[1]
            # Check that the location is valid
            if 0 <= new_x < self.world.get_max_x() and 0 <= new_y < self.world.get_max_y():
                # Ask the world if the location is empty
                if not self.world.empty_location(new_x, new_y):
                    # If not empty, ask the world what is the object at the location
                    if isinstance(self.world.look_at_location(new_x, new_y), Fish):
                        # If it is a Fish, up the count by one
                        adjacent_fish += 1

        if adjacent_fish >= 3:
            self.world.del_life_form(self)
        else:
            self.breed_tick += 1
            if self.breed_tick >= 2:
                self.try_to_breed()

            self.try_to_move()
