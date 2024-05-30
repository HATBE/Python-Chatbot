const messageFormEl = document.getElementById("message-form");
const messageTextEl =  document.getElementById("message-text");
const sendButtonEl =  document.getElementById("send-button");
const messageWrapperEl = document.getElementById("message-wrapper");

let supporter_name = "No Name";

function addLeftMessage(message) {
    const messageEl = copyTemplate('chat-message-name');
    messageEl.querySelector('.message').classList.add('left');
    messageEl.querySelector('.message-name').textContent = supporter_name;
    messageEl.querySelector('.message-text').textContent = message;
    messageWrapperEl.appendChild(messageEl)

    messageWrapperEl.scrollTop = messageWrapperEl.scrollHeight;
}

function addRightMessage(message) {
    const messageEl = copyTemplate('chat-message');
    messageEl.querySelector('.message').classList.add('right');
    messageEl.querySelector('.message-text').textContent = message;
    messageWrapperEl.appendChild(messageEl)

    messageWrapperEl.scrollTop = messageWrapperEl.scrollHeight;
}

function addSpecialMessage(message) {
    const messageEl = copyTemplate('chat-message-name');
    messageEl.querySelector('.message').classList.add('left');
    messageEl.querySelector('.message').classList.add('special');
    messageEl.querySelector('.message-name').textContent = "INFO!";
    messageEl.querySelector('.message-text').textContent = message;
    messageWrapperEl.appendChild(messageEl)

    messageWrapperEl.scrollTop = messageWrapperEl.scrollHeight;
}

function copyTemplate(templateName) {
    // deep copy html template
    return document.importNode(document.getElementById(templateName).content, true);
}

const ws = new WebSocket("ws://localhost:2000");

ws.onopen = () => {
    console.log("Connected to the server");
};

ws.onmessage = (event) => {
    // when the connection starts
    try {
        message = JSON.parse(event.data);
    } catch(error) {
        console.log(error);
        message = event.data;
    }   

    if(message.type == "init") {
        // handle the init package that is sent on chat initioation
        supporter_name = message.supporter_name;
    } else if(message.type == "message") {
        // messages from server
        addLeftMessage(message.text);
    } else {
        // default edge case
        addLeftMessage(message);
    }  
};

ws.onclose = () => {
    // when the connection closes
    console.log("Connection closed");
    addSpecialMessage("Connection Closed");
    messageTextEl.disabled = true;
    sendButtonEl.disabled = true;
};

ws.onerror = (error) => {
    // when the connection has an error
    console.error("WebSocket error:", error);
    addSpecialMessage("WebSocket error occurred");
    messageTextEl.disabled = true;
    sendButtonEl.disabled = true;
};

messageFormEl.addEventListener("submit", (event) => {
    // when the user sends the messasge
    event.preventDefault();

    const message = messageTextEl.value;

    if (message) {
        addRightMessage(message);

        ws.send(message);
        messageTextEl.value = "";
        messageTextEl.focus
    }
});

startWebsocket();