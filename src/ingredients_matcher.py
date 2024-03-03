import pandas as pd
import inflect
import re
import sys
p = inflect.engine()

ROOT_PATH = '../public/data/'
NR_RESULTS = 20
keywords = pd.read_csv(ROOT_PATH + 'ingredients_data.csv')['Ingredient'].tolist()

# Matches the ingredient in a recipe to one in the predefined list of ingredients
# Finds longest match
def find_ingredient(ingredient):
    longest_keyword = None
    max_length = 0
    for keyword in keywords:
        if keyword.lower() in ingredient or p.plural(keyword) in ingredient:
            if len(keyword) > max_length:
                longest_keyword = keyword
                max_length = len(keyword)
    return longest_keyword

#Loads the scraped data and parses the ingredients
def generate_clean_csv():
    # Load the data
    recipe_data = pd.read_csv(ROOT_PATH + 'recipes_data.csv')
    recipe_data.dropna(subset=['ingredient'], inplace=True)

    for index, recipe in recipe_data.iterrows():
        ingredient_data = recipe['ingredient'].split(',')
        cleaned_ingredients = []
        for ingredient in ingredient_data:
            ingredient = re.sub(";[^;]*$", "", ingredient) #remove everything after ;
            matched_ingredient = find_ingredient(ingredient)
            if matched_ingredient:
                cleaned_ingredients.append(matched_ingredient)
        #Replace the ingredient list with the cleaned one - convert to set to remove duplicates
        recipe_data.loc[index, 'ingredient'] = ','.join(set(cleaned_ingredients))
    recipe_data.to_csv(ROOT_PATH + 'cleaned-recipes.csv')

#Matches the search terms to the ingredients in the recipes
def match_search_terms(search_terms):
    recipe_data = pd.read_csv(ROOT_PATH + 'cleaned-recipes.csv')
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
    return recipe_data.head(NR_RESULTS)


#generate_clean_csv()
print("loaded data!")
results = match_search_terms(['Thai curry paste', 'Egg'])
print(results)
