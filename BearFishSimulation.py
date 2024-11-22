import random
from World import World
from Fish import Fish
from Bear import Bear


def predator_prey_sim(width: int, height: int, num_fish: int, num_bears: int, turns: int):
    # create a world
    my_world = World(width, height)
    my_world.draw()

    my_world.w_screen.tracer(0, 0)

    # create a random collection of locations in the world
    locations = []
    for i in range(my_world.get_max_x()):
        for j in range(my_world.get_max_y()):
            locations.append((i, j))

    random.shuffle(locations)

    # Fish
    for i in range(num_fish):
        newFish = Fish()
        loc = locations.pop()  # removes the last element from the locations list
        my_world.add_life_form(newFish, loc[0], loc[1])

    # Bear
    for i in range(num_bears):
        newBear = Bear()
        loc = locations.pop()
        my_world.add_life_form(newBear, loc[0], loc[1])

    my_world.w_screen.tracer(1, 0)

    # Run the simulation
    for i in range(turns):
        my_world.live_a_little()

    fish, bears = count_lifeforms(my_world)
    print(fish, bears)
    my_world.freeze_world()


def count_lifeforms(my_world):
    num_fish = 0
    num_bear = 0
    for lifeForm in my_world.life_forms:
        if isinstance(lifeForm, Fish):
            num_fish += 1
        if isinstance(lifeForm, Bear):
            num_bear += 1

    return num_fish, num_bear


def main():
    predator_prey_sim(20, 20, 100, 10, 10000)


if __name__ == "__main__":
    main()

