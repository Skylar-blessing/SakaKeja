import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function PostProperty() {
  const navigate = useNavigate();
  const [bedrooms, setBedrooms] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [location, setLocation] = useState('');
  const [category, setCategory] = useState('');
  const [imageFiles, setImageFiles] = useState([]);

  const handleImageUpload = (event) => {
    const files = event.target.files;
    setImageFiles(files);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('bedrooms', bedrooms);
    formData.append('description', description);
    formData.append('price', price);
    formData.append('location', location);
    if (category) {
      formData.append('category', category);
    }
    for (const file of imageFiles) {
      formData.append('images', file);
    }

    const accessToken = localStorage.getItem('access_token');

    try {
      const response = await fetch('http://127.0.0.1:5000/properties', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
        body: formData,
      });

      const data = await response.json();

      if (response.ok) {
        alert('Property posted successfully!');
        navigate('/owner-dashboard');
      } else {
        alert(`Failed to post property: ${JSON.stringify(data)}`);
      }
    } catch (error) {
      console.error('Error occurred while posting property:', error);
    }
  };

  return (
    <div className="post-property-container">
      <h2>Post New Listing!</h2>
      <form onSubmit={handleSubmit}>
        <div className="property-input">
          <label>Bedrooms:</label>
          <input
            type="number"
            value={bedrooms}
            onChange={(e) => setBedrooms(e.target.value)}
          />
        </div>
        <div className="property-input">
          <label>Description:</label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>
        <div className="property-input">
          <label>Price:</label>
          <input
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
          />
        </div>
        <div className="property-input">
          <label>Location:</label>
          <input
            type="text"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
          />
        </div>
        <div className="property-input">
          <label>Category (optional):</label>
          <input
            type="text"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
          />
        </div>
        <div className="property-input">
          <label>Upload Images:</label>
          <input
            type="file"
            multiple
            accept="image/*"
            onChange={handleImageUpload}
          />
        </div>
        <button className="post-property-button" type="submit">
          Post Property
        </button>
      </form>
    </div>
  );
}

export default PostProperty;
