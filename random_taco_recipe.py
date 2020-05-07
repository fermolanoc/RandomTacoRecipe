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
# - create the taco recipe name based on the 5 main ingredients
# - style the whole workbook
# save the document
import os
import requests
import docx
from docx.enum.text import WD_BREAK
from PIL import Image, ImageDraw, ImageFont
import urllib.request
from docx.shared import Inches

# Access API and get data in json format
# url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'
# random_recipes_data = requests.get(url).json()

# print(random_recipes_data['mixin']['recipe'])

# # 5 main ingredients needed
ingredients = ['seasoning', 'condiment', 'mixin', 'base_layer', 'shell']

# Get 5 main ingredients example
# seasoning_name = random_recipes_data['seasoning']['name']
# seasoning_recipe = random_recipes_data['seasoning']['recipe']
#
# condiment_name = random_recipes_data['condiment']['name']
# condiment_recipe = random_recipes_data['condiment']['recipe']

# print(seasoning_name)
# print(seasoning_recipe)


# Getting image Full Size from Unsplash API
# Developer Credentials
# Unsplash API to get images
api_url = 'https://api.unsplash.com/photos/random/'

# Access key
key = os.environ.get('IMAGE_KEY')

# Params to parse on the search
query = 'taco,tacos'

# get JSON data and convert it to Python dictionary by sending the api url, access key and search query on the request
image_data = api_url + '?query=' + query + '&client_id=' + key
random_image = requests.get(image_data).json()

# Get the full size image version
random_image_url = random_image['urls']['full']
# Save full size image into project folder
urllib.request.urlretrieve(random_image_url, 'random_taco.png')

# Resizing Image with Unsplash API -> dpr = Device Pixel Ratio -> Controls the density of the image, which means
# image density varies depending on the user's device so highest quality always will be shown depending on which quality
# level user's device can support -> min value is 1, max is 8 (3 is good enough and doesn't consume much bandwidth)
resized_image = random_image_url + '&w=600&dpr=3'
# Save resized image into project folder
urllib.request.urlretrieve(resized_image, 'random_taco_600x600.png')

"""
    Another method to resized image manually is shown below
    I decided to go with the Unsplash API method above just because is faster, requires less code and
    final result has same great quality but both methods have been tested.
"""
# # Resizing image manually
# image = Image.open('random_taco.png')
# # RESIZING IMAGE
# # Getting original width and height
# width = image.width
# height = image.height
# print(width, height)
# percentage_to_reduce = float((800 * 100) / width)
# print(percentage_to_reduce)
#
# height_resize = int(height * (percentage_to_reduce/100))
# # width will be reduced by 14% too to keep contrast
# width_resize = int(width * (percentage_to_reduce/100))
#
# # Resize image keeping contrast
# resized_image_manually = image.resize((width_resize, height_resize))
# # print(image_resized.width, image_resized.height)
# resized_image_manually.show()
# # Save changes over image and include new width and height on file name with png format for better quality
# resized_image_manually.save(f'random_taco_{width_resize}x{height_resize}_manually.png')

# Create Workbook
document = docx.Document()

# First Page includes Title, Image and Credits
# Title
document_title = 'Random Taco Cookbook'
document.add_paragraph(document_title.upper(), 'Title')

# Including image in Workbook
document.add_picture('random_taco_600x600.png', height=docx.shared.Inches(6.25))

# Add Credits
# Heading
credits_heading = 'Credits'
document.add_heading(credits_heading)

# Credits List
credit_p = document.add_paragraph
photo_author = random_image['user']['name']
credit_p(f'Taco image: Photo by {photo_author} on Unsplash', style='List Bullet')

# Random Taco Recipes's API URL
recipes_url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'
credit_p(f'Tacos from: {recipes_url}', style='List Bullet')
credit_p('Code by: Fernando Molano', style='List Bullet')

document.add_page_break()
paragraph = document.add_paragraph()


def create_recipe(url):
    random_recipes_data = requests.get(url).json()
    custom_recipe_title = ''
    for ingredient in ingredients:
        ingredient_title = random_recipes_data[f'{ingredient}']['name']
        document.add_heading(ingredient_title)
        ingredient_recipe = random_recipes_data[f'{ingredient}']['recipe']
        document.add_paragraph(ingredient_recipe)
        custom_recipe_title = custom_recipe_title + ingredient
    prior_paragraph = paragraph.insert_paragraph_before(custom_recipe_title)


for i in range(3):
    create_recipe('https://taco-1150.herokuapp.com/random/?full_taco=true')
    if i != 2:
        document.add_page_break()
    else:
        break

document.save('Random_Taco_Recipes.docx')
