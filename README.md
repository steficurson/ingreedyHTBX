## Inspiration
We wanted to create a solution to an everyday problem and realised a problem that all of us had encountered. We've all had leftover ingredients in the fridge that we just don't know how to use. In many cases, these ingredients will just stay there, sad and unused in our fridges and cupboards, until they eventually get thrown out! This creates unnecessary food waste and is a waste of money.
Ingreedy minimises wastage by helping users find recipes that use the ingredients they already have.

## What it does
Users can input the ingredients they want to use in their recipe. They can also filter recipes based on meal type, skill level, and cooking time. Ingreedy will then display the recipes which match the most ingredients and filters in the search term.

## How we built it
We used React.js to create the main web application.
Using our Beautiful Soup scraper, we got the recipes and the list of all ingredients from BBC GoodFood.
Python scripts were used in the backend to extract the ingredients from the recipes, and then to match these to the user's searches.
Kate led front-end development, Anna wrote the web scraper and Stefi wrote the Python scripts.

## Challenges we ran into
Connecting front-end and back-end. We wrote the front-end in React and created back-end scripts in Python, but we had difficulties connecting these such that the form inputs would be passed into the Python function. We tried using Django and Flask, and library Pyodide for this but nothing worked in the end. Therefore, we have a frontend and a backend but no bridge between them :(

## Accomplishments that we're proud of
Web scraper: we weren't very familiar with Beautiful Soup beforehand so we feel proud that we managed to scrape from BBC GoodFood and get this data into a format where we could match it to user inputs.

## What we learned
We all learned a lot about React, and about Python web libraries like Django and Flask. We also learned about web scraping with Beautiful Soup

## What's next for Ingreedy
Integrate the frontend and backend successfully.
Add support for filtering by dietary requirements. We have scraped this data from BBC GoodFood, so we will just add another multi-select which will filter the user's search results.
