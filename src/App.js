import './App.css';
import React from 'react';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home'
import About from './pages/About';

function App() {
  return (
    <>
      <Router>
      <Navbar />
      <Routes>
        <Route path='/' exact element= {<Home/>} />
        <Route path='/about' exact element= {<About/>} />
      </Routes>
      </Router>
    </>
  );
}

export default App;