
const chatForm = document.querySelector("#chatForm");
const chatInput = document.querySelector("#chatInput");
const chatBox = document.querySelector("#chatBox");
const activityList = document.querySelector("#activityList");

function addMessage(text, sender = "agent") {
  if (!chatBox) return;

  const message = document.createElement("div");
  message.className = `message ${sender}`;
  message.textContent = text;
  chatBox.appendChild(message);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function addActivity(text) {
  if (!activityList) return;

  const item = document.createElement("div");
  item.className = "activity-item";
  item.textContent = text;
  activityList.prepend(item);
}

if (chatForm && chatInput) {
  chatForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const text = chatInput.value.trim();
    if (!text) return;

    addMessage(text, "user");
    addActivity("নতুন নির্দেশনা পাওয়া গেছে।");
    chatInput.value = "";

    addMessage(
      "তোমার নির্দেশনা পেয়েছি। Gemini AI-এর সঙ্গে সংযোগ এখনো সেটআপ করা হয়নি। ব্যাকএন্ড যুক্ত হলে আমি নির্দেশনা প্রক্রিয়া করতে পারব।",
      "agent"
    );
  });
}

document.querySelectorAll("[data-progress]").forEach((bar) => {
  const progress = Number(bar.dataset.progress || 0);
  bar.style.width = `${Math.max(0, Math.min(100, progress))}%`;
});
