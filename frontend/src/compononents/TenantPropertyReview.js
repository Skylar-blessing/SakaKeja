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
  const [reviews, setReviews] = useState([]);

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

      fetchPropertyDetails();
    }
  }, [propertyId]);

  useEffect(() => {
    if (property && property.owner_id) {
      const fetchOwnerDetails = async () => {
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
      };

      fetchOwnerDetails();
    }
  }, [property]);

  useEffect(() => {
    if (propertyId) {
      const fetchPropertyReviews = async () => {
        try {
          const response = await fetch(`http://127.0.0.1:5000/reviews?property_id=${propertyId}`);
          const data = await response.json();
          if (response.ok && Array.isArray(data.data)) {
            setReviews(data.data);
          } else {
            console.error('Error fetching property reviews:', data);
          }
        } catch (error) {
          console.error('Error fetching property reviews:', error);
        }
      };
  
      fetchPropertyReviews();
    }
  }, [propertyId]);

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
            <div>
              <h3>Reviews</h3>
              {reviews.length > 0 ? (
                <ul>
                  {reviews.map((review) => (
                    <li key={review.id}>
                      <p>Review by: {review.tenant.first_name}</p>
                      <p>Rating: {review.rating} stars</p>
                      <p>{review.review_text}</p>
                    </li>
                  ))}
                </ul>
              ) : (
                <p>No reviews available.</p>
              )}
            </div>
          </div>
        </div>
      ) : (
        <p>Loading property details...</p>
      )}
    </div>
  );
}

export default TenantPropertyReview;
