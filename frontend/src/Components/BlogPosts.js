import React from 'react';
import { Link as ScrollLink } from 'react-scroll';
import blogImage1 from '../images/Home.jpeg'; 
import blogImage2 from '../images/hh.jpg'; 

const BlogPosts = () => {
  return (
    <section id="blog" className="blog-container">
      <h2 className="section-heading">Our Blog</h2>
      <div className="blog-post">
        <div className="blog-post-image">
          <img src={blogImage1} alt="Blog Post 1" />
        </div>
        <div className="blog-post-content">
          <h3 className="blog-post-title">Exploring New Trends in Real Estate</h3>
          <p className="blog-post-date">Posted on August 15, 2023</p>
          <p className="blog-post-text">
          The world of real estate is constantly evolving, shaped by economic shifts, technological advancements, and changing societal preferences. In recent years, several exciting trends have emerged, transforming the way we buy, sell, and live in properties. Let's dive into some of the new trends reshaping the real estate landscape.
          </p>
          <ScrollLink
            to="contact-us"
            spy={true}
            smooth={true}
            offset={-70}
            duration={500}
            className="blog-read-more"
          >
            Read More
          </ScrollLink>
        </div>
      </div>
      <div className="blog-post">
        <div className="blog-post-image">
          <img src={blogImage2} alt="Blog Post 2" />
        </div>
        <div className="blog-post-content">
          <h3 className="blog-post-title">The Future of Urban Living</h3>
          <p className="blog-post-date">Posted on August 25, 2023</p>
          <p className="blog-post-text">
          Urban living has long captured the imagination with its vibrancy, cultural diversity, and economic opportunities. However, the concept of urban living is undergoing a profound transformation, driven by technological advancements, demographic shifts, and the need for sustainable development. Here's a glimpse into what the future holds for urban dwellers:
          </p>
          <ScrollLink
            to="contact-us"
            spy={true}
            smooth={true}
            offset={-70}
            duration={500}
            className="blog-read-more"
          >
            Read More
          </ScrollLink>
        </div>
      </div>
    </section>
  );
};

export default BlogPosts;


// import React from 'react';

// const BlogPosts = () => {
//   return (
//     <section id="blog" className="blog">
//       <div className="blog-content">
//         <h2>Embracing Modern Trends in Property Construction: A Guide for Property Owners</h2>
//         <p>
//           In the ever-evolving landscape of real estate, staying updated with modern construction techniques is crucial for property owners. With advancements in technology and sustainability, building methods have transformed, offering improved efficiency, aesthetics, and durability. Whether you're planning a new construction or considering a renovation, here are some modern ways of building that can significantly enhance your property's value and appeal:

//           <br></br>
//           <button>Read More</button>
//         </p>
//       </div>
//     </section>
//   );
// };

// export default BlogPosts;

