import React, { useState, useEffect } from 'react';
import { apiService } from '../services/apiService';

const AccountDisplay = () => {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    const fetchAccounts = async () => {
      try {
        const response = await apiService.get('/accounts');
        setAccounts(response.data);
      } catch (error) {
        console.error('Error fetching accounts:', error);
      }
    };

    fetchAccounts();
  }, []);

  return (
    <div className="account-display">
      <h2>Accounts</h2>
      {accounts.length > 0 ? (
        <ul>
          {accounts.map((account) => (
            <li key={account.id}>
              <div>
                <strong>Account Name:</strong> {account.name}
              </div>
              <div>
                <strong>Balance:</strong> {account.balance}
              </div>
            </li>
          ))}
        </ul>
      ) : (
        <p>No accounts found.</p>
      )}
    </div>
  );
};

export default AccountDisplay;
