import React from 'react';
import Main from './Main'
import AboutUs from './OurCompany';
import PropertyExplore from './PropertyExplore';

const App = () => {
  return (
    <div>
      <Main />
      <AboutUs />
      <PropertyExplore />
      {/* Other sections/components */}
    </div>
  );
};

export default App;