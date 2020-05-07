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
from docx.enum.text import WD_BREAK
from docx import Document

# Access API and get data in json format
url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'
random_recipes_data = requests.get(url).json()

# print(random_recipes_data['mixin']['recipe'])

# # 5 main ingredients needed
ingredients = ['seasoning', 'condiment', 'mixin', 'base_layer', 'shell']


# Get 5 main ingredients
seasoning_name = random_recipes_data['seasoning']['name']
seasoning_recipe = random_recipes_data['seasoning']['recipe']

condiment_name = random_recipes_data['condiment']['name']
condiment_recipe = random_recipes_data['condiment']['recipe']

mixin_name = random_recipes_data['mixin']['name']
mixin_recipe = random_recipes_data['mixin']['recipe']

base_layer_name = random_recipes_data['base_layer']['name']
base_layer_recipe = random_recipes_data['base_layer']['recipe']

shell_name = random_recipes_data['shell']['name']
shell_recipe = random_recipes_data['shell']['recipe']

# print(seasoning_name)
# print(seasoning_recipe)


# Create Workbook
document = docx.Document()

document_title = 'Random Taco Cookbook'
document.add_paragraph(document_title.upper(), 'Title')
document.paragraphs[0].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)

for ingredient in ingredients:
    ingredient_title = random_recipes_data[f'{ingredient}']['name']
    document.add_heading(ingredient_title)
    ingredient_recipe = random_recipes_data[f'{ingredient}']['recipe']
    document.add_paragraph(ingredient_recipe)
document.add_page_break()

document.save('Random_Taco_Recipes.docx')