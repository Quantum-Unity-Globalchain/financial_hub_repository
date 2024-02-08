import React, { useState } from 'react';
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';

const TransactionInitiation = () => {
  const [transactionDetails, setTransactionDetails] = useState({
    fromAccount: '',
    toAccount: '',
    amount: '',
    currency: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setTransactionDetails({
      ...transactionDetails,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you would typically handle the submission to the backend
    console.log('Transaction Details: ', transactionDetails);
    alert('Transaction initiated!');
  };

  return (
    <div className="transaction-initiation">
      <h2>Initiate Transaction</h2>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label for="fromAccount">From Account</Label>
          <Input
            type="text"
            name="fromAccount"
            id="fromAccount"
            placeholder="Enter sender's account ID"
            value={transactionDetails.fromAccount}
            onChange={handleChange}
          />
        </FormGroup>
        <FormGroup>
          <Label for="toAccount">To Account</Label>
          <Input
            type="text"
            name="toAccount"
            id="toAccount"
            placeholder="Enter recipient's account ID"
            value={transactionDetails.toAccount}
            onChange={handleChange}
          />
        </FormGroup>
        <FormGroup>
          <Label for="amount">Amount</Label>
          <Input
            type="number"
            name="amount"
            id="amount"
            placeholder="Enter amount"
            value={transactionDetails.amount}
            onChange={handleChange}
          />
        </FormGroup>
        <FormGroup>
          <Label for="currency">Currency</Label>
          <Input
            type="text"
            name="currency"
            id="currency"
            placeholder="Enter currency (e.g., USD)"
            value={transactionDetails.currency}
            onChange={handleChange}
          />
        </FormGroup>
        <Button type="submit" color="primary">Initiate Transaction</Button>
      </Form>
    </div>
  );
};

export default TransactionInitiation;
