import React from 'react';
// import { useState } from 'react';
import '../App.css'
import Welcome from '../components/Welcome';
import Search from '../components/Search';
import Recipes from '../components/Recipes';
import Footer from '../components/Footer'
// import { recipesData } from './yourData';


function Home() {
    // const [selectedRecipe, setSelectedRecipe] = useState(null);

    // const handleRecipeClick = (recipe) => {
    //   setSelectedRecipe(recipe);
    // };
    return (
        <div>
        <Welcome/>
        <Search/>
        <Recipes />
            {/* {selectedRecipe ? (
            <div>
            <h2>{selectedRecipe.title}</h2>
           
            </div>
        ) : (
            <Recipes recipes={recipesData} onRecipeClick={handleRecipeClick} />
        )} */}
        <Footer/>
        </div>
    );
}

export default Home;