import React, { useState, useEffect } from 'react';
import PropertyList from './PropertyList';
import Movers from './Movers';
import Settings from './Settings';
import Payments from './Payments';

function TenantDashboard() {
  const [userData, setUserData] = useState(null);
  const [showPropertyList, setShowPropertyList] = useState(false);
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

  const handleRentClick = () => {
    setShowPropertyList(true);
    setShowMovers(false);
    setShowSettings(false);
    setShowPayments(false);
  };

  const handleMoversClick = () => {
    setShowMovers(true);
    setShowPropertyList(false);
    setShowSettings(false);
    setShowPayments(false);
  };

  const handleSettingsClick = () => {
    setShowSettings(true);
    setShowPropertyList(false);
    setShowMovers(false);
    setShowPayments(false);
  };

  const handlePaymentsClick = () => {
    setShowPayments(true);
    setShowPropertyList(false);
    setShowMovers(false);
    setShowSettings(false);
  };

  return (
    <div style={{ display: 'flex' }}>
      <div style={{ width: '20%', height: '100vh', backgroundColor: '#f7f7f7', padding: '20px' }}>
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          <li style={{ marginBottom: '10px' }}>
            <div onClick={handleRentClick} style={{ cursor: 'pointer' }}>Rent</div>
          </li>
          <li style={{ marginBottom: '10px' }}>
            <div onClick={handleMoversClick} style={{ cursor: 'pointer' }}>Movers</div>
          </li>
          <li style={{ marginBottom: '10px' }}>
            <div onClick={handleSettingsClick} style={{ cursor: 'pointer' }}>Settings</div>
          </li>
          <li style={{ marginBottom: '10px' }}>
            <div onClick={handlePaymentsClick} style={{ cursor: 'pointer' }}>Payments</div>
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
