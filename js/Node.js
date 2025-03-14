const express = require('express');
const app = express();
const port = 3000;

app.use(express.json()); // To parse JSON bodies

app.post('/api/checkID', (req, res) => {
    const { userId, serverId } = req.body;

    // Simulate a response (replace with actual server logic)
    if (userId && serverId) {
        // Here, you'd fetch account data from the MLBB server or a database
        res.json({ success: true });
    } else {
        res.json({ success: false, message: 'Invalid ID or Server.' });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
