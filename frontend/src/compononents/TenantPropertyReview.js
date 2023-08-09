import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';

function TenantPropertyReview() {
  const location = useLocation();
  const navigate = useNavigate();
  const propertyId = location.state?.propertyId;
  const [property, setProperty] = useState(null);
  const [showOwnerDetails, setShowOwnerDetails] = useState(false);
  const [ownerDetails, setOwnerDetails] = useState(null);

  useEffect(() => {
    if (propertyId) {
      const fetchPropertyDetails = async () => {
        try {
          const response = await fetch(`http://127.0.0.1:5000/properties/${propertyId}`);
          const data = await response.json();
          if (response.ok) {
            setProperty(data);
          } else {
            console.error('Error fetching property details:', data);
          }
        } catch (error) {
          console.error('Error fetching property details:', error);
        }
      };

      const fetchOwnerDetails = async () => {
        if (property && property.owner_id) {
          try {
            const response = await fetch(`http://127.0.0.1:5000/users/${property.owner_id}`);
            const data = await response.json();
            if (response.ok) {
              setOwnerDetails(data);
            } else {
              console.error('Error fetching owner details:', data);
            }
          } catch (error) {
            console.error('Error fetching owner details:', error);
          }
        }
      };

      fetchPropertyDetails();
      fetchOwnerDetails();
    }
  }, [propertyId, property]);

  const handleBookClick = () => {
    setShowOwnerDetails(true);
  };

  return (
    <div>
      {property ? (
        <div>
          <div className="carousel-container">
            <Carousel
              showThumbs={false}
              showStatus={false}
              infiniteLoop={true}
            >
              {property.image_urls.reverse().map((imageUrl, index) => (
                <div key={index} className="slide-container">
                  <div className="image-holder">
                    <img src={imageUrl} alt={`Property ${index + 1}`} className="slide-image" />
                  </div>
                </div>
              ))}
            </Carousel>
          </div>
          <div>
            <h2>{property.location}</h2>
            <p>Price: ${property.price}</p>
            <p>Number of Rooms: {property.number_of_rooms}</p>
            <p>Description: {property.description}</p>
            <p>Category: {property.category}</p>
            {showOwnerDetails && ownerDetails && (
              <div>
                <p>Owner: {ownerDetails.first_name}</p>
                <p>Phone Number: {ownerDetails.phone_number}</p>
              </div>
            )}
            <button onClick={() => navigate('/payments')} style={{ background: '#3A5B22', color: 'white', border: 'none', cursor: 'pointer', padding: '5px 10px' }}>Pay</button>
            <button onClick={handleBookClick} style={{ background: '#3A5B22', color: 'white', border: 'none', cursor: 'pointer', padding: '5px 10px' }}>Book</button>
          </div>
        </div>
      ) : (
        <p>Loading property details...</p>
      )}
    </div>
  );
}

export default TenantPropertyReview;
