import React from "react";
import aboutImage from "../images/cc.jpg";
import aboutImage2 from "../images/dd.jpg";

const OurCompany = () => {
  return (
    <section className="about-us">
      <div className="about-content">
        <div className="about-text">
          <h4>Who we are</h4>
          <h2>
            Discover a Home and Relocate in a Fast and Simple Way and Start Living with SakaKeja.
          </h2>
          <p>
            SakaKeja is a real estate agency specializing in discovering friendly homes and neighborhoods. We offer a range of friendly properties, including homes, homes built with eco-friendly materials, and homes equipped with sustainable technologies such as solar panels.
          </p>
        </div>
        <div
          className="about-image"
          style={{
            backgroundImage: `url(${aboutImage})`,
          }}
        ></div>
      </div>
      <br />
      <div className="about-content">
        <div
          className="about-image"
          style={{
            backgroundImage: `url(${aboutImage2})`,
          }}
        ></div>
        <div className="about-text">
          <h4>
            Our Mission
          </h4>
          <h2>
            Building a Better Future with Friendly Neighborhoods.
          </h2>
          <p>
            The agency's mission is to provide clients with a selection of properties that meet high environmental standards, while also providing a comfortable and luxurious lifestyle.
          </p>
        </div>
      </div>
    </section>
  );
};

export default OurCompany;