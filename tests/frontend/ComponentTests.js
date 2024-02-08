import React from 'react';
import { render, screen, cleanup } from '@testing-library/react';
import '@testing-library/jest-dom';
import AccountDisplay from '../components/AccountDisplay';
import TransactionInitiation from '../components/TransactionInitiation';
import WalletManagement from '../components/WalletManagement';
import EthereumTransactions from '../components/EthereumTransactions';
import WalletConnector from '../components/WalletConnector';

afterEach(cleanup);

describe('Component Rendering Tests', () => {
  test('AccountDisplay component renders correctly', () => {
    render(<AccountDisplay />);
    expect(screen.getByText(/Account Details/i)).toBeInTheDocument();
  });

  test('TransactionInitiation component renders correctly', () => {
    render(<TransactionInitiation />);
    expect(screen.getByText(/Initiate Transaction/i)).toBeInTheDocument();
  });

  test('WalletManagement component renders correctly', () => {
    render(<WalletManagement />);
    expect(screen.getByText(/Manage Your Wallets/i)).toBeInTheDocument();
  });

  test('EthereumTransactions component renders correctly', () => {
    render(<EthereumTransactions />);
    expect(screen.getByText(/Ethereum Transactions/i)).toBeInTheDocument();
  });

  test('WalletConnector component renders correctly', () => {
    render(<WalletConnector />);
    expect(screen.getByText(/Connect Your Wallet/i)).toBeInTheDocument();
  });
});
