const ws = new WebSocket('ws://localhost:2000');

const messageFormEl = document.getElementById("message-form");
const messageTextEl =  document.getElementById("message-text");
const messageWrapper = document.getElementById("message-wrapper");

ws.onopen = () => {
    console.log('Connected to the server');
};

ws.onmessage = (event) => {
    addMessage(event.data, 'left')
};

function addMessage(message, bubbleClass) {
    const messageEl = document.createElement('div');
    messageEl.classList.add('message', bubbleClass)
    const messageInnerEl = document.createElement('div');
    messageInnerEl.textContent = message;
    messageEl.appendChild(messageInnerEl);
    messageWrapper.appendChild(messageEl);
    messageWrapper.scrollTop = messageWrapper.scrollHeight;
}


messageFormEl.addEventListener('submit', (event) => {
    event.preventDefault();

    const message = messageTextEl.value;

    if (message) {
        addMessage(message, 'right')

        ws.send(message);
        messageTextEl.value = '';
    }
});