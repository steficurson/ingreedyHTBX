import './Welcome-style.css'
import veg from '../images/veggies.jpg'

const Welcome = () => {
    return (
        <div className='WelcomeContainer'>
                <div className='WelcomeContent'>
                    <div className='WelcomeImg'>
                        <img className='Img'src={veg} alt="veg"/> 
                    </div>
                    <div className='WelcomeContentText'>
                        <div className='WelcomeContentTitle'><h2>What is Ingreedy?</h2></div>
                        <div className='WelcomeText'>
                            <p>Got spare ingredients left in the fridge? Not sure what to make?
                            We have a variety of categories to choose from that help meet your needs in finding unique recipes just for you.
                            You can customize the ingredients you want to be added in your meal. </p>
                        </div>
                    </div>
                </div> 
        </div>
    )
}

export default Welcome;