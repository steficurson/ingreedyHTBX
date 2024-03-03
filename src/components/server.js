const express = require('express');
const fs = require('fs');
const csvParser = require('csv-parser');

const app = express();
const port = 3001;

app.get('/read-csv', (req, res) => {
  const results = [];

  fs.createReadStream('path/to/your/csv/file.csv')
    .pipe(csvParser())
    .on('data', (data) => results.push(data))
    .on('end', () => {
      res.json(results);
    });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});