import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function TenantDashboard() {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    const fetchUserData = async () => {
      const userId = localStorage.getItem('user_id');
      console.log('User ID:', userId);
      if (!userId) {
        console.error('User ID not found in local storage.');
        return;
      }

      try {
        const response = await fetch(`http://127.0.0.1:5000/users/${userId}`);
        const data = await response.json();
        if (data && data.first_name) {
          setUserData(data);
        } else {
          console.error('User data not in the expected format.');
        }
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    };

    fetchUserData();
  }, []);

  return (
    <div>
      <div style={{ padding: '20px' }}>
        {userData && <p>Hi, {userData.first_name}</p>}
      </div>

      <div style={{ width: '20%', height: '100vh', backgroundColor: '#f7f7f7', padding: '20px' }}>
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          <li style={{ marginBottom: '10px' }}>
            <Link to="/rent">Rent</Link>
          </li>
          <li style={{ marginBottom: '10px' }}>
            <Link to="/payments">Payments</Link>
          </li>
          <li style={{ marginBottom: '10px' }}>
            <Link to="/movers">Movers</Link>
          </li>
          <li style={{ marginBottom: '10px' }}>
            <Link to="/settings">Settings</Link>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default TenantDashboard;
