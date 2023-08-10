import React from 'react';
import Main from './Main';
import Login from './Login'; 
import SignUp from './SignUp';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import OwnerDashboard from './OwnerDashboard';
import TenantDashboard from './TenantDashboard';
import PropertyList from './PropertyList'
import PostProperty from './PostProperty';
import ViewProperties from './ViewProperties';
import ViewPaymentBalance from './ViewPayments';
import TenantPropertyReview from './TenantPropertyReview';
import Payments from './Payments';


const App = () => {
  return (
    <Router>
      <div>
        <Routes>
        <Route path="/" element={<Main />} />
        </Routes>
        
        <Routes> 
          <Route path="/login" element={<Login />} /> 
          <Route path="/signup" element={<SignUp />} />
          <Route path="/owner-dashboard" element={<OwnerDashboard />} />
        <Route path="/tenant-dashboard" element={<TenantDashboard />} />
        <Route path="/rent" element={<PropertyList />} />
        <Route path="/post-property" element={<PostProperty />} />
        <Route path="/view-properties" element={<ViewProperties />} />
        <Route path="/view-payment-balance" element={<ViewPaymentBalance />} />
        <Route path="/tenant-property-review" element={<TenantPropertyReview />} />
        <Route path="/payments" element={<Payments />} />
        </Routes>

        
        
      </div>
    </Router>
  );
};

export default App;
