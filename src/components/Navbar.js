import React, { useState, useEffect, View } from 'react';
import { Link, redirect } from 'react-router-dom';
import './Navbar.css';
import tomat from '../images/TOMATO.png'

function Navbar() {
    const [click, setClick] = useState(false);
    const [button, setButton] = useState(true)

    const handleClick = () => setClick(!click);
    const closeMobileMenu = () => setClick(false)

    const showButton = () => {
        if(window.innerWidth <= 960) {
            setButton(false);
        } else {
            setButton(true);
        }
    };

    useEffect(() => { showButton(); }, []);

    window.addEventListener('resize', showButton);

  return (
    <>
    <nav className='navbar'>
        <div className='navbar-container'>
            <div style={{flexDirection:'row', justifySelf:'start', alignItems:'center', display:'flex'}}>
            <a className="logo_image" href="/"><img style={{width:75, height:70, paddingRight:10}} onClick={closeMobileMenu} src={tomat} alt=''/></a>
            <h1 style={{color: '#d6322c'}}>Ingreedy</h1>
            </div>

            <div className='menu-icon' onClick={handleClick}>
                <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
            </div>
            <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                <li className='nav-item'>
                    <Link to='/' className='nav-links' onClick={closeMobileMenu}>Home</Link>
                </li>
                <li className='nav-item'>
                    <Link to='/about' className='nav-links' onClick={closeMobileMenu}>About</Link>
                </li>
                <li className='nav-item'>
                    <Link to='/contact-us' className='nav-links' onClick={closeMobileMenu}>Contact Us</Link>
                </li>
            </ul>
        </div>
    </nav>
    </>
  )
}

export default Navbar