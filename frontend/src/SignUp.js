import React, { useState } from 'react';
import './SignIn.css'
import Login from './Login';

const SignUp = () => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('tenant');

  const handleFirstNameChange = (e) => {
    setFirstName(e.target.value);
  };

  const handleLastNameChange = (e) => {
    setLastName(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleRoleChange = (e) => {
    setRole(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle sign-up logic here using the form data.
    // For example, you could send the data to a backend server for user registration.
  };

  const handleGmailSignUp = () => {
    // Handle Gmail sign-up logic here.
    // You might use an external authentication library or a backend service.
  };

  const handleAppleSignUp = () => {
    // Handle Apple sign-up logic here.
    // You might use an external authentication library or a backend service.
  };

  const login = () => {
    return <Login/>
  }

  return (
    <div>
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit}>
        <label>
          First Name:
          <input type="text" value={firstName} onChange={handleFirstNameChange} />
        </label>
        <br />
        <label>
          Last Name:
          <input type="text" value={lastName} onChange={handleLastNameChange} />
        </label>
        <br />
        <label>
          Email:
          <input type="email" value={email} onChange={handleEmailChange} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={handlePasswordChange} />
        </label>
        <br />
        <label>
          Role:
          <select value={role} onChange={handleRoleChange}>
            <option value="tenant">Tenant</option>
            <option value="owner">Owner</option>
          </select>
        </label>
        <br />
        <button type="submit">Sign Up</button>
        <div>
            <p> ----------------------- or ---------------------</p>
        </div>
        <div>

        {/* Buttons for signing up with Gmail and Apple */}
        <button className='google-logo' type="button" onClick={handleGmailSignUp}>
          Sign up with Gmail
        </button>
        <div></div>
        <button className='apple-logo' type="button" onClick={handleAppleSignUp}>
          Sign up with Apple
        </button>
        </div>
        
      </form>
      <div>
      <p> Already have an account?</p>
      <button onClick={login}>Login</button>
      </div>
      
      
    </div>
    
  );
};

export default SignUp;
