import React from 'react';

function MoversCard({ mover, handleBookService }) {
  return (
    <div style={{ border: '1px solid #ddd', padding: '10px', width: '300px' }}>
      <div style={{ marginBottom: '10px', height: '150px', backgroundColor: '#eee', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <span style={{ fontSize: '24px' }}>Logo</span>
      </div>
      <h2>{mover.name}</h2>
      <p>Service: {mover.service}</p>
      <div>
        <button onClick={() => handleBookService(mover.id)}>Book Service</button>
        {mover.isBooked && (
          <p>The status of moving your items is: {mover.status}</p>
        )}
      </div>
    </div>
  );
}

export default MoversCard;
