from material import Material
from simulator import Simulator


def main():
    iron = Material(0, 1)
    iron.__set_name__("iron")

    iron_bar = Material(0, 15)
    iron_bar.__set_name__("iron-bar_1")
    iron_bar.add_material_to_recipe(iron, 5)

    iron_bar2 = Material(0, 8)
    iron_bar2.__set_name__("iron-bar_2")
    iron_bar2.add_material_to_recipe(iron, 5)

    iron_bolt = Material(0, 10)
    iron_bolt.__set_name__("iron-bolt")
    iron_bolt.add_material_to_recipe(iron_bar, 2)

    copper = Material(0, 2)
    copper.__set_name__("copper")

    copper_bar = Material(0, 8)
    copper_bar.__set_name__("copper-bar")
    copper_bar.add_material_to_recipe(copper, 5)

    plate = Material(0, 30)
    plate.__set_name__("plate")
    plate.add_material_to_recipe(iron_bolt, 1)
    plate.add_material_to_recipe(copper_bar, 3)

    simulator = Simulator(120, [iron, iron_bar, iron_bar2, iron_bolt, copper, copper_bar, plate])
    simulator.simulate()


if __name__ == "__main__":
    main()
