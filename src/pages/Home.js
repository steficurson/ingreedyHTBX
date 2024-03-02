import React from 'react';
import '../App.css'
import Welcome from '../components/Welcome';
import Search from '../components/Search';


function Home() {
    return (
        <div>
        <Welcome/>
        <Search/>
        </div>
    );
}

export default Home;