import React from 'react';
// import Header from './Header';
import Welcome from './Welcome';
import OurCompany from './OurCompany';
import PropertyExplore from './PropertyExplore';


const Main = () => {
  return(
    <div className="app-container">
      {/* <Header /> */}
      <Welcome />
      <OurCompany />
      <PropertyExplore />
    </div>
  );
};

export default Main;
