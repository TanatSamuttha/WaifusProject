const chatbox = document.getElementById("chatbox");

function appendMessage(sender, message) {
    const div = document.createElement("div");
    div.className = "msg " + sender;
    div.textContent = `sender: ${message}`;
    chatbox.appendChild(div);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function emotionalImg(emotional){
    const img = document.getElementById("img");
    img.src = `EmotionalImg/${emotional}.png`
}

async function sendMessage() {
    const input = document.getElementById("messageInput");
    const message = input.value.trim();
    const session = document.getElementById("session");
    const session_id = session.value.trim();
    if (!message) return;

    appendMessage("You", message);
    appendMessage("Elaina", "Typping...");
    input.value = "";

    const response = await fetch("/chat/Elaina", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
        body: JSON.stringify({session_id, message})
    });

    const data = await response.json();
    chatbox.removeChild(chatbox.lastChild);
    appendMessage("Elaina", data.response + ` (${data.emotional})`);
    emotionalImg(data.emotional)
}