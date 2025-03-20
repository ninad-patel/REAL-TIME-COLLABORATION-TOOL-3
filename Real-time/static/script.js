// Establish WebSocket connection
const socket = io.connect('http://' + document.domain + ':' + location.port);

// Get the text editor element
const editor = document.getElementById('editor');

// Listen for real-time updates from the server
socket.on('text_update', function(data) {
    // Update the editor with the new content
    editor.value = data.text;
});

// Handle text input and send updates to the server
editor.addEventListener('input', function() {
    const text = editor.value;

    // Emit the updated text to the server
    socket.emit('update_text', { text: text });
});
