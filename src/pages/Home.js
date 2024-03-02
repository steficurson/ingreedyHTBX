import React from 'react';
import '../App.css'
import Welcome from '../components/Welcome';
import Search from '../components/Search';
import Footer from '../components/Footer'


function Home() {
    return (
        <div>
        <Welcome/>
        <Search/>
        <Footer/>
        </div>
    );
}

export default Home;