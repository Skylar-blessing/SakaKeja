// import React, { useState } from 'react';

// const LoginPage = () => {
//   const [userType, setUserType] = useState('owners');
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [rememberMe, setRememberMe] = useState(false);

//   const handleLogin = () => {
//     // Log user input data
//     console.log('User Type:', userType);
//     console.log('Email:', email);
//     console.log('Password:', password);
//     console.log('Remember Me:', rememberMe);
//   };

//   return (
//     <div className="login-container">
//       <h2>Welcome back!</h2>
//       <p>Enter your credentials to access your account</p>
//       <div className="user-type-dropdown">
//         <label>Select User Type:</label>
//         <select value={userType} onChange={(e) => setUserType(e.target.value)}>
//           <option value="owners">Owners</option>
//           <option value="tenants">Tenants</option>
//           <option value="admin">Admin</option>
//         </select>
//       </div>
//       <div className="login-form">
//         <div className="email-container">
//           <label>Email address:</label>
//           <input
//             type="email"
//             value={email}
//             onChange={(e) => setEmail(e.target.value)}
//           />
//         </div>
//         <div className="password-container">
//           <label>Password:</label>
//           <input
//             type="password"
//             value={password}
//             onChange={(e) => setPassword(e.target.value)}
//           />
//         </div>
//         <div className="remember-me-container">
//           <input
//             type="checkbox"
//             checked={rememberMe}
//             onChange={() => setRememberMe(!rememberMe)}
//           />
//           <label>Remember for 30 days</label>
//         </div>
//         <button className="login-button" onClick={handleLogin}>
//           Login
//         </button>
//         <div className="sign-in-options">
//           <p>Or sign in with:</p>
//           <button className="google-sign-in">Sign in with Google</button>
//           <button className="apple-sign-in">Sign in with Apple</button>
//         </div>
//       </div>
//       <div className="signup-option">
//         <p>Don't have an account? <a href="/signup">Sign Up</a></p>
//       </div>
//       <div className="google-logo">Google Logo</div>
//       <div className="apple-logo">Apple Logo</div>
//     </div>
//   );
// };

// export default LoginPage;
