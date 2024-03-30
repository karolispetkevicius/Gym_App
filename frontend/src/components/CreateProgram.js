import React, { useState } from 'react';

import '../styling/CreateProgram.css';

function CreateProgram({ onProgramCreated }) {
    const [programName, setProgramName] = useState('');
  
    const handleSubmit = async (event) => {
      event.preventDefault();
  
      const response = await fetch('http://127.0.0.1:8000/programs/create/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: programName }),
      });
  
      const data = await response.json();
      onProgramCreated(data.id, programName);
    };
  
    return (
      <form onSubmit={handleSubmit} className="create-program">
        <input
          type="text"
          value={programName}
          onChange={(e) => setProgramName(e.target.value)}
        />
        <button type="submit">Create New Program</button>
      </form>
    );
}

export default CreateProgram;
