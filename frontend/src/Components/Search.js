import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch, faFilter } from '@fortawesome/free-solid-svg-icons';
const SearchComponent = () => {
  const [selectedOption, setSelectedOption] = useState('Rent');

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div className="search-container">
      <div className="dropdown">
        <select value={selectedOption} onChange={handleOptionChange}>
          <option value="Rent">Rent</option>
          <option value="Sale">Sale</option>
        </select>
      </div>
      <div className="search-input">
        <input type="text" placeholder="Search..." />
      </div>
      <div className="filter-icon">
        <FontAwesomeIcon icon={faFilter} />
      </div>
      <div className="search-icon">
        <FontAwesomeIcon icon={faSearch} />
      </div>
    </div>
  );
};

export default SearchComponent;
