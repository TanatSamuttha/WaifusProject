const chatbox = document.getElementById("chatbox");

function appendMessage(sender, message) {
    const div = document.createElement("div");
    div.className = "msg " + sender;
    div.textContent = `${sender === 'user' ? 'You' : 'Elaina'}: ${message}`;
    chatbox.appendChild(div);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function emotionalImg(emotional){
    const img = document.getElementById("img");
    switch (emotional) {
        case "Blushing":
            img.src = "EmotionalImg/Blushing.png";
            break;
        case "Annoyed":
            img.src = "EmotionalImg/Annoyed.png";
            break;
        case "Bored":
            img.src = "EmotionalImg/Bored.png";
            break;
        case "Playful":
            img.src = "EmotionalImg/Playful.png";
            break;
        case "Embarrassed":
            img.src = "EmotionalImg/Embarrassed.png"
            break;
        default:
            img.src = "EmotionalImg/Normal.png"; // fallback
    }
}

async function sendMessage() {
    const input = document.getElementById("messageInput");
    const message = input.value.trim();
    const session = document.getElementById("session");
    const session_id = session.value.trim();
    if (!message) return;

    appendMessage("user", message);
    appendMessage("elaina", "Typping...");
    input.value = "";

    const response = await fetch("/chat/Elaina", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
        body: JSON.stringify({session_id, message})
    });

    const data = await response.json();
    chatbox.removeChild(chatbox.lastChild);
    appendMessage("elaina", data.response + ` (${data.emotional})`);
    emotionalImg(data.emotional)
}