import React from 'react'
import './Search-style.css'

function Search() {
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

export default Search