import React, { useState, useEffect } from 'react';
import CreateProgram from './CreateProgram';
import AddDay from './AddDay';
import AddExercise from './AddExercise';

function ProgramBuilder() {
    const [programId, setProgramId] = useState(null);
    const [programName, setProgramName] = useState('');
    const [days, setDays] = useState([]);
  
    const handleProgramCreated = (id, name) => {
      setProgramId(id);
      setProgramName(name);
    };
  
    const handleDayAdded = (day) => {
      setDays([...days, day]);
    };
  
    return (
      <div>
        <CreateProgram onProgramCreated={handleProgramCreated} />
        {programId && <h2>Program: {programName}</h2>}
        {programId && <AddDay programId={programId} onDayAdded={handleDayAdded} />}
        {days.map((day) => (
          <div key={day.id}>
            <h3>{day.name}</h3>
            {day.exercises.map((exercise) => (
              <p key={exercise.id}>{exercise.name}</p>
            ))}
          </div>
        ))}
      </div>
    );
  }
  
export default ProgramBuilder;