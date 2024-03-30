import React from 'react';

import '../styling/SmallButtons.css';

function DeleteExercise({ exerciseId, onExerciseDeleted }) {
    const handleDelete = async () => {
        const response = await fetch(`http://127.0.0.1:8000/exercises/${exerciseId}/delete/`, { method: 'DELETE' });
        if (response.ok) {
            onExerciseDeleted(exerciseId);
        } else {
            console.error('Failed to delete exercise');
        }
    };

    return (
        <button onClick={handleDelete} className="small-button">Delete</button>
    );
}

export default DeleteExercise;

