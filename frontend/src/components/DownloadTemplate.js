import axios from 'axios';

function DownloadButton({ programId }) {
    const handleDownload = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/programbuilder/generate/${programId}`, {
                responseType: 'blob', // important
            });

            // Create a blob from the response for download
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'program.xlsx'); 
            document.body.appendChild(link);
            link.click();
        } catch (error) {
            console.error('Error downloading file:', error);
        }
    };

    return <button onClick={handleDownload} className="add-exercise-button">Download Program</button>;
}

export default DownloadButton;
