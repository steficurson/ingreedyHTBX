import datetime
import time
import warnings
import os
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

warnings.filterwarnings('ignore')


def range_of_numbers(n):
    return list(range(1, n + 1))

def extract_ingredients(pages,sleep_timer):
    def get_urls():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        urls_df = pd.DataFrame(columns=['ingredient_urls'])

        time.sleep(sleep_timer)
        url = f'https://www.bbcgoodfood.com/glossary'
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        ingredient_urls = pd.Series([a.get("href") for a in soup.find_all("a") if a.get("href")])
        
        """ recipe_urls = recipe_urls[(recipe_urls.str.count("-") > 0)
                                      & (recipe_urls.str.contains("/recipes/") == True)
                                      & (recipe_urls.str.contains("category") == False)
                                      & (recipe_urls.str.contains("collection") == False)].unique() """
            
        #Filtering soup results 
        ingredient_urls = ingredient_urls[ (ingredient_urls.str.contains("glossary") == True)
                                    & (ingredient_urls.str.contains("category") == False)
                                    & (ingredient_urls.str.contains("comnan") == False)
                                    & (ingredient_urls.str.contains("https"))].unique()#howto/guide]
      #  print("making " + str(page) + " dataframe")
        df = pd.DataFrame({"ingredient_urls": ingredient_urls})
        urls_df = pd.concat([urls_df, df], ignore_index=True)

       # urls_df['ingredient_urls'] = 'https://www.bbcgoodfood.com' + urls_df['recipe_urls'].astype(str)
       # print("list urls:")
        list_urls = urls_df['ingredient_urls'].to_list() 
     #   for item in list_urls:
      #      print(item)
        return list_urls
    
    def get_ingredients(list_urls):
        print("Getting individual ingredients...")
        names = []
        for url in list_urls:
            try:
                html = requests.get(url)
            except:
                #Invalid URL, skipping
                break
            soup = BeautifulSoup(html.text, 'html.parser')
            try:
                ingredients = soup.find_all('div', {'class':'standard-card-new'})
                for ingredient in ingredients:
                    names.append(ingredient['data-item-name']) 
            except:
                print("na")     
        ingredients_df = pd.DataFrame(names, columns=['Ingredient'])     

        return ingredients_df
   

    urls = get_urls()
    return(get_ingredients(urls))

    #return list_urls, urls_df, recipes_df
