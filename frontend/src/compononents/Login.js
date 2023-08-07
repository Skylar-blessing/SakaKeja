import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Login.css';


function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (event) => {
    event.preventDefault();

    const loginData = {
      email,
      password,
    };

    try {
      const response = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(loginData),
      });

      if (response.ok) {
        const data = await response.json();
        const refreshToken = data.refresh_token;
        const userType = Object.keys(data)[1]; 

        saveRefreshToken(refreshToken); 

        if (userType === 'owner' || userType === 'tenant') {
          navigate(`/${userType}-dashboard`);
        } else {
        }
      } else {
      }
    } catch (error) {
      console.error('Error occurred during login:', error);
    }
  };

  const saveRefreshToken = (token) => {
    localStorage.setItem('refresh_token', token);
  };

  return (
    <div className="login-container">
      <div className="left-half">
        <h2>Welcome back!</h2>
        <p>Enter your credentials to access your account</p>
        <div className="login-form">
          <form onSubmit={handleLogin}>
            <div className="email-container">
              <label>Email address:</label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div className="password-container">
              <label>Password:</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <button className="login-button" type="submit">
              Login
            </button>
          </form>
        </div>
        <div className="sign-in-options">
          <p>Or sign in with:</p>
          <button className="signin-google-button">
            <img
              src="/images/Google.png"
              alt="Google Logo"
              className="signin-icon"
            />
            Sign in with Google
          </button>
          <button className="signin-apple-button">
            <img
              src="/home/steve/Saka-Keja/SakaKeja/frontend/src/images/Apple.png"
              alt="Apple Logo"
              className="signin-icon"
            />
            Sign in with Apple
          </button>
        </div>
        <div className="signup-option">
          <p>
            Don't have an account? <a href="/signup">Sign Up</a>
          </p>
        </div>
      </div>
      <div className="right-half"></div>
    </div>
  );
};
export default Login;
