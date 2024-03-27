const inputField = document.getElementById('input-code');
const outputField = document.getElementById('output-code');
const generateButton = document.getElementById('generate');

window.onload = () => {
    inputField.value = '';
    outputField.value = '';
};

generateButton.addEventListener('click', () => {
    const inputValue = inputField.value;
    // Send a POST request to the Flask backend with the input code
    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: inputValue })
    })
    .then(response => response.json())
    .then(data => outputField.value = data.outputCode)
    .catch(error => console.error('Error:', error));
});
