
import { Link } from "react-router-dom"


import React from 'react';


 const NavBar = () => {
    return ( 
      <>
        <div className="nav-link">
            <nav className="links">
            <Link className="link" to="/"  href="">Home</Link>
              <Link  className="link" to="/Properties" href="">Properties</Link>
                <Link  className="link" to="/ContactUs"  href="">Contact Us</Link>
                </nav>    
        </div>
        </>
     );
 }
  
 export default NavBar;
