import './Recipe-style.css'
// import SingleRecipe from './SingleRecipe';

 const Recipes = ({recipes, onRecipeClick}) => {
return (
    <div className='RecipeContainer'>
                 <div className='RecipeContent'>
                     <div className='RecipeContentText'>
                         <div className='RecipeContentTitle'><h2>Recipes</h2></div>
                     </div>
                     {/* {recipes.map((recipe) => (
                         <SingleRecipe key={recipe.id} recipe={recipe} onClick={onRecipeClick} />
                     ))} */}
                 </div> 
         </div>
     )
 };

 export default Recipes;