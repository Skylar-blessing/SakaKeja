import React from 'react';
import Header from './Header';
import Welcome from './Welcome';
import Search from './Search';
import Login from './Login';

const App = () => {
  return (
    <div className="app-container">
      <Header />
      <Welcome />
      <Search />
      <Login />
    </div>
  );
};

export default App;