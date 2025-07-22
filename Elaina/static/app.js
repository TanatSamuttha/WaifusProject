const chatbox = document.getElementById("chatbox");

function appendMessage(sender, message) {
    const div = document.createElement("div");
    div.className = "msg " + (sender === "You" ? "user" : "elaina");
    div.textContent = `${sender}: ${message}`;
    chatbox.appendChild(div);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function emotionalImg(emotional) {
    const img = document.getElementById("img");
    img.src = `EmotionalImg/${emotional}.png`;
}

async function sendMessage() {
    const input = document.getElementById("messageInput");
    const message = input.value.trim();
    const session = document.getElementById("session");
    const session_id = session.value.trim();
    if (!message) return;

    appendMessage("You", message);
    appendMessage("Elaina", "Typing...");
    input.value = "";

    const response = await fetch("/chat/Elaina", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id, message })
    });

    const data = await response.json();
    chatbox.removeChild(chatbox.lastChild); // remove "Typing..."
    appendMessage("Elaina", data.response);
    emotionalImg(data.emotional);
}
