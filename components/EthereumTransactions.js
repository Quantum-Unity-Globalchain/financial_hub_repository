import React, { useState } from 'react';
import { ethers } from 'ethers';
import { Button, Form, FormGroup, Label, Input, Alert } from 'react-bootstrap';
import blockchainService from '../services/blockchainService';

const EthereumTransactions = () => {
  const [transactionHash, setTransactionHash] = useState('');
  const [error, setError] = useState('');
  const [amount, setAmount] = useState('');
  const [recipient, setRecipient] = useState('');

  const handleTransaction = async (e) => {
    e.preventDefault();
    setError('');
    setTransactionHash('');

    try {
      const provider = blockchainService.getProvider();
      const signer = provider.getSigner();
      const tx = await signer.sendTransaction({
        to: recipient,
        value: ethers.utils.parseEther(amount),
      });
      setTransactionHash(tx.hash);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <h2>Ethereum Transactions</h2>
      <Form onSubmit={handleTransaction}>
        <FormGroup>
          <Label for="recipient">Recipient Address</Label>
          <Input
            type="text"
            name="recipient"
            id="recipient"
            placeholder="Enter recipient address"
            value={recipient}
            onChange={(e) => setRecipient(e.target.value)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="amount">Amount (ETH)</Label>
          <Input
            type="text"
            name="amount"
            id="amount"
            placeholder="Enter amount in ETH"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
          />
        </FormGroup>
        <Button type="submit" color="primary">Send Transaction</Button>
      </Form>
      {transactionHash && <Alert color="success">Transaction successful! Hash: {transactionHash}</Alert>}
      {error && <Alert color="danger">Error: {error}</Alert>}
    </div>
  );
};

export default EthereumTransactions;
