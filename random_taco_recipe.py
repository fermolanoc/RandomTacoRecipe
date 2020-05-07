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
