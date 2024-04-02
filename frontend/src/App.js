import React from 'react';
import ProgramBuilder from './components/ProgramBuilder';
import './App.css';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        Gym Program Builder
      </header>
        <body>
          <ProgramBuilder />
        </body>
      <footer className="App-footer">
        2024. Made using Django and React
      </footer>
    </div>
  );
}

export default App;