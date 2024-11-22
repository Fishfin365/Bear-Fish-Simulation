import turtle
import random


class World(object):
    extra_width = 8
    extra_height = 8

    def __init__(self, x, y):
        self.max_x = x
        self.max_y = y
        self.life_forms = []
        self.grid = []

        # Populate the grid with locations
        for row in range(self.max_y):
            row = []
            for col in range(self.max_x):
                row.append(None)
            self.grid.append(row)

        self.w_screen = turtle.Screen()
        self.w_screen.setworldcoordinates(-self.extra_width, -self.extra_height, self.max_x - 1 + self.extra_width,
                                          self.max_y - 1 + self.extra_height)
        self.w_turtle = turtle.Turtle()
        self.w_turtle.speed(0)

        # Register Bear and Fish images(shapes)
        self.w_screen.addshape("Fish.gif")
        self.w_screen.addshape("Bear.gif")

    def freeze_world(self):
        self.w_screen.exitonclick()

    def draw(self):
        self.w_screen.tracer(0, 0)
        # This method is to actually draw the grid on the screen
        self.w_turtle.forward(self.max_x - 1)
        self.w_turtle.left(90)
        self.w_turtle.forward(self.max_y - 1)
        self.w_turtle.left(90)
        self.w_turtle.forward(self.max_x - 1)
        self.w_turtle.left(90)
        self.w_turtle.forward(self.max_y - 1)
        self.w_turtle.left(90)
        for i in range(self.max_y - 1):
            self.w_turtle.forward(self.max_x - 1)
            self.w_turtle.backward(self.max_x - 1)
            self.w_turtle.left(90)
            self.w_turtle.forward(1)
            self.w_turtle.right(90)

        self.w_turtle.forward(1)
        self.w_turtle.right(90)

        for i in range(self.max_x - 2):
            self.w_turtle.forward(self.max_y - 1)
            self.w_turtle.backward(self.max_y - 1)
            self.w_turtle.left(90)
            self.w_turtle.forward(1)
            self.w_turtle.right(90)

        self.w_screen.tracer(1, 0)

    def get_max_x(self):
        return self.max_x

    def get_max_y(self):
        return self.max_y

    def get_life_forms(self):
        return self.life_forms

    def add_life_form(self, life_form, x, y):
        life_form.set_x(x)  # strange? -> we are assuming that there is an object lifeForm with a method setX()
        life_form.set_y(y)
        self.grid[y][x] = life_form
        life_form.set_world(self)
        self.life_forms.append(life_form)
        life_form.appear()

    def del_life_form(self, life_form):
        life_form.hide()
        self.grid[life_form.get_y()][life_form.get_x()] = None
        self.life_forms.remove(life_form)

    def empty_location(self, x, y):
        if self.grid[y][x] is None:
            return True
        else:
            return False

    def look_at_location(self, x, y):
        return self.grid[y][x]

    def move_life_form(self, oldx, oldy, newx, newy):
        self.grid[newy][newx] = self.grid[oldy][oldx]
        self.grid[oldy][oldx] = None

    def live_a_little(self):
        if self.life_forms:
            randomLifeForm = random.choice(self.life_forms)
            randomLifeForm.live_a_little()  # life-form will take its turn


def main():
    from Fish import Fish
    test_world = World(10, 10)

    test_world.draw()

    # Add a single fish to the world
    fish1 = Fish()
    test_world.add_life_form(fish1, 9, 9)

    test_world.freeze_world()


if __name__ == "__main__":
    main()
