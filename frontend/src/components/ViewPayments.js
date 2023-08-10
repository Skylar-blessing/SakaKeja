import React, { useState } from 'react';

function ViewPayments() {
  const [balance, setBalance] = useState(1500); // Example initial balance
  const [withdrawAmount, setWithdrawAmount] = useState('');
  const [transferAmount, setTransferAmount] = useState('');
  const [transferAccount, setTransferAccount] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleWithdraw = () => {
    if (withdrawAmount <= balance) {
      setBalance(balance - withdrawAmount);
      setSuccessMessage(`Withdrawal of $${withdrawAmount} successful!`);
      setErrorMessage('');
    } else {
      setErrorMessage('Insufficient balance for withdrawal');
      setSuccessMessage('');
    }
    setWithdrawAmount('');
  };

  const handleTransfer = () => {
    if (transferAmount <= balance) {
      setBalance(balance - transferAmount);
      setSuccessMessage(`Transfer of $${transferAmount} to ${transferAccount} successful!`);
      setErrorMessage('');
    } else {
      setErrorMessage('Insufficient balance for transfer');
      setSuccessMessage('');
    }
    setTransferAmount('');
    setTransferAccount('');
  };

  return (
    <div className="view-payments-container">
      <h2>View Payments and Balances</h2>
      <p>Your current balance: ${balance}</p>

      <div className="withdraw-section">
        <h3>Withdraw Balance</h3>
        <input
          type="number"
          placeholder="Enter amount"
          value={withdrawAmount}
          onChange={(e) => setWithdrawAmount(e.target.value)}
        />
        <button onClick={handleWithdraw}>Withdraw</button>
        {errorMessage && <p className="error-message">{errorMessage}</p>}
        {successMessage && <p className="success-message">{successMessage}</p>}
      </div>

      <div className="transfer-section">
        <h3>Transfer Balance</h3>
        <input
          type="number"
          placeholder="Enter amount"
          value={transferAmount}
          onChange={(e) => setTransferAmount(e.target.value)}
        />
        <input
          type="text"
          placeholder="Enter account"
          value={transferAccount}
          onChange={(e) => setTransferAccount(e.target.value)}
        />
        <button onClick={handleTransfer}>Transfer</button>
        {errorMessage && <p className="error-message">{errorMessage}</p>}
        {successMessage && <p className="success-message">{successMessage}</p>}
      </div>
    </div>
  );
}

export default ViewPayments;
