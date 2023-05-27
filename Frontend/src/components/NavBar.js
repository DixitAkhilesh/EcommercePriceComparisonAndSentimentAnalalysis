import React from 'react';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar" style={{margin: '0', padding:'20px'}}>
        <a href="/" style={{color:"white", textDecoration: 'none', fontSize: '20px'}}>CompareKar</a>
        <div className="navbar-links">
            <a href="/about" style={{color:"white", textDecoration: 'none'}}>About</a>
            <a href="/contact" style={{color:"white", textDecoration: 'none'}}>Contact Us</a>
        </div>
    </nav>
  );
}

export default Navbar;
