import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { Button, Alert } from 'react-bootstrap';

const WalletConnector = () => {
  const [currentAccount, setCurrentAccount] = useState(null);
  const [errorMessage, setErrorMessage] = useState('');

  // Check if MetaMask is installed
  useEffect(() => {
    if (!window.ethereum) {
      setErrorMessage('MetaMask is not installed. Please install it to use this feature.');
    }
  }, []);

  // Function to connect to MetaMask
  const connectWalletHandler = async () => {
    if (window.ethereum) {
      try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected', accounts[0]);
        setCurrentAccount(accounts[0]);
      } catch (err) {
        setErrorMessage('Failed to connect wallet. ' + err.message);
      }
    } else {
      setErrorMessage('MetaMask is not installed. Please install it to use this feature.');
    }
  };

  return (
    <div>
      {errorMessage && <Alert variant="danger">{errorMessage}</Alert>}
      {!currentAccount && (
        <Button onClick={connectWalletHandler}>Connect Wallet</Button>
      )}
      {currentAccount && (
        <div>
          <Alert variant="success">Connected with: {currentAccount}</Alert>
        </div>
      )}
    </div>
  );
};

export default WalletConnector;
