import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import AccountDisplay from './components/AccountDisplay';
import TransactionInitiation from './components/TransactionInitiation';
import WalletManagement from './components/WalletManagement';
import EthereumTransactions from './components/EthereumTransactions';
import WalletConnector from './components/WalletConnector';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/accounts" exact component={AccountDisplay} />
          <Route path="/transactions" exact component={TransactionInitiation} />
          <Route path="/wallets" exact component={WalletManagement} />
          <Route path="/ethereum-transactions" exact component={EthereumTransactions} />
          <Route path="/connect-wallet" exact component={WalletConnector} />
          {/* You can add more routes here as needed */}
          <Route path="/" render={() => <div>Welcome to the Financial Hub Integration Platform</div>} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
