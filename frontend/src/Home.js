import React from 'react';
import NavBar from "./NavBar";
import { Link } from "react-router-dom"

const Home = () => {
  
  return (
    <>
<NavBar />
     <div className='heading'>


      <h1>Find Home!</h1>
      <p > Discover.</p>
      <nav>
      <Link  className="link" to="/properties"  href=""> View properties</Link>
      </nav>
      </div>    
    </>
  );
};

export default Home;
