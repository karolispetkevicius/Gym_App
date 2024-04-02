import React, { useState, useEffect } from 'react';
import CreateProgram from './CreateProgram';
import ChooseTemplate from './ChooseTemplate'; // Import the ChooseTemplate component
import ProgramDays from './ProgramDays';
import AddExercise from './AddExercise';
import DeleteExercise from './DeleteExercise';
import EditExercise from './EditExercise';
import DownloadButton from './DownloadTemplate';

function ProgramBuilder() {
    const [programId, setProgramId] = useState(null);
    const [programName, setProgramName] = useState('');
    const [update, setUpdate] = useState(false);  

    const handleProgramCreated = (id, name) => {
        setProgramId(id);
        setProgramName(name);
    };

    const handleExerciseAdded = () => {  
        setUpdate(!update);
    };

    // Define the handleTemplateSelected function here
    async function handleTemplateSelected(templateId) {
        // Make a POST request to your backend to create a new WorkoutProgram
        // object based on the selected template.
        console.log('handleTemplateSelected called')
        const response = await fetch('http://127.0.0.1:8000/programs/create_from_template', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ template_id: templateId }),
        });

        const data = await response.json();
        
        console.log('Before state update:', programId, programName);

        // Update the state with the new program's ID and name
        setProgramId(data.id);
        setProgramName(data.name);
        
        console.log('After state update:', programId, programName);
    }

    return (
        <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <div style={{ flex: 2,  marginLeft:'10px'}}>
            <h2 style={{fontSize:'22px', marginRight:'300px'}}>Create Your own workout program or select from one of our templates</h2>
                <CreateProgram onProgramCreated={handleProgramCreated} />
                <ChooseTemplate onTemplateSelected={handleTemplateSelected} /> 
                {programId && (
                    <div>
                        <div style={{ marginBottom: '48px' }}>
                            <h2>Choose day and add exercises</h2>
                            <AddExercise programId={programId} onExerciseAdded={handleExerciseAdded} />
                        </div>
                        <div>
                            <h2>Download Your free Excel Template </h2>
                        </div>
                            <DownloadButton programId={programId} />
                    </div>
            
                )}
            </div>
            <div style={{ flex: 2, fontSize:'24px', marginBottom:'12px'}}>
                <h2>Program: {programName}</h2>
                    <div style={{ marginBottom: '30px',  fontSize: '14px' }} >
                        Click on days to expand
                    </div>
                    {programId && (
                        <ProgramDays programId={programId} key={update} /> 
                    )}
                </div>
            </div>
        );
}

export default ProgramBuilder;


