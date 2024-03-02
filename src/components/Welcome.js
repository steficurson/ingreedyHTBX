import './Welcome-style.css'

const Welcome = () => {
    return (
        <div className='WelcomeContainer'>
                <div className='WelcomeContent'>
                    <div className='WelcomeImg'>
                        {/* <img className='Img'src={hi} alt="veg"/> */}
                    </div>
                    <div className='WelcomeContentText'>
                        <div className='WelcomeContentTitle'><h2>What is Ingreedy?</h2></div>
                        <div className='WelcomeText'>
                            <p>Got spare ingredients left in the fridge? Not sure what to make?
                            We have a variety of categories to choose from that help meet your needs in finding unique recipes just for you.
                            You can customize the ingredients you want to be added in your meal. </p>
                        </div>
                        <div className='WelcomeText'>
                            <p>
                            We will find a variety of recipes based on your meal type, cooking level, time and ingredients. 
                            Start by using the available search bar to add ingredients.</p>
                        </div>
                    </div>
                </div> 
        </div>
    )
}

export default Welcome;