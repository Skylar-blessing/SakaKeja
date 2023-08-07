import React from 'react';
import Header from './Header';
import Welcome from './Welcome';
import Search from './Search';

const App = () => {
  return (
    <div className="app-container">
      <Header />
      <Welcome />
      <Search />
      {/* Other sections/components */}
    </div>
  );
};

export default App;
