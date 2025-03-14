// Function to send data to the backend server
function saveData() {
    const userId = document.getElementById('userId').value;
    const serverId = document.getElementById('serverId').value;

    if (!userId || !serverId) {
        document.getElementById('response').innerText = 'Please fill in all fields.';
        return;
    }

    // Send the data to the server using a POST request
    fetch('http://localhost:3000/api/users/saveData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userId, serverId }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('response').innerText = 'Data saved successfully!';
        } else {
            document.getElementById('response').innerText = 'Error: ' + data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('response').innerText = 'An error occurred while saving data.';
    });
}
