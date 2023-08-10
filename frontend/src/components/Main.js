import React from 'react';
import Header from './Header';
import Welcome from './Welcome';
import OurCompany from './OurCompany';
import PropertyExplore from './PropertyExplore';
import Blog from './Blog';
import ContactUs from './ContactUs';
import Footer from './Footer';



const Main = () => {
  return(
    <div>
      <div className="app-container">
      <Header />
      <Welcome />
      </div>
      <div className='AboutU'>
        <OurCompany />
      </div>
      <div className='PropEx'>
      <PropertyExplore />
      </div>
      <div className='Blog'>
      <Blog />
      </div>
      <div className='Contact'>
      <ContactUs />
      </div>
      <div>
        <Footer />
      </div>
    </div>
  );
};

export default Main;