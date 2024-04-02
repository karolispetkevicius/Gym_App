import React, { useState, useEffect } from 'react';

import '../styling/ChooseTemplate.css';


function ChooseTemplate({ onTemplateSelected }) {
    const [templates, setTemplates] = useState([]);
    const [selectedTemplate, setSelectedTemplate] = useState('');

    // Fetch templates when component mounts
    useEffect(() => {
        const fetchTemplates = async () => {
            const response = await fetch('http://127.0.0.1:8000/programs/templates/');
            const data = await response.json();
            setTemplates(data);
        };
        fetchTemplates();
    }, []);

  // Handle selection of a template
    const handleSelection = (event) => {
        setSelectedTemplate(event.target.value);
        console.log(`Template selected: ${event.target.value}`); // Add this line
    };

    const handleClick = () => {
        console.log('handleClick called'); // Add this line
        if (selectedTemplate) {
            console.log(`Button clicked with template: ${selectedTemplate}`);
            onTemplateSelected(selectedTemplate);
        }
    };

    return (
        <div className="choose-template-component">
            <select value={selectedTemplate} onChange={handleSelection} className="template-select">
                {templates.map((template) => (
                    <option key={template.id} value={template.id}>
                        {template.name}
                    </option>
                ))}
            </select>
            <button onClick={handleClick} className="template-button">Choose Template Program</button>
        </div>
    );
}
export default ChooseTemplate;