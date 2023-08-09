import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';

function TenantPropertyReview() {
  const location = useLocation(); // Get the location object from React Router
  const propertyId = location.state?.propertyId; // Access property ID from location state
  const [property, setProperty] = useState(null);

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
            {/* Render property details here */}
            <h2>{property.location}</h2>
            <p>Price: ${property.price}</p>
            <p>Number of Rooms: {property.number_of_rooms}</p>
            <p>Description: {property.description}</p>
            <p>Category: {property.category}</p>
            {/* Add more details as needed */}
          </div>
        </div>
      ) : (
        <p>Loading property details...</p>
      )}
    </div>
  );
}

export default TenantPropertyReview;
