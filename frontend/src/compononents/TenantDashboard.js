import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import PropertyList from './PropertyList';
import Movers from './Movers';
import Settings from './Settings';
import Payments from './Payments';

function TenantDashboard() {
  const navigate = useNavigate();
  const [userData, setUserData] = useState(null);
  const [showPropertyList, setShowPropertyList] = useState(true);
  const [showMovers, setShowMovers] = useState(false);
  const [showSettings, setShowSettings] = useState(false);
  const [showPayments, setShowPayments] = useState(false);

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

  const handleLogout = () => {
    localStorage.removeItem('user_id');
    navigate('/login');
  };

  return (
    <div style={{ display: 'flex' }}>
      <div style={{ width: '20%', height: '100vh', backgroundColor: '#dcdcdc', padding: '20px' }}>
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          <li style={{ marginBottom: '10px' }}>
            <div onClick={() => setShowPropertyList(true)} style={{ cursor: 'pointer' }}>Rent</div>
          </li>
          <li style={{ marginBottom: '10px' }}>
            <div onClick={() => setShowMovers(true)} style={{ cursor: 'pointer' }}>Movers</div>
          </li>
          <li style={{ marginBottom: '10px' }}>
            <div onClick={() => setShowPayments(true)} style={{ cursor: 'pointer' }}>Payments</div>
          </li>
          <li style={{ marginBottom: '10px' }}>
            <div onClick={() => setShowSettings(true)} style={{ cursor: 'pointer' }}>Settings</div>
          </li>
          <li style={{ marginBottom: '10px' }}>
            <button onClick={handleLogout} style={{ background: '#3A5B22', color: 'white', border: 'none', cursor: 'pointer', padding: '5px 10px' }}>Logout</button>
          </li>
        </ul>
      </div>

      <div style={{ flex: 1, padding: '20px' }}>
        <div style={{ padding: '20px' }}>
          {userData && <p>Hi, {userData.first_name}</p>}
        </div>

        {showPropertyList && <PropertyList />}
        {showMovers && <Movers />}
        {showSettings && <Settings />}
        {showPayments && <Payments />}
      </div>
    </div>
  );
}

export default TenantDashboard;
