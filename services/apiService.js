import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api'; // Adjust this URL to your Django backend's deployed URL

// Setting up the default headers for all requests
axios.defaults.headers.common['Content-Type'] = 'application/json';

const getAuthHeader = (token) => {
  return { headers: { Authorization: `Bearer ${token}` } };
};

const apiService = {
  // User Authentication
  login: async (email, password) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/login/`, { email, password });
      return response.data;
    } catch (error) {
      console.error('Login Error:', error.response || error);
      throw error;
    }
  },

  register: async (userData) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/register/`, userData);
      return response.data;
    } catch (error) {
      console.error('Registration Error:', error.response || error);
      throw error;
    }
  },

  // Account Management
  fetchAccounts: async (token) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/accounts/`, getAuthHeader(token));
      return response.data;
    } catch (error) {
      console.error('Fetch Accounts Error:', error.response || error);
      throw error;
    }
  },

  // Transaction Processing
  initiateTransaction: async (transactionData, token) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/transactions/`, transactionData, getAuthHeader(token));
      return response.data;
    } catch (error) {
      console.error('Transaction Error:', error.response || error);
      throw error;
    }
  },

  // Wallet and Blockchain Operations
  fetchWalletInfo: async (token) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/wallets/`, getAuthHeader(token));
      return response.data;
    } catch (error) {
      console.error('Fetch Wallet Info Error:', error.response || error);
      throw error;
    }
  },

  executeEthereumTransaction: async (transactionData, token) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/ethereum-transactions/`, transactionData, getAuthHeader(token));
      return response.data;
    } catch (error) {
      console.error('Ethereum Transaction Error:', error.response || error);
      throw error;
    }
  },

  // Add more API calls as needed
};

export default apiService;
