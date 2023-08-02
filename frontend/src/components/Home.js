import React from 'react';
import NavBar from "./NavBar";
import { Link } from "react-router-dom"

const Home = () => {
  
  return (
    <>
<NavBar />
     <div className='heading'>
      <div className='gif'>
      <h1>Find Home!</h1>
      <p > Discover.</p>
      <nav>
      <Link  className="link" to="/properties"  href=""> View properties</Link>
      </nav>
        <img src='https://media.giphy.com/media/l0IylQoMkcbZUbtKw/giphy.gif' />
      </div>

      
      </div>    
    </>
  );
};

export default Home;