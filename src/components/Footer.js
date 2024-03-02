import React from 'react';
import './Footer.css';
import { Link } from 'react-router-dom';


function Footer() {
  return (
    <div id='contact-us'>
    <div className='footer-container'>
      <section className='footer-email'>
        <p className='footer-email-heading'>
          Contact Us
        </p>
        <a href='mailto:ingreedy@business.com' className='footer-email-text'>
         ingreedy@business.com
        </a>    
        <p className='footer-coder-text'>
         Website by Charli's (XCX) Angels
        </p>
      </section>
       
      <section class='social-media'>
        <div class='social-media-wrap'>
          <div class='footer-logo'>
          </div>
          <small class='website-rights'>Ingreedy © 2023</small>
          <div class='social-icons'>
            <Link
              class='social-icon-link facebook'
              to='/'
              target='/'
              aria-label='Facebook'
            >
              <i class='fab fa-facebook-f' />
            </Link>
            <Link
              class='social-icon-link instagram'
              to='/'
              target='/'
              aria-label='Instagram'
            >
              <i class='fab fa-instagram' />
            </Link>
            <Link
              class='social-icon-link tik tok'
              to='/'
              target='/'
              aria-label='Tiktok'
            >
              <i class='fab fa-tiktok' />
            </Link>
            <Link
              class='social-icon-link x'
              to='/'
              target='/'
              aria-label='X'
            >
              <i class='fab fa-x' />
            </Link>
          </div>
        </div>
      </section>
    </div>
    </div>
  );
}


export default Footer;