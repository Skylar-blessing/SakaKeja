import React, { useState, useEffect } from 'react';

const PropertyExplore = () => {
  const [properties, setProperties] = useState([]);

  useEffect(() => {
    // Fetch properties from the backend API
    fetch('http://127.0.0.1:5000/properties') 
      .then(response => response.json())
      .then(data => {
        setProperties(data.data.slice(0, 9)); // Display only the first 9 properties
      })
      .catch(error => {
        console.error('Error fetching properties:', error);
      });
  }, []);

  return (
    <div className="property-explore">
      <h2>Explore Properties</h2>
      <div className="property-list">
        {properties.map(property => (
          <div key={property.id} className="property-card">
            <img src={property.image_urls[0]} alt={property.location} />
            <div className="property-details">
              <h3>{property.location}</h3>
              <p>Price: ${property.price}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PropertyExplore;
