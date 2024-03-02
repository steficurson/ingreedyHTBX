import React from 'react';
import '../App.css'
import Welcome from '../components/Welcome';
import Search from '../components/Search';
import Recipes from '../components/Recipes';
import Footer from '../components/Footer'


function Home() {
    return (
        <div>
        <Welcome/>
        <Search/>
        <Recipes />
        <Footer/>
        </div>
    );
}

export default Home;