from material import Material
from simulator import Simulator

iron = Material(0, 1)
iron.__set_name__("iron")

ironBar = Material(0, 15)
ironBar.__set_name__("iron-bar_1")
ironBar.add_material_to_recipe(iron, 5)

ironBar2 = Material(0, 8)
ironBar2.__set_name__("iron-bar_2")
ironBar2.add_material_to_recipe(iron, 5)

ironBolt = Material(0, 10)
ironBolt.__set_name__("iron-bolt")
ironBolt.add_material_to_recipe(ironBar, 2)

copper = Material(0, 2)
copper.__set_name__("copper")

copperBar = Material(0, 8)
copperBar.__set_name__("copper-bar")
copperBar.add_material_to_recipe(copper, 5)

plate = Material(0, 30)
plate.__set_name__("plate")
plate.add_material_to_recipe(ironBolt, 1)
plate.add_material_to_recipe(copperBar, 3)

simulator = Simulator(120, [iron, ironBar, ironBar2, ironBolt, copper, copperBar, plate])
simulator.simulate()
