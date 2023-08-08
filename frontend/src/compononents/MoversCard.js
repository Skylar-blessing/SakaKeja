import React from 'react';
import '../styles/MoversCard.css';

function MoversCard({ mover, handleBookService }) {
  return (
    <div className="card">
      <div className="logo-placeholder">
        {mover.image ? <img src={mover.image} alt={mover.name} /> : 'Logo'}
      </div>
      <h2>{mover.name}</h2>
      <p className="service-info">Service: {mover.service}</p>
      <div className="button-container">
        <button onClick={() => handleBookService(mover.id)}>Book Service</button>
        {mover.isBooked && (
          <p>The status of moving your items is: {mover.status}</p>
        )}
      </div>
    </div>
  );
}

export default MoversCard;
