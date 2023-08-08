import React from 'react';
import '../styles/MoversCard.css';

function MoversCard({ mover, handleBookService }) {
  return (
    <div className="card">
      <div className="logo-placeholder">
        {mover.image ? <img src={mover.image} alt={mover.name} /> : 'Logo'}
      </div>
      <h2>{mover.name}</h2>
      <p className="service-info">{mover.service_details}</p>
      <div className="button-container">
        <button onClick={() => handleBookService(mover.id)}>Book Service</button>
        {mover.isBooked && (
          <p>Thank you for booking with us,
            The status of moving your items is: {mover.status}.
            We will notify you when complete</p>
        )}
      </div>
    </div>
  );
}

export default MoversCard;
