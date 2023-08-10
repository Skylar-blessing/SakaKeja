import React from 'react';
// import Header from './Header';
import Welcome from './Welcome';
import OurCompany from './OurCompany';
import PropertyExplore from './PropertyExplore';
import ContactUs from './ContactUs';
import Blog from './Blog';


const Main = () => {
  return(
    <div className="app-container">
      {/* <Header /> */}
      <Welcome />
      <OurCompany />
      <PropertyExplore />
      <Blog />
      <ContactUs />

    </div>
  );
};

export default Main;
