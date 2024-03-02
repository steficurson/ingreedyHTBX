import pandas as pd
import numpy as np
import inflect
p = inflect.engine()

# ----- code for method 1 -----

preceeding_words = ['tsp', 'tbsp', 'tsps', 'tbsps', 'large', 'small', 'medium', 'ml', 'carton', 'x', 'about', 'can', 'cans', 'aprx', 'about', 'around', 'pack', 'packs', 'slices', 'cloves', 'boneless', 'shredded', 'fresh', 'cooked', 'bunch', 'bunches']

def is_measurement(word):
    for letter in word:
        if letter.isdigit():
            return True
    return False

def clean_ingredient(ingredient):
    ingredient = ingredient.lower()
    ingredient_words = ingredient.split(' ')
    ingredient_list = []
    if 'of' in ingredient_words:
        ingredient_words = ingredient_words[ingredient_words.index('of') + 1:]

    for i in range(0, len(ingredient_words)):
        word = ingredient_words[i]
        if word not in preceeding_words:
            if not is_measurement(word):
                ingredient_list.append(''.join([c for c in word if c.isalpha()]))

    return ' '.join(ingredient_list)

# ----- code for method 2 -----

keywords = ['onion', 'garlic', 'spring onion', 'ginger', 'soy sauce', 'olive oil', 'pork', 'chicken breast', 'chicken thigh',
    'ground cumin', 'cumin', 'tomato', 'tomato paste', 'butter', 'tomato ketchup', 'parsley', 'leek', 'pork sausages', 'beef',
    'salt', 'water', 'sugar', 'flour', 'butter', 'onion', 'garlic', 'olive oil', 'egg', 'milk', 'chopped tomatoes', 'chicken stock',
    'pepper', 'vanilla extract', 'baking powder', 'lemon juice', 'chicken', 'tomato', 'cream', 'cheese', 'chocolate', 'rice',
    'baking soda', 'vinegar', 'honey', 'cinnamon', 'bell pepper', 'carrot', 'parsley', 'lemon zest', 'lime juice', 'yogurt', 'curry paste',
    'ginger', 'nutmeg', 'brown sugar', 'basil', 'oregano', 'thyme', 'rosemary', 'cumin', 'coriander', 'cayenne pepper', 'paprika',
    'mustard', 'turmeric', 'garlic powder', 'onion powder', 'black pepper', 'white pepper', 'red pepper flakes', 'chili powder', 'dill', 'red chilli',
    'bay leaf', 'celery', 'potato', 'haddock' 'bell pepper', 'spinach', 'mushroom', 'zucchini', 'squash', 'sweet potato', 'corn', 'peas', 'garam masala'
    'green beans', 'asparagus', 'broccoli', 'cauliflower', 'avocado', 'lettuce', 'cabbage', 'kale', 'radish', 'beet', 'eggplant', 'chilli powder',
    'cucumber', 'tomato paste', 'tomato sauce', 'tomato puree', 'tomato', 'chopped tomato', 'coconut milk', 'coconut oil', 'coconut flakes', 'almond', 'walnut', 'pecan',
    'cashew', 'peanut', 'pistachio', 'macadamia nut', 'pine nut', 'sunflower seed', 'sesame seed', 'flaxseed', 'chia seed', 'poppy seed',
    'quinoa', 'barley', 'oats', 'bulgur', 'couscous', 'brown rice', 'white rice', 'wild rice', 'spaghetti', 'penne', 'fettuccine',
    'lasagna noodles', 'macaroni', 'gnocchi', 'ramen noodles', 'soba noodles', 'udon noodles', 'rice noodles', 'cannellini beans', 'black beans',
    'pinto beans', 'tomato purée', 'kidney beans', 'chickpeas', 'lentils', 'green lentils', 'red lentils', 'split peas', 'black-eyed peas', 'chili beans',
    'green peas', 'peanut butter', 'jam', 'jelly', 'crème fraîche', 'sour cream', 'yogurt', 'mascarpone', 'ricotta', 'cottage cheese', 'chives',
    'vanilla', 'curry powder', 'feta cheese', 'puff pastry', 'salmon', 'tuna', 'white wine', 'sage', 'vegetable oil']

# Matches the ingredient in a recipe to one in the predefined list of ingredients
# Finds longest match
def find_ingredient(ingredient):
    longest_keyword = None
    max_length = 0
    for keyword in keywords:
        if keyword in ingredient or p.plural(keyword) in ingredient:
            if len(keyword) > max_length:
                longest_keyword = keyword
                max_length = len(keyword)
    return longest_keyword

#Loads the scraped data and parses the ingredients
def generate_clean_csv():
    # Load the data
    recipe_data = pd.read_csv('data/sample-data.csv')
    recipe_data.dropna(subset=['ingredient'], inplace=True)

    for index, recipe in recipe_data.iterrows():
        ingredient_data = recipe['ingredient'].split(',')
        cleaned_ingredients = []
        for ingredient in ingredient_data:
            matched_ingredient = find_ingredient(ingredient)
            if matched_ingredient:
                cleaned_ingredients.append(matched_ingredient)
        #Replace the ingredient list with the cleaned one - convert to set to remove duplicates
        recipe_data.loc[index, 'ingredient'] = ','.join(set(cleaned_ingredients))
    recipe_data.to_csv('data/cleaned-recipes.csv')

#Matches the search terms to the ingredients in the recipes
def match_search_terms(search_terms):
    recipe_data = pd.read_csv('data/cleaned-recipes.csv')
    recipe_data.dropna(subset=['ingredient'], inplace=True)
    recipe_data["nr_matches"] = ""
    recipe_data["matched_ingredients"] = ""
    for index, recipe in recipe_data.iterrows():
        ingredients = recipe['ingredient'].split(",")
        matched_ingredients = []
        nr_matches = 0
        for ingredient in ingredients:
            #Increment nr of matches if ingredient is in search terms
            if ingredient in search_terms:
                nr_matches += 1
                matched_ingredients.append(ingredient)
        #Adds the number of matches and the matched ingredients to the dataframe
        recipe_data.loc[index, 'nr_matches'] = nr_matches
        recipe_data.loc[index, 'matched_ingredients'] = ','.join(matched_ingredients)
    recipe_data.sort_values(by=['nr_matches'], ascending=False, inplace=True)


#generate_clean_csv()
print("loaded data!")
match_search_terms(['onion', 'potato', 'garlic', 'tomato', 'pork sausages', 'tomato paste', 'tomato purée'])

