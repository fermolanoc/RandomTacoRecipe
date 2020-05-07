"""
    Program that creates a workbook with 3 random taco recipes based
    on the recipe info by accessing an API that generates a random recipe each time it is accessed
    Workbook will include a Title with a related Taco image, credits to the image author, the taco API and
    workbook creator --> myself
    Then, 3 recipes will be shown on workbook, each one will have a name which will be composed based on the 5 main
    ingredients that the recipe contains (seasoning, condiment, mixin, base layer and shell).
    Each main ingredient will have its own title, description and detailed recipe info/preparation

    After each recipe document will include a page break to organize the content and show the next recipe
    By running the program it'll generate a Workbook document named RandomTacos.docx which will include 3 different
    taco recipes each time it is ran.
"""

# Pending Tasks:
# - access api and confirm the whole data is accessible by parsed in json format
# - get 5 main ingredients with their recipes
# - create a dictionary to save the whole recipe
# - create the taco recipe name based on the 5 main ingredients
# - create workbook
# - include workbook title, taco image (pending download it and resizing it or getting it by Unsplash API)
# - create a function that calls the API 3 times to get 3 recipes - each time save it in the dictionary and add it to
# the workbook
# - style the whole workbook
# save the document

import requests
import docx

url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'
load_data = requests.get(url).json()

print(load_data)

seasoning_name = load_data['seasoning']['name']
seasoning_recipe = load_data['seasoning']['recipe']

condiment_name = load_data['condiment']['name']
condiment_recipe = load_data['condiment']['recipe']

mixin_name = load_data['mixin']['name']
mixin_recipe = load_data['mixin']['recipe']

base_layer_name = load_data['base_layer']['name']
base_layer_recipe = load_data['base_layer']['recipe']

shell_name = load_data['shell']['name']
shell_recipe = load_data['shell']['recipe']


print(seasoning_name)
print(seasoning_recipe)


