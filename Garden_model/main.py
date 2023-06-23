import random
from typing import List, Dict

import matplotlib.pyplot as plt

# Define the different types of plants you want to model
plants = {
    "carrots": {"germination_time": 10, "growth_rate": 13, "harvest_time": 60},
    "tomatoes": {"germination_time": 7, "growth_rate": 10, "harvest_time": 90},
    "lettuce": {"germination_time": 5, "growth_rate": 7, "harvest_time": 30}
}

# Define the garden data structure
garden = []

# Fill the garden with empty squares
for i in range(3):
    row = []
    for j in range(10):
        value = random.randint(1,3)
        if value == 1:
            row.append({"plant": "carrots", "growth_stage": 0, "soil_type": "clay", "water_level": 0, "weed": False, "disease": False})
        elif value == 2:
            row.append({"plant": "tomatoes", "growth_stage": 0, "soil_type": "clay", "water_level": 0, "weed": False, "disease": False})
        elif value == 3:
            row.append({"plant": "lettuce", "growth_stage": 0, "soil_type": "clay", "water_level": 0, "weed": False, "disease": False})
    garden.append(row)


# Define the simulation functions
def simulate_weather():
    # Update the water level in each square of the garden based on rainfall
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            garden[i][j]["water_level"] += random.randint(0, 10)

def simulate_pests():
    # Simulate pests by setting the weed flag to True in some squares
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if random.random() < 0.1:
                garden[i][j]["weed"] = True

def simulate_disease():
    # Simulate disease by setting the disease flag to True in some squares
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if random.random() < 0.05:
                garden[i][j]["disease"] = True

def simulate_growth():
    # Simulate the growth of the plants in the garden
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if garden[i][j]["plant"] is not None:
                plant = plants[garden[i][j]["plant"]]
            if garden[i][j]["weed"] or garden[i][j]["disease"]:
                # If the plant is affected by weeds or disease, reduce its growth rate
                growth_rate = plant["growth_rate"] / 2
            else:
                growth_rate = plant["growth_rate"]
            garden[i][j]["growth_stage"] += growth_rate
            if garden[i][j]["growth_stage"] >= plant["harvest_time"]:
                # If the plant is ready to be harvested, remove it from the garden
                garden[i][j]["plant"] = None
def plot_growth():
    # Plot the growth rate of each plant in the garden over time
    for plant_type in plants:
        growth_rate = []
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if garden[i][j]["plant"] is None and garden[i][j]["type"] != plant_type:
                growth_rate.append(plants["growth_rate"])
    plt.plot(growth_rate, label=plant_type)
    plt.legend()
    plt.show()
simulate_weather()
simulate_pests()
simulate_disease()
simulate_growth()
plot_growth()