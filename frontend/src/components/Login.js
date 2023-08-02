import React, { useState } from "react";


const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle login logic here using the 'email' and 'password' states.
    // For example, you could send the data to a backend server for authentication.
  };

  const handleGmailSignIn = () => {
    // Handle Gmail sign-in logic here.
    // You might use an external authentication library or a backend service.
  };

  const handleAppleSignIn = () => {
    // Handle Apple sign-in logic here.
    // You might use an external authentication library or a backend service.
  };

  return (
    <div className='login'>
      <h2>Welcome back!</h2>
      <p>Enter your credentials to access you account.</p>
      <form className="login_form" onSubmit={handleSubmit}>
        <label>
          Email Address:
          <input type="email" value={email} onChange={handleEmailChange} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={handlePasswordChange} />
        </label>
        <br />
        <button type="submit">Login</button>
        <div>
          <p>                      or              </p>
        </div>
        <div>
        {/* Buttons for signing in with Gmail and Apple */}
        <button className='google-logo' type="button" onClick={handleGmailSignIn}>
          Sign in with Gmail
        </button>
        <div></div>
        <button className='apple-logo' type="button" onClick={handleAppleSignIn}>
          Sign in with Apple
        </button>
        </div>  
      </form>
    </div>
  );
};

export default Login;