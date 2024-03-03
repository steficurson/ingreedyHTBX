import React, { useEffect, useState } from 'react';
import match_search_terms from "../ingredients_matcher.py";

function PyodidePythonHelper (args = [] ) {
  const [result, setResult] = useState('');

  useEffect(() => {
    // Load Pyodide
       const pyodide = window.pyodide;

    // Define the arguments to be passed to the Python script

    // Execute Python code with arguments
    // pyodide.runPython(matcher,{argv:args}).then(() => {
    //   // Get the result from Python
    //   const resultFromPython = pyodide.globals.result.toJs();
    //   setResult(resultFromPython);
    // });
    console.log("IN PYTHON THING")
    const pythonCode = `

    # Call the function with the argument
    result = ${match_search_terms}(${args});

    `;

// Execute the Python code using runPython
    pyodide.runPython(pythonCode).then(() => {
    // Get the result from Python
    const resultFromPython = pyodide.globals.result.toJs();
    setResult(resultFromPython);
      }).catch(error => {
        console.error('Error executing Python code:', error);
     });

    }, []); // Empty dependency array ensures useEffect runs only once
      return (
        <div>
          <h2>Result from Python:</h2>
          console.log("IN PYTHON THING")
         <p>{result}</p>
        </div>
       );
    };

export default PyodidePythonHelper;
