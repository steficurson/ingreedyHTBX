import pandas as pd
import numpy as np
import inflect
p = inflect.engine()

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
    'pinto beans', 'kidney beans', 'chickpeas', 'lentils', 'green lentils', 'red lentils', 'split peas', 'black-eyed peas', 'chili beans',
    'green peas', 'peanut butter', 'jam', 'jelly', 'crème fraîche', 'sour cream', 'yogurt', 'mascarpone', 'ricotta', 'cottage cheese', 'chives',
    'vanilla', 'curry powder', 'feta cheese', 'puff pastry', 'salmon', 'tuna', 'white wine', 'sage', 'vegetable oil']

def find_longest_keyword(ingredient):
    # Initialize variables to store the longest matching keyword and its length
    longest_keyword = ""
    max_length = 0

    # Iterate through each keyword in the 'keywords' array
    for keyword in keywords:
        # Check if the keyword or its plural form is present in the ingredient string
        if keyword in ingredient or p.plural(keyword) in ingredient:
            # If the length of the keyword is greater than the current longest length, update the variables
            if len(keyword) > max_length:
                longest_keyword = keyword
                max_length = len(keyword)

    # Return the longest matching keyword
    return longest_keyword


# Load the data
recipe_data = pd.read_csv('data/sample-data.csv')
all_recipes_cleaned_ingredients= dict.fromkeys(recipe_data["title"].tolist())

for recipe in recipe_data:
    ingredient_data = recipe_data[recipe]
    recipe = recipe.split(',')
    cleaned_ingredients = []
    for ingredient in recipe:
        matched_ingredient = find_longest_keyword(ingredient)
        cleaned_ingredients.append(matched_ingredient)

#print(cleaned_ingredient_list)

