import React, { useState, useEffect } from 'react';

import '../styling/AddExercise.css';

function AddExercise({ programId, onExerciseAdded }) {
    const [day, setDay] = useState('Monday');
    const [exerciseId, setExerciseId] = useState('');
    const [exerciseName, setExerciseName] = useState('');
    const [sets, setSets] = useState(1);
    const [reps, setReps] = useState(1);
    const [exercises, setExercises] = useState([]);
    const [isRestDay, setIsRestDay] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        const fetchExercises = async () => {
            const response = await fetch('http://127.0.0.1:8000/exercises/');
            const data = await response.json();
            setExercises(data);
        };

        fetchExercises();
    }, []);

    const handleExerciseChange = (e) => {
        const selectedExerciseId = Number(e.target.value);
        const selectedExercise = exercises.find(exercise => exercise.id === selectedExerciseId);
        setExerciseId(selectedExercise.id);
        setExerciseName(selectedExercise.exercise);
    };

    const handleUnsetRestDay = async () => {
        const response = await fetch(`http://127.0.0.1:8000/programs/${programId}/days/${day}/notrest`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ day_of_week: day }),
        });

        if (response.ok) {
            alert('Rest day unset successfully');
            setIsRestDay(false);
        } else {
            alert('Failed to unset rest day');
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (isRestDay) {
            const response = await fetch(`http://127.0.0.1:8000/programs/${programId}/days/${day}/rest`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ day_of_week: day }),
            });

            if (response.ok) {
                alert('Rest day set successfully');
            } else {
                alert('Failed to set rest day');
            }
        } else {
            const response = await fetch(`http://127.0.0.1:8000/programs/${programId}/days/${day}/exercises/add/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ exercise: exerciseId, sets, reps }),
            });

            const data = await response.json();
            onExerciseAdded(day, { ...data, exercise: exerciseName });
        }
    };

    return (
        <form onSubmit={handleSubmit}>
        <div style={{ display: 'flex', marginBottom: '20px' }}>
            <label>
                Day:
                <select value={day} onChange={(e) => setDay(e.target.value)}>
                    <option value="Monday">Monday</option>
                    <option value="Tuesday">Tuesday</option>
                    <option value="Wednesday">Wednesday</option>
                    <option value="Thursday">Thursday</option>
                    <option value="Friday">Friday</option>
                    <option value="Saturday">Saturday</option>
                    <option value="Sunday">Sunday</option>
                </select>
            </label>
            <label>
                Rest Day:
                <input type="checkbox" checked={isRestDay} onChange={(e) => setIsRestDay(e.target.checked)} /> 
            </label>
        </div>
        {!isRestDay && (
            <>
            <div style={{ display: 'flex', marginBottom: '20px' }}>
                <label>
                    Exercise:
                    <input type="text" placeholder="Search..." value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} />
                    <select value={exerciseId} onChange={handleExerciseChange}>
                        {exercises.filter(exercise => exercise.exercise.toLowerCase().includes(searchTerm.toLowerCase())).map((exercise) => (
                            <option key={exercise.id} value={exercise.id}>
                                {exercise.exercise}
                            </option>
                        ))}
                    </select>
                </label>
                </div>
                <div style={{ display: 'flex', marginBottom: '20px' }}>
                    <label>
                        Sets:
                        <input type="number" min="1" value={sets} onChange={(e) => setSets(e.target.value)} />
                    </label>
                    <label>
                        Reps:
                        <input type="number" min="1" value={reps} onChange={(e) => setReps(e.target.value)} />
                    </label>
                    </div>
                </>
                
        )}
        {isRestDay && (
            <button type="button" onClick={handleUnsetRestDay}>Unset Rest Day</button>
        )}
        <button type="submit" className="add-exercise-button">{isRestDay ? 'Set Rest Day' : 'Add Exercise'}</button>
    </form>
        );
    }

export default AddExercise;



