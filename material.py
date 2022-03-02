class Material:
    def __init__(self, initial_amount, production_time):
        self.initial_amount = initial_amount
        self.production_time = production_time
        self.ingredients = {}
        self.should_start = 1
        self.start_production_time = 0

    def __set_name__(self, name):
        self.name = name

    def add_material_to_recipe(self, material, amount):
        self.ingredients[material.name.split("_")[0]] = amount
