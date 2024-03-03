import './Search-style.css'
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import * as Papa from 'papaparse'
import React, { useEffect, useState } from 'react';


function DropDown() {
  // "proxy" : "http://localhost:3000", - had in package.json file 
  const [ text, setText ] = useState();

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData =() => {
    fetch("../../public/ingredients_data.csv")
    .then( response => response.text() )
    .then( responseText => {
        // -- parse csv
        var data = Papa.parse(
          responseText);
        setText(data[0])
       // console.log('data:', data);
    });
  }
 /* const [data, setData] = useState([]);
  useEffect(() => {
    fetch("../data/ingredients_data.csv")
      .then(response => response.json())
      .then(data => {
        setData(data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);
  //const ingredients = fetch('../data/ingredients_data.csv')
  // .then(ingredients => ingredients.text())
   //.then(v => Papa.parse(v))
   //.then(v => console.log(v))
   //.catch(err => console.log(err))
  // const ingredients = (csvFile) => {
  /*  return new Promise((resolve,reject)=> {
          Papa.parse(csvFile, {
            header:false,
            dynamicTyping:false,
            complete:(result) => {
              resolve(result.data);
            },
            error:(error) => {
              reject(error)
            },
          });
      });
   }; */

  //ingredients("../data/ingredients_data.csv").then(v=>console.log(v))
 // console.log(ingredients("../data/ingredients_data.csv"))
 // ingredients.then(v => ingredientsList)
  
  return (
    <> 
    <h1>CSV Data</h1>
    <h2>setText</h2>
    <button onClick={fetchData}>Fetch Data</button>
      {['Ingredients'].map(
        (variant) => (
          <DropdownButton
            as={ButtonGroup}
            key={variant}
            id={`dropdown-variants-${variant}`}
            variant={variant.toLowerCase()}
            title={variant}>
            
            <Dropdown.Item eventKey="1">Action</Dropdown.Item>
            <Dropdown.Item eventKey="2">Another action</Dropdown.Item>
            <Dropdown.Item eventKey="3" active>
              Active Item
            </Dropdown.Item>
            <Dropdown.Divider />
            <Dropdown.Item eventKey="4">Separated link</Dropdown.Item>
          </DropdownButton>
        ),
      )}
    </>
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
                    <option value='easy'>Easy</option>
                    <option value='easy'>Intermediate</option>
                    <option value='hard'>Hard</option>
                </select>
                </div>
          
                <div className='DropdownContainer'>
                <label htmlFor='time' style={{padding: 10}}>Cooking Time</label>
                <select id='time' name='time'>
                    <option value='fast'>Fast</option>
                    <option value='slow'>Slow</option>
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