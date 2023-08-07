import React from 'react';
import Main from './Main'
import AboutUs from './OurCompany';
import PropertiesPage from './PropertiesPage';

const App = () => {
  return (
    <div>
      <Main />
      <AboutUs />
      <PropertiesPage />
      {/* Other sections/components */}
    </div>
  );
};

export default App;