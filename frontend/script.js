const ws = new WebSocket("ws://localhost:2000");

const messageFormEl = document.getElementById("message-form");
const messageTextEl =  document.getElementById("message-text");
const sendButtonEl =  document.getElementById("send-button");
const messageWrapper = document.getElementById("message-wrapper");

ws.onopen = () => {
    console.log("Connected to the server");
};

ws.onmessage = (event) => {
    addMessage(event.data, "left");
};

ws.onclose = () => {
    console.log("Connection closed");
    addMessage("Connection Closed", "special");
    messageTextEl.disabled = true;
    sendButtonEl.disabled = true;
};

ws.onerror = (error) => {
    console.error("WebSocket error:", error);
    addMessage("WebSocket error occurred", "special");
    messageTextEl.disabled = true;
    sendButtonEl.disabled = true;
};

function addMessage(message, bubbleClass) {
    const messageEl = document.createElement("div");
    messageEl.classList.add("message", bubbleClass)
    const messageInnerEl = document.createElement("div");
    messageInnerEl.textContent = message;
    messageEl.appendChild(messageInnerEl);
    messageWrapper.appendChild(messageEl);
    messageWrapper.scrollTop = messageWrapper.scrollHeight;
}

messageFormEl.addEventListener("submit", (event) => {
    event.preventDefault();

    const message = messageTextEl.value;

    if (message) {
        if(message == "clear") {
            messageWrapper.innerHTML = "";
            messageTextEl.value = "";
            return;
        }

        addMessage(message, "right");

        ws.send(message);
        messageTextEl.value = "";
    }
});