const express = require('express');
const app = express();
const port = 3000;

// Serve static files from the "public" directory
app.use(express.static('public'));

// Define a route for the home page
app.get('/', (req, res) => {
  res.send('Hello, World! Your server is running.');
});


app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
  console.log("Hello, World! Your Node.js server is running.");
  console.log("Hello, World!");

});

