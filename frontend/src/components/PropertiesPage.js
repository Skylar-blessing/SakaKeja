import React, { useState } from 'react';

const PropertiesPage = () => {
  const [location, setLocation] = useState('');
  const [propertyType, setPropertyType] = useState('all');
  const [priceRange, setPriceRange] = useState('');
  const [style, setStyle] = useState('');

  const handleSearch = () => {
    console.log('Location:', location);
    console.log('Property Type:', propertyType);
    console.log('Price Range:', priceRange);
    console.log('Style:', style);
  };

  return (
    <div className="properties-container">
      <div className="search-input">
        <input
          type="text"
          placeholder="Search..."
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />
      </div>
      <div className="welcome-message">
        <p>Welcome, username!</p>
      </div>
      <div className="menu">
        <div className="left-menu">
          <ul>
            <li>Buy</li>
            <li>Rent</li>
            <li>Payments</li>
            <li>Settings</li>
          </ul>
        </div>
        <div className="mid-left-filter">
          <label>Location:</label>
          <input
            type="text"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
          />
          <label>Type of Place:</label>
          <select
            value={propertyType}
            onChange={(e) => setPropertyType(e.target.value)}
          >
            <option value="all">All</option>
            <option value="apartment">Apartment</option>
            <option value="house">House</option>
          </select>
          <label>Price Range:</label>
          <input
            type="text"
            value={priceRange}
            onChange={(e) => setPriceRange(e.target.value)}
          />
          <label>Styles:</label>
          <input
            type="text"
            value={style}
            onChange={(e) => setStyle(e.target.value)}
          />
        </div>
      </div>
      <div className="results">
        <p>Results of the Search:</p>
        <p>Location: {location}</p>
        <p>Property Type: {propertyType}</p>
        <p>Price Range: {priceRange}</p>
        <p>Style: {style}</p>
      </div>
      <div className="logout-button">
        <button>Logout</button>
      </div>
    </div>
  );
};

export default PropertiesPage;
