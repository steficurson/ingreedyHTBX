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

keywords = ['onion', 'garlic', 'spring onion', 'ginger', 'soy sauce', 'olive oil', 'pork', 'chicken breast', 'chicken thigh', 'ground cumin', 'cumin', 'tomato', 'tomato paste', 'butter', 'tomato ketchup', 'parsley', 'leek', 'pork sausages']

def find_longest_keyword(ingredient):
    # Initialize variables to store the longest matching keyword and its length
    longest_keyword = ""
    longest_length = 0

    # Iterate through each keyword in the 'keywords' array
    for keyword in keywords:
        # Check if the keyword or its plural form is present in the ingredient string
        if keyword in ingredient or p.plural(keyword) in ingredient:
            # If the length of the keyword is greater than the current longest length, update the variables
            if len(keyword) > longest_length:
                longest_keyword = keyword
                longest_length = len(keyword)

    # Return the longest matching keyword
    return longest_keyword


# Load the data
df = pd.read_csv('data/sample-data.csv')
ingredient_list = df["ingredient"].tolist()

for recipe in ingredient_list:
    recipe = recipe.split(',')
    for ingredient in recipe:
        #print(ingredient + "----------->" + str(clean_ingredient(ingredient)))
        print(ingredient + "----------->" + str(find_longest_keyword(ingredient)))
