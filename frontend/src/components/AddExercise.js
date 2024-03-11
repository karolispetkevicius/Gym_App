import React, { useState, useEffect } from 'react';

function AddExercise({ dayId }) {
  const [exercise, setExercise] = useState('');
  const [sets, setSets] = useState(0);
  const [reps, setReps] = useState(0);
  const [exercises, setExercises] = useState([]);

  useEffect(() => {
    const fetchExercises = async () => {
      const response = await fetch('http://127.0.0.1:8000/exercises/');
      const data = await response.json();
      setExercises(data);
    };

    fetchExercises();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await fetch(`http://127.0.0.1:8000/days/${dayId}/add_exercise/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ program_day: dayId, exercise, sets, reps }),
    });

    const data = await response.json();
    // Now you can use data to update your state
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Select Exercise</label>
      <select value={exercise} onChange={(e) => setExercise(e.target.value)}>
        {exercises.map((exercise) => (
          <option key={exercise.id} value={exercise.id}>
            {exercise.exercise}
          </option>
        ))}
      </select>
      </div>
      <div>
        <label>Number of Sets:</label>
            <input
            type="number"
            value={sets}
            onChange={(e) => setSets(e.target.value)}
        />
      </div>
      <div>
      <label>Number of Reps:</label>
      <input
        type="number"
        value={reps}
        onChange={(e) => setReps(e.target.value)}
      />
      </div>
      <button type="submit">Add Exercise</button>
    </form>
  );
}

export default AddExercise;