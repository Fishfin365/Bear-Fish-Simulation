import turtle
import random
from abc import abstractmethod


class LifeForm(object):
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.world = None
        self.breed_tick = 0

        self.l_turtle = turtle.Turtle()
        self.l_turtle.up()
        self.l_turtle.hideturtle()

    def set_x(self, new_x):
        self.x_pos = new_x

    def set_y(self, new_y):
        self.y_pos = new_y

    def get_x(self):
        return self.x_pos

    def get_y(self):
        return self.y_pos

    def set_world(self, a_world):
        self.world = a_world

    def appear(self):
        self.l_turtle.goto(self.x_pos, self.y_pos)
        self.l_turtle.showturtle()

    def move(self, new_x, new_y):
        self.world.move_life_form(self.x_pos, self.y_pos, new_x, new_y)
        self.set_x(new_x)
        self.set_y(new_y)
        self.l_turtle.goto(self.get_x(), self.get_y())

    def hide(self):
        self.l_turtle.hideturtle()

    def _get_offset_location(self):
        """
        To get a valid location for this Fish to move to.
        :return:
        """
        offset_list = [(-1, 1), (0, 1), (1, 1),
                       (-1, 0), (1, 0),
                       (-1, -1), (0, -1), (1, -1)]

        locations = []  # list of tuples of possible locations for this Fish to move to
        for offset in offset_list:
            pos_x = self.x_pos + offset[0]
            pos_y = self.y_pos + offset[1]
            # We should only select a position inside the world
            if 0 <= pos_x < self.world.get_max_x() and 0 <= pos_y < self.world.get_max_y():
                locations.append((pos_x, pos_y))

        return random.choice(locations)

    def try_to_move(self):
        newLocation = self._get_offset_location()

        # if newLocation is empty, move to that space
        if self.world.empty_location(newLocation[0], newLocation[1]):
            self.move(newLocation[0], newLocation[1])

    def try_to_breed(self):
        valid_location = self._get_offset_location()

        if self.world.empty_location(valid_location[0], valid_location[1]):
            child = LifeForm()
            self.world.add_life_form(child, valid_location[0], valid_location[1])
            self.breed_tick = 0

        # Maybe later we can change this method so that Bear will be able to breed as long as there is an
        # adjacent empty location

    # Users of the module will learn that objects of type LifeForm cannot be created
    # Developers  must override the .live_a_little() abstract method in subclasses
    @abstractmethod
    def live_a_little(self):
        pass
