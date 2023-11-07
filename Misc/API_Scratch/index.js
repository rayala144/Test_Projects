const express = require('express'); // Initiating middleware
const app = express();
const PORT = 8080;

app.use(express.json()) // Using middleware to parse JSON before the data hits the function

app.get('/tshirt', (req, res) => {
    res.status(200).send({
        tshirt: '👚',
        size: 'large'
    })
});

app.post('/tshirt/:id', (req, res) => {
    const { id } = req.params; // Given in the URL
    const { logo } = req.body; // Given as body POST request

    if (!logo) {
        res.status(418).send({
            message: "We need a logo!!!"
        })
    }

    res.send({
        tshirt: `👚 with your ${logo} and ID: ${id}`,
    })



});

app.listen(
    PORT,
    () => console.log(`It's active on http://localhost:${PORT}`)
);