def extract_recipes(pages, sleep_timer):
    def get_urls():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        urls_df = pd.DataFrame(columns=['recipe_urls'])

        for page in pages:
            time.sleep(sleep_timer)
            #url = f'https://www.bbcgoodfood.com/search/recipes/page/{page}/'
            recipe_url = f"https://www.bbcgoodfood.com/recipes/"
            #collections = f"https://www.bbcgoodfood.com/search/recipes"
          #  url = f'https://www.bbcgoodfood.com/search/page/{page}'
            html = requests.get(recipe_url)
            soup = BeautifulSoup(html.text, 'html.parser')
            recipe_urls = pd.Series([a.get("href") for a in soup.find_all("a")])
            collection_urls = pd.Series([a.get("href") for a in soup.find_all("a")])
            """ recipe_urls = recipe_urls[(recipe_urls.str.count("-") > 0)
                                      & (recipe_urls.str.contains("/recipes/") == True)
                                      & (recipe_urls.str.contains("category") == False)
                                      & (recipe_urls.str.contains("collection") == False)].unique() """
            
            #Filtering URLs 
            recipe_urls = recipe_urls[(recipe_urls.str.count("-") > 0)
                                      & (recipe_urls.str.contains("recipes/") == True)
                                      & (recipe_urls.str.contains("category") == False)
                                      & (recipe_urls.str.contains("collection") == False)#owto/guide
                                      & (recipe_urls.str.contains("howto") == False)].unique()
            collection_urls = collection_urls[(collection_urls.str.count("-") > 0)
                                      & (collection_urls.str.contains("recipes/") == True)
                                      & (collection_urls.str.contains("category") == False)
                                      & (collection_urls.str.contains("collection") == True)#owto/guide
                                      & (collection_urls.str.contains("https") == True)
                                      & (collection_urls.str.contains("comnan") == False)].unique()
            
            

            print("making " + str(page) + " dataframe")
            df = pd.DataFrame({"recipe_urls": recipe_urls})

            collection_recipes=[]
            for collection_url in collection_urls:
                try:
                    html = requests.get(collection_url)
                except:
                    break
                soup = BeautifulSoup(html.text, 'html.parser')
                thiscollections_urls = pd.Series([a.get("href") for a in soup.find_all("a")])
                thiscollections_urls = thiscollections_urls[(thiscollections_urls.str.count("-") > 0)
                                      & (thiscollections_urls.str.contains("recipes/") == True)
                                      & (thiscollections_urls.str.contains("category") == False)
                                      & (thiscollections_urls.str.contains("collection") == False)
                                      & (thiscollections_urls.str.contains("howto") == False)].unique()
                
                collection_recipes.extend(thiscollections_urls)
            print("all collection recipes ")


            collections_recipes_df = pd.DataFrame(collection_recipes, columns=['recipe_urls'])

            all_urls = pd.concat([collections_recipes_df, df], ignore_index=True)
            urls_df = pd.concat([urls_df, all_urls], ignore_index=True)
            urls_df.drop_duplicates(inplace=True)

          

        urls_df['recipe_urls'] = 'https://www.bbcgoodfood.com' + urls_df['recipe_urls'].astype(str)
        recipes_df = pd.DataFrame(
            columns=['title', 'difficulty', 'serves', 'rating', 'vegetarian', 'vegan', 'dairy_free',
                     'gluten_free', 'prep_time', 'cook_time', 'ingredients'])
        list_urls = urls_df['recipe_urls'].to_list()
        return list_urls, urls_df, recipes_df

    def get_recipes(list_urls, urls_df, recipes_df):
        print("getting ingredients")
        for i in range(len(list_urls)):
            time.sleep(sleep_timer)
            url = list_urls[i]
            try:
                html = requests.get(url)
            except:
                print("invalid url: " + str(url))
                continue
            soup = BeautifulSoup(html.text, 'html.parser')

            try:
                recipe_title = soup.find('h1', {'class': 'heading-1'}).text
                print(recipe_title)
                if(recipe_title.lower().__contains__("how")):
                    continue

            except:
                recipe_title = np.nan
            try:
                difficulty = soup.find_all('div', {'class': 'icon-with-text__children'})[1].text
            except:
                difficulty = np.nan
            try:
                serves = soup.find_all('div', {'class': 'icon-with-text__children'})[2].text
            except:
                serves = np.nan
            try:
                rating = soup.find_all('span', {'class': 'sr-only'})[86].text
            except:
                rating = np.nan
            try:
                prep_time = soup.find('li', {'class': 'body-copy-small list-item'}).text
            except:
                prep_time = np.nan
            try:
                cook_time = soup.find_all('li', {'class': 'body-copy-small list-item'})[1].text
            except:
                cook_time = np.nan
            try:
                categories = soup.find_all('ul', {
                    'class': 'terms-icons-list d-flex post-header__term-icons-list mt-sm hidden-print list list--horizontal'})[
                    0].text
                if 'Vegetarian' in categories:
                    vegetarian = 'True'
                if not 'Vegetarian' in categories:
                    vegetarian = False
                if 'Vegan' in categories:
                    vegan = True
                if not 'Vegan' in categories:
                    vegan = False
                if 'Dairy-free' in categories:
                    dairy_free = True
                if not 'Dairy-free' in categories:
                    dairy_free = False
                if 'Gluten-free' in categories:
                    gluten_free = True
                if not 'Gluten-free' in categories:
                    gluten_free = False
            except:
                vegetarian = False
                vegan = False
                keto = False
                dairy_free = False
                gluten_free = False

            i = 0
            ingredient_list = []
            ingredient = soup.find_all('li', {'class': 'pb-xxs pt-xxs list-item list-item--separator'})
            while i < len(ingredient):
                try:
                    ingredient_string = str(''.join(str(ingredient[i]).split('<!-- -->')[1]))
                    ingredient_string= ingredient_string.replace(",", ";")
                except Exception as e:
                    ingredient_string = str(''.join(ingredient[i].text))
                    ingredient_string = ingredient_string.replace(",", ";")
                    pass
                ingredient_list.append(ingredient_string)
                ingredient_list = [l.replace('</li>', '') for l in ingredient_list]
                i = i + 1

            recipes_df = recipes_df._append(
                {'title': recipe_title, 'difficulty': difficulty, 'serves': serves, 'rating': rating, 'vegetarian': vegetarian, 'vegan': vegan,
                 'dairy_free': dairy_free, 'gluten_free': gluten_free, 'prep_time': prep_time, 'cook_time': cook_time,
                 'ingredient': ingredient_list}, ignore_index=True)

        recipes_df = recipes_df.join(urls_df)

        return recipes_df
    print("get urls")
    list_urls, urls_df, recipes_df = get_urls()
    recipes_df = get_recipes(list_urls, urls_df, recipes_df)
    return recipes_df


if __name__ == '__main__':
    # enter how many pages of recipes you would like to scrape
    pages = range_of_numbers(1)
    # here you can change the amount of time between each request to scrape data
    sleep_timer = 1
   # week = datetime.datetime.now().strftime("%Y-%m-%d")

    print(f'Scraping {pages} pages from BBC good food')
    ingredients_df = extract_ingredients(3,1)
    recipes_df = extract_recipes(pages, sleep_timer)

 #   allFood_df = extract_ingredients()


    if os.path.exists("recipes_data.csv"):
        os.remove("recipes_data.csv")
    
    if os.path.exists("ingredients_data.csv"):
        os.remove("ingredients_data.csv")
    
    ingredients_df.to_csv(f'ingredients_data.csv', index=False)
    recipes_df.to_csv(f'recipes_data.csv', index=False)
    
    print('Complete')
    