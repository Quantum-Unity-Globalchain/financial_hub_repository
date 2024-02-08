import { ethers } from 'ethers';

const blockchainService = {
  // Function to connect to Ethereum network and get the provider
  getProvider: () => {
    // Using ethers to connect to the default provider (homestead/mainnet)
    const provider = ethers.getDefaultProvider();
    return provider;
  },

  // Function to create a new Ethereum wallet
  createWallet: () => {
    const wallet = ethers.Wallet.createRandom();
    return {
      address: wallet.address,
      privateKey: wallet.privateKey,
    };
  },

  // Function to load an Ethereum wallet using a private key
  loadWallet: (privateKey) => {
    try {
      const wallet = new ethers.Wallet(privateKey);
      return {
        address: wallet.address,
        privateKey: wallet.privateKey,
      };
    } catch (error) {
      console.error('Error loading wallet:', error);
      throw error;
    }
  },

  // Function to send ETH from one wallet to another
  sendETH: async (senderPrivateKey, recipientAddress, amount) => {
    try {
      const provider = blockchainService.getProvider();
      const senderWallet = new ethers.Wallet(senderPrivateKey, provider);
      const transaction = await senderWallet.sendTransaction({
        to: recipientAddress,
        value: ethers.utils.parseEther(amount.toString()),
      });
      return transaction;
    } catch (error) {
      console.error('Error sending ETH:', error);
      throw error;
    }
  },

  // Function to interact with a smart contract
  interactWithContract: async (walletPrivateKey, contractAddress, abi, methodName, methodParams) => {
    try {
      const provider = blockchainService.getProvider();
      const wallet = new ethers.Wallet(walletPrivateKey, provider);
      const contract = new ethers.Contract(contractAddress, abi, wallet);
      const transaction = await contract[methodName](...methodParams);
      return transaction;
    } catch (error) {
      console.error('Error interacting with contract:', error);
      throw error;
    }
  },
};

export default blockchainService;
