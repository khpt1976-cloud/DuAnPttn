import React from 'react';
import Header from './components/Header';
import ProductGrid from './components/ProductGrid';
import Footer from './components/Footer';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header />
      <ProductGrid />
      <Footer />
    </div>
  );
}

export default App;
