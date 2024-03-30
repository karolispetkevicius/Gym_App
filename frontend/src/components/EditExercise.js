import React, { useState } from 'react';

import '../styling/SmallButtons.css';

function EditExercise({ exercise, onExerciseEdited }) {
    console.log(exercise);
    const [sets, setSets] = useState(exercise.sets);
    const [reps, setReps] = useState(exercise.reps);
    const [isEditing, setIsEditing] = useState(false);

    const handleEdit = async () => {
        const requestBody = {
            sets,
            reps,
            program_day: exercise.program_day,
            exercise: exercise.exercise_id,
        };
    
        console.log(requestBody);  // Print the request body
    
        const response = await fetch(`http://127.0.0.1:8000/exercises/${exercise.id}/edit/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestBody),
        });

        if (response.ok) {
            const updatedExercise = await response.json();
            onExerciseEdited(updatedExercise);
            setIsEditing(false);  // Close the form after editing
        } else {
            console.error('Failed to edit exercise');
        }
    };

    return (
        <div>
            {isEditing ? (
                <div>
                    <label>
                        Sets:
                        <input type="number" min="1" value={sets} onChange={(e) => setSets(e.target.value)} />
                    </label>
                    <label>
                        Reps:
                        <input type="number" min="1" value={reps} onChange={(e) => setReps(e.target.value)} />
                    </label>
                    <button onClick={handleEdit} className="small-button">Save</button>
                    <button onClick={() => setIsEditing(false)} className="small-button" >Cancel</button>
                </div>
            ) : (
                <button onClick={() => setIsEditing(true)} className="small-button">Edit</button>
            )}
        </div>
    );
}

export default EditExercise;