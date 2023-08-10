import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

const SearchComponent = ({ applyFilters }) => {
  const [filterType, setFilterType] = useState('');
  const [filterValue, setFilterValue] = useState('');

  const handleSearch = () => {
    applyFilters(filterType, filterValue);
  };

  return (
    <div className="search-container">
      <div className="filter-select">
        <select value={filterType} onChange={(e) => setFilterType(e.target.value)}>
          <option value="">Select Filter</option>
          <option value="location">Location</option>
          <option value="price">Price</option>
          <option value="bedrooms">Bedrooms</option>
        </select>
      </div>
      <div className="filter-input">
        <input
          type="text"
          placeholder="Filter Value"
          value={filterValue}
          onChange={(e) => setFilterValue(e.target.value)}
        />
      </div>
      <div className="search-icon" onClick={handleSearch}>
        <FontAwesomeIcon icon={faSearch} />
      </div>
    </div>
  );
};

export default SearchComponent;