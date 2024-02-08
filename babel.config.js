module.exports = {
  // Your existing Babel config here (if any)
  
  // Jest configuration
  jest: {
    transform: {
      "^.+\\.[t|j]sx?$": "babel-jest"
    },
    moduleNameMapper: {
      "\\.(css|less|sass|scss)$": "identity-obj-proxy"
    },
    setupFilesAfterEnv: ["<rootDir>/src/setupTests.js"]
  },

  // Other configurations or scripts
  scripts: {
    test: "jest --all"
  }
};
