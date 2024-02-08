// setupTests.js
// This file is intentionally left empty for Jest setup.
import '@testing-library/jest-dom/extend-expect';

// Optional: Add global configurations or mocks here
// For example, to mock a localStorage API
const localStorageMock = (function() {
  let store = {};
  return {
    getItem: function(key) {
      return store[key] || null;
    },
    setItem: function(key, value) {
      store[key] = value.toString();
    },
    clear: function() {
      store = {};
    },
    removeItem: function(key) {
      delete store[key];
    }
  };
})();

Object.defineProperty(window, 'localStorage', { value: localStorageMock });

// If using fetch API in your application, you might need to mock it globally
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({}),
  })
);
