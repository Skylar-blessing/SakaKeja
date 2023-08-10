import React from 'react';
import Header from './Header';
import Welcome from './Welcome';
import OurCompany from './OurCompany';
import PropertyExplore from './PropertyExplore';
import BlogPosts from './BlogPosts';



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
      <BlogPosts />
      </div>
    </div>
  );
};

export default Main;