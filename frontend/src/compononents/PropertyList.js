import React, { useState, useEffect } from 'react';
import PropertyCard from './PropertyCard';

function PropertyList() {
  const [properties, setProperties] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/properties')
      .then((response) => response.json())
      .then((data) => {
        if (data && Array.isArray(data.data)) {
          setProperties(data.data);
        } else {
          console.error('Invalid data format received from API:', data);
        }
      })
      .catch((error) => console.error('Error fetching properties:', error));
  }, []);

  const propertyCardsContainerStyle = {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))',
    gap: '20px',
    justifyItems: 'center',
  };

  return (
    <div style={propertyCardsContainerStyle}>
      {properties.map((property) => (
        <PropertyCard key={property.id} property={property} />
      ))}
    </div>
  );
}

export default PropertyList;
