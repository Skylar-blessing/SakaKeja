import React, { useState, useEffect } from 'react';
import SearchComponent from './SearchComponent';
import PropertyCard from './PropertyCard';

const PropertyExplore = () => {
  const [properties, setProperties] = useState([]);
  const [filteredProperties, setFilteredProperties] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/properties')
      .then((response) => response.json())
      .then((data) => {
        if (data && Array.isArray(data.data)) {
          setProperties(data.data);
          setFilteredProperties(data.data);
        } else {
          console.error('Invalid data format received from API:', data);
        }
      })
      .catch((error) => console.error('Error fetching properties:', error));
  }, []);

  const applyFilters = (filterType, filterValue) => {
    let filtered = properties;

    if (filterType === 'location') {
      filtered = filtered.filter(property =>
        property.location.toLowerCase().includes(filterValue.toLowerCase())
      );
    } else if (filterType === 'price') {
      filtered = filtered.filter(property => property.price <= filterValue);
    } else if (filterType === 'bedrooms') {
      filtered = filtered.filter(property => property.number_of_rooms <= filterValue);
    }

    setFilteredProperties(filtered);
  };

  return (
    <div className="property-explore">
      <h2>Explore Properties</h2>
      <SearchComponent applyFilters={applyFilters} />
      <div className="property-list">
        {filteredProperties.map(property => (
          <PropertyCard key={property.id} property={property} />
        ))}
      </div>
    </div>
  );
};

export default PropertyExplore;
