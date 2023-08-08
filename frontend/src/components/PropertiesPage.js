// import React, { useState } from 'react';

// const PropertiesPage = () => {
//   const [location, setLocation] = useState('');
//   const [propertyType, setPropertyType] = useState('all');
//   const [priceRange, setPriceRange] = useState('');
//   const [style, setStyle] = useState('');
//   const [properties, setProperties] = useState([
//     {
//       id: 1,
//       image: 'path/to/property1.jpg',
//       location: 'Nairobi',
//       propertyType: 'House',
//       price: 40000,
//       style: 'Mansion',
//     },
//     {
//       id: 2,
//       image: 'path/to/property2.jpg',
//       location: 'Mombasa',
//       propertyType: 'Apartment',
//       price: 25000,
//       style: 'Cottage',
//     },
//   ]);

//   const handleSearch = () => {
//     const filteredProperties = properties.filter((property) => {
//       return (
//         (location === '' || property.location.toLowerCase().includes(location.toLowerCase())) &&
//         (propertyType === 'all' || property.propertyType === propertyType) &&
//         (priceRange === '' || property.price <= parseInt(priceRange)) &&
//         (style === '' || property.style.toLowerCase().includes(style.toLowerCase()))
//       );
//     });

//     setProperties(filteredProperties);
//   };

//   return (
//     <div className="properties-container">
//       <div className="search-input">
//         <input
//           type="text"
//           placeholder="Search..."
//           value={location}
//           onChange={(e) => setLocation(e.target.value)}
//         />
//         <button className="filter-button" onClick={handleSearch}>
//           Filter
//         </button>
//       </div>
//       <div className="menu">
//         <div className="left-menu">
//           <ul>
//             <li>Buy</li>
//             <li>Rent</li>
//             <li>Payments</li>
//             <li>Settings</li>
//           </ul>
//         </div>
//         <div className="mid-left-filter">
//           <label>Location:</label>
//           <input
//             type="text"
//             value={location}
//             onChange={(e) => setLocation(e.target.value)}
//           />
//           <label>Type of Place:</label>
//           <select
//             value={propertyType}
//             onChange={(e) => setPropertyType(e.target.value)}
//           >
//             <option value="all">All</option>
//             <option value="Apartment">Apartment</option>
//             <option value="House">House</option>
//           </select>
//           <label>Price Range:</label>
//           <input
//             type="text"
//             value={priceRange}
//             onChange={(e) => setPriceRange(e.target.value)}
//           />
//           <label>Styles:</label>
//           <input
//             type="text"
//             value={style}
//             onChange={(e) => setStyle(e.target.value)}
//           />
//         </div>
//       </div>
//       <div className="properties">
//         {properties.map((property) => (
//           <div className="property-card" key={property.id}>
//             <img src={property.image} alt={property.location} />
//             <div className="property-details">
//               <p>Location: {property.location}</p>
//               <p>Property Type: {property.propertyType}</p>
//               <p>Price: {property.price}</p>
//               <p>Style: {property.style}</p>
//             </div>
//           </div>
//         ))}
//       </div>
//       <div className="logout-button">
//         <button>Logout</button>
//       </div>
//     </div>
//   );
// };

// export default PropertiesPage;