const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process');
const app = express();
const port = 3000;

app.use(cors());

// Set up a route for file uploads
app.post('/upload', (req, res) => {
  const file = req.body.file;

  // Aquí se debe llamar al script predict.py y pasarle el archivo
  const pythonProcess = spawn('python', ['predict.py', file]);

  pythonProcess.stdout.on('data', (data) => {
    // Enviar el resultado de la predicción como respuesta al cliente
    res.json({ prediction_result: data.toString() });
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});