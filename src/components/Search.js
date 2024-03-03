import './Search-style.css'
import React, { useEffect, useState } from 'react';
import stuff from '../../src/ingredients_data.csv'
import Select from 'react-select';
import {csv} from 'd3'

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
    <div>
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
          }),
          multiValueLabel: (provided) => ({
            ...provided,
            color: ' #d6322c' // Change color of selected option text
          }),
        }}
      />
      <div>
      <h3>Selected Ingredients:</h3>
        <ul>
          {selectedIngredients.map((ingredient, index) => (
            <li key={index}>{ingredient}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

function SearchBar() {
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
                <label htmlFor='difficulty' style={{padding: 10}}>Difficulty</label>
                <select id='difficulty' name='difficulty'>
                    <option value='any'>Any</option>
                    <option value='easy'>Easy</option>
                    <option value='moreEffort'>More Effort</option>
                    <option value='aChallenge'>A challenge</option>
                </select>
                </div>

                <div className='DropdownContainer'>
                <label htmlFor='time' style={{padding: 10}}>Cooking Time</label>
                <select id='time' name='time'>
                    <option value='any'>Any</option>
                    <option value='superQuick'>Under 20 mins</option>
                    <option value='quick'>20-60 mins</option>
                    <option value='medium'>1-2 hrs</option>
                    <option value='long'>2+ hrs</option>
                </select>
                </div>
                </div>
                <DropDown />
                <div className='SearchBar'>
                {/* searchbar */}
                  <input type='text' id='search' name='search' placeholder='Add ingredients' />
                  <button type='button'>Search</button>

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
