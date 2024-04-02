import React, { useState, useEffect } from 'react';
import DeleteExercise from './DeleteExercise';
import EditExercise from './EditExercise';
import Collapsible from 'react-collapsible'

function ProgramDays({ programId }) {
    const [programDays, setProgramDays] = useState([]);

    const onExerciseDeleted = (exerciseId) => {
        setProgramDays(programDays.map(day => ({
            ...day,
            exercises: day.exercises.filter(exercise => exercise.id !== exerciseId)
        })));
    };

    const onExerciseEdited = (updatedExercise) => {
        setProgramDays(programDays.map(day => ({
            ...day,
            exercises: day.exercises.map(exercise => 
                exercise.id === updatedExercise.id ? updatedExercise : exercise
            )
        })));
    };

    useEffect(() => {
        const fetchProgramDays = async () => {
            const response = await fetch(`http://127.0.0.1:8000/programs/${programId}/days/`);
            const data = await response.json();
            setProgramDays(data.program_days);
            console.log(data)
        };

        fetchProgramDays();
    }, [programId]);

    return (
        <div>
            {programDays.map((day) => {
                // Create a list of unique body parts for the day
                const bodyParts = [...new Set(day.exercises.map(exercise => exercise.body_part))];

                return (
                    <div key={day.id} style={{ marginBottom: '22px',  }}>
                        <Collapsible trigger={
            <>
                    <h3 style={{ fontWeight: 'bold', display: 'inline', marginRight: '11px', fontSize: '32px' }}>
                    {day.day_of_week}
                </h3> 
                <span style={{ fontSize: '14px' }}>{bodyParts.join('/')}</span>
                        </>
                    }>
                            {day.rest_day ? (
                                <p>Rest Day</p>
                            ) : (
                                day.exercises.map((exercise, index) => (
                                    <div key={exercise.id} style={{ display: 'flex', alignItems: 'center', fontSize:'18px',marginRight:'5px' }}>
                                        <p>
                                        <span style={{ fontSize: '20px', fontWeight: 'bold' }}>{index + 1}. {exercise.exercise_name}</span>
                                            {' '}
                                        {exercise.sets} sets {exercise.reps} reps
                                        </p>
                                        <div style={{ display: 'flex', marginBottom: '4px', marginLeft: '10px' }}>
                                            <EditExercise exercise={exercise} onExerciseEdited={onExerciseEdited} />
                                        </div>
                                        <div style={{ display: 'flex'}}>
                                            <DeleteExercise exerciseId={exercise.id} onExerciseDeleted={onExerciseDeleted} />
                                        </div>
                                    </div>
                                ))
                            )}
                        </Collapsible>
                        <hr />
                    </div>
                );
            })}
        </div>
    );
}

export default ProgramDays;
