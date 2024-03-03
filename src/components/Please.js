function onPyodideLoaded() {
    // Pyodide is now fully loaded and available for use
    console.log('Pyodide is loaded');
    // Now you can initialize Pyodide and perform any operations that depend on it
    // For example:
    pyodide.runPython(`
        print("Hello from Pyodide!")
    `);
}