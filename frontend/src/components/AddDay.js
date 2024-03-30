import React, { useState } from 'react';
import AddExercise from './AddExercise';

function AddDay({ programId }) {
  const [dayOfWeek, setDayOfWeek] = useState('Monday');
  const [isRestDay, setIsRestDay] = useState(false);
  const [dayId, setDayId] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await fetch(`http://127.0.0.1:8000/programs/${programId}/add_day/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ day_of_week: dayOfWeek, rest_day: isRestDay }),
    });

    const data = await response.json();
    setDayId(data.id); // Update the day ID state with the ID of the new day
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <select value={dayOfWeek} onChange={(e) => setDayOfWeek(e.target.value)}>
          <option value="Monday">Monday</option>
          <option value="Tuesday">Tuesday</option>
          <option value="Wednesday">Wednesday</option>
          <option value="Thursday">Thursday</option>
          <option value="Friday">Friday</option>
          <option value="Saturday">Saturday</option>
          <option value="Sunday">Sunday</option>
        </select>
        <div>
            <span>Rest Day</span>
        <input
        type="checkbox"
        checked={isRestDay}
        onChange={(e) => setIsRestDay(e.target.checked)}
        />
        </div>
        <button type="submit">Select Day</button>
      </form>
      {dayId && <AddExercise dayId={dayId} />}
    </div>
  );
}

export default AddDay;
