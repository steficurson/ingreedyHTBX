import './Recipe-style.css'
// import SingleRecipe from './SingleRecipe';

const Recipes = ({recipes, onRecipeClick}) => {
    return (
        <div className='RecipeContainer'>
            <div className='RecipeContent'>
                <div className='RecipeContentText'>
                    <div className='RecipeContentTitle'><h2>Recipes</h2></div>
                    <div className='RecipeShow'>
                        <h2>Kimchi Fried Rice  <a href="https://www.bbcgoodfood.com/recipes/kimchi-fried-rice" target="_blank"><i className="fa fa-external-link" style={{ fontSize: '18px', color: 'brown' }}></i></a></h2>
                        <p>Cook time: 20 mins</p>
                        <p>Difficulty: Easy</p>
                        <p>Ingredients: <strong><u>rice</u></strong>, <strong><u>kimchi</u></strong>, <strong><u>egg</u></strong>, garlic, ginger, carrot, spring onion, lime</p>
                    </div>
                    <div className='RecipeShow'>
                        <h2>Kimchi Pancake (Kimchi Jeon) <a href="https://www.bbcgoodfood.com/recipes/spicy-kimchi-pancake-kimchi-jeon" target="_blank"><i className="fa fa-external-link" style={{ fontSize: '18px', color: 'brown' }}></i></a></h2>
                        <p>Cook time: 20 mins</p>
                        <p>Difficulty: Easy</p>
                        <p>Ingredients: <strong><u>rice</u></strong>, <strong><u>kimchi</u></strong>, gochujang, cornflour, self-raising flour</p>
                    </div>
                    <div className='RecipeShow'>
                        <h2>Kimchi Sesame Udon Noodles <a href="https://www.bbcgoodfood.com/recipes/kimchi-sesame-udon-noodles" target="_blank"><i className="fa fa-external-link" style={{ fontSize: '18px', color: 'brown' }}></i></a></h2>
                        <p>Cook time: 15 mins</p>
                        <p>Difficulty: Easy</p>
                        <p>Ingredients: <strong><u>kimchi</u></strong>, <strong><u>egg</u></strong>, spring onion, udon noodle, soy sauce, broccoli, ginger, garlic</p>
                    </div>
                </div>
                {/* {recipes.map((recipe) => (
                <SingleRecipe key={recipe.id} recipe={recipe} onClick={onRecipeClick} />
                ))} */}
            </div>
        </div>
    )
};

export default Recipes;
