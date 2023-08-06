import React from "react";
import aboutImage from "../images/Img2.jpg"; 

const AboutUs = () => {
  return (
    <section className="about-us">
      <div className="about-content">
        <div className="about-text">
          <h2>About Us</h2>
          <p>
            Saka-Keja is a real estate platform that connects property owners
            and tenants. We aim to make the process of finding a home or
            renting out a property easy, efficient, and stress-free. Our
            platform allows property owners to list their properties for rent,
            and tenants can easily search for properties that meet their
            requirements.
          </p>
        </div>
        <div
          className="about-image"
          style={{
            backgroundImage: `url(${aboutImage})`}}
        ></div>
      </div>
    </section>
  );
};

export default AboutUs;


// AboutUs.js

// import React from 'react';
// // import aboutImage from '../images/cc.jpg'; // Import the image

// const AboutUs = () => {
//   return (
//     <section className="about-us" id="about">
//       <div className="about-content">
//         <div className="about-text">
//           <h2>About Us</h2>
          // <p>
          //   Saka-Keja is a real estate platform that connects property owners
          //   and tenants. We aim to make the process of finding a home or
          //   renting out a property easy, efficient, and stress-free. Our
          //   platform allows property owners to list their properties for rent,
          //   and tenants can easily search for properties that meet their
          //   requirements.
          // </p>
//         </div>
//         <div className="about-image" ></div>
//       </div>
//     </section>
//   );
// };

// export default AboutUs;
