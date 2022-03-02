import math


class Simulator:
    def __init__(self, time, snapshot, boosters=None):
        if boosters is None:
            boosters = []
        self.total_time = time
        self.materials = snapshot
        self.boosters = boosters

    def simulate(self):
        for t in range(self.total_time):
            print(t, end='\t')
            for material in self.materials:
                print("{0:.2f}".format(material.initial_amount), end='\t')
                #         add boosters later

                has_all_required_materials = {}
                for ingredient in material.ingredients.keys():
                    required = material.ingredients[ingredient]
                    owns = 0
                    for material1 in self.materials:
                        key = ingredient.split("_")[0]
                        if material1.name.split("_")[0] == key:
                            owns += math.floor(material1.initial_amount)

                    has_req_mat = self.H(owns - required)
                    has_all_required_materials[ingredient] = has_req_mat

                has_all_materials = 1
                material_already_started = 0

                if len(material.ingredients) > 0:
                    if 0.0001 < material.initial_amount % 1 < 0.9999:
                        material_already_started = 1

                    if material.should_start == 0:
                        material.start_production_time += 1
                        if material.start_production_time >= material.production_time:
                            material.start_production_time = 0
                            material.should_start = 1

                    for req in material.ingredients.keys():
                        has_all_materials *= has_all_required_materials[req]

                    material_continue_work = material.should_start ^ 1 | material_already_started | has_all_materials
                else:
                    material_continue_work = 1

                if material.production_time != -1:
                    produced = material_continue_work / material.production_time
                    material.initial_amount += produced

                a = (has_all_materials & material_already_started) ^ 1
                for req in material.ingredients.keys():
                    a *= has_all_required_materials[req]

                for req in material.ingredients.keys():
                    if material.production_time != -1:
                        used = a * material.ingredients[req]
                        if used > 0:
                            for material1 in self.materials:
                                key = req.split("_")[0]
                                if material1.name.split("_")[0] == key:
                                    floor = int(material1.initial_amount)
                                    material1.initial_amount -= min(used, floor)
                                    used -= min(used, floor)
                                    if used <= 0:
                                        break

                material.should_start *= (has_all_materials & material_already_started) ^ 1

            print()

        print(self.total_time, end='\t')
        for material in self.materials:
            print("{0:.2f}".format(material.initial_amount), end='\t')

    def H(self, value):
        if value >= 0:
            return 1
        else:
            return 0
