import React from 'react'
import NavBar from './NavBar';
import { useState, useEffect } from 'react';

const Home = () => {
  const [property, setProperty] = useState([])
    useEffect(() => {
      fetch('http://localhost:3000/properties')
      .then((res)=> res.json())
      .then((properties)=> {
        setProperty(properties)
      })

  }, []);

  const filterProperties = (e) => {
    const search = e.target.value.toLowerCase();
    if (search === "") {
      fetch("http://localhost:3000/properties")
      .then((res) => res.json())
      .then((properties) => {
        setProperty(properties)
      })
    }
    else {
      const filteredProperties = property.filter((property) =>
      property.Make.toLowerCase().includes(search)
      );
      setProperty(filteredProperties);
    }
  }

  return (
    <div>
      <h1 className="title">Saka Keja</h1>
      <div>
      <NavBar/>
      </div>
      <h1>Look, Like, Love, Live .</h1>
      <p>Discover the Advantages of Eco-Friendly Homes with Our Real Estate Agency.</p>
      <input className='search'
        type='search'
        onChange={(e) => filterProperties(e)}
        placeholder='Search by location...' />

    </div>
  )
}

export default Home;
