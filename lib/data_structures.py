from statistics import mean 
from functools import reduce 
import numpy

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food.get("name") for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    return [print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶' * food.get('heat_level')}") for food in spicy_foods]

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food.get('cuisine') == cuisine), [{}])

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    # return mean([food['heat_level'] for food in spicy_foods])
    # return sum([[food['heat_level'] for food in spicy_foods]] for food in spicy_foods])/len(spicy_foods)
    # return numpy.average([food['heat_level'] for food in spicy_foods])
    return reduce(lambda acc, food: acc + food['heat_level'], spicy_foods, 0) / len(spicy_foods)
    # Add the 0 as default value or the entire first object will become acc after the first iteration