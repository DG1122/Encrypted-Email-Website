function toggleCompose() {
    const composeArea = document.getElementById('composeArea');
    composeArea.classList.toggle('hidden');
}

function sendMessage() {
    alert('Message Sent!');
    toggleCompose();
}
