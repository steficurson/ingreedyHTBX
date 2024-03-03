import './Search-style.css'
import React, { useEffect, useState } from 'react';
import stuff from '../../src/ingredients_data.csv'
import Select from 'react-select'; 
import {csv} from 'd3'
import PyodidePythonHelper from "./RecipeBuilder"

const selected_ingredients = []

let pyodide;

function onPyodideLoaded() {
    pyodide = window.pyodide;
    console.log('Pyodide is loaded');
}

function DropDown() {

  const [ingredients, setIngredients] = useState([]);
  const [selectedIngredients, setSelectedIngredients] = useState([]);

  useEffect(() => {
    // Fetch CSV data and parse it
    csv(stuff).then(response => {
      setIngredients(response); // Assuming response is an array of ingredients
    });
  }, []); // Empty dependency array ensures useEffect runs only once
  
  const options = ingredients.map(ingredient => ({
    value: ingredient.Ingredient,
    label: ingredient.Ingredient
  }));

  const handleSelectChange = selectedOptions => {
    // Extract the selected ingredient names from selectedOptions
    const selectedIngredientNames = selectedOptions.map(option => option.value);

    setSelectedIngredients(selectedIngredientNames);
  };

  

  return (
    <div className='hi'>
      <h2>Select Ingredients:</h2>
      <Select
        options={options}
        isMulti
        onChange={handleSelectChange}
        styles={{
          option: (provided, state) => ({
            ...provided,
            color: state.isSelected ? 'white' : 'black', // Change color based on selection
            backgroundColor: state.isSelected ? ' #d6322c' : 'white', // Change background color based on selection
            width: 100,
            padding:10
          }),
          multiValueLabel: (provided) => ({
            ...provided,
            color: ' #d6322c' // Change color of selected option text
          }),
        }}
      />
      <div className='plz'>
      <h2>Selected Ingredients:</h2>
        <ul>
          {selectedIngredients.map((ingredient, index) => (
            selected_ingredients.push({ingredient}),
            <li key={index}>{ingredient}</li>
          ))}
        </ul>
        {/* <MatchRecipes></MatchRecipes> */}
      </div>
    </div>
  );
}

// function MatchRecipes(){
//   const [text, setText] = useState([]);

//   useEffect(() => {
//     // Fetch CSV data and parse it
//     builder(ingredients).then(response => {
//       setIngredients(response); // Assuming response is an array of ingredients
//     });
//   }, []); // Empty dependency array ensures useEffect runs only once
  
//   const handleSelectChange = allRecipes => {
//     // Extract the selected ingredient names from selectedOptions
//     const recipes = allRecipes.map(option => option.value);
//     setSelectedIngredients(selectedIngredientNames);
//   };

//   return(
//     <div>
//       <h1>Recipes</h1>
//     </div>
//   )
// }


function SearchBar() {
  //Took out, dont think its working 
  const [showResult, setShowResult] = useState(false);
  const handleSearchClick = () => {
    setShowResult(true);
  };
  return (
    <div className='SearchContainer'>
        <div className='SearchContent'>
                <div className='SearchContextText'>
                <div className='SearchContentTitle'>
                  <h2>What can I make?</h2>
                </div>
                
                {/* buttons */}
                <div className='SearchTitleButtons'>
                <div className='DropdownContainer'>
                <label htmlFor='difficulty' style={{padding: 10, fontSize: 25}}>Difficulty</label>
                <select id='difficulty' name='difficulty'>
                    <option value='easy'>Easy</option>
                    <option value='easy'>Intermediate</option>
                    <option value='hard'>Hard</option>
                </select>
                </div>
          
                <div className='DropdownContainer'>
                <label htmlFor='time' style={{padding: 10, fontSize: 25}}>Cooking Time</label>
                <select id='time' name='time'>
                    <option value='fast'>Fast</option>
                    <option value='slow'>Slow</option>
                </select>
                </div>
                </div>
                <DropDown />
                <div className='SearchBar'>
                
                <button type='button' onClick={handleSearchClick}>Search</button>
                {showResult && <PyodidePythonHelper selectedIngredients={selected_ingredients} />}
                </div>
                </div>
        </div> 
    </div>
  )
}



export default function Search(){
   return(
    <div>
      <SearchBar />
    </div>

)
}