// static/js/start_new_chat.js

document.addEventListener('DOMContentLoaded', function() {
    console.log("start_new_chat.js DOMContentLoaded fired.");

    const startChatButtons = document.querySelectorAll('.start-chat-btn');

    function getCookie(name) { /* ... your getCookie function ... */ }
    const csrfToken = getCookie('csrftoken');

    let isCreatingConversation = false; // Flag for this specific page

    startChatButtons.forEach(button => {
        button.addEventListener('click', async function() {
            const userId = this.dataset.userId;
            if (!userId) {
                console.error('User ID not found for button:', this);
                alert('Error: User ID not found.');
                return;
            }

            if (isCreatingConversation) {
                console.warn("Conversation creation already in progress. Ignoring duplicate click.");
                return;
            }

            isCreatingConversation = true;
            this.disabled = true; // Disable button immediately

            try {
                const response = await fetch(`/messenger/api/start_conversation/${userId}/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify({})
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.message || `HTTP error! Status: ${response.status}`);
                }

                const data = await response.json();
                if (data.status === 'success' && data.conversation_id) {
                    window.location.href = `/messenger/?conversation_id=${data.conversation_id}`;
                } else {
                    alert('Failed to start conversation: ' + (data.message || 'Unknown error'));
                }
            } catch (error) {
                console.error('Error starting conversation:', error);
                alert('Error starting conversation: ' + error.message);
            } finally {
                isCreatingConversation = false;
                this.disabled = false; // Re-enable button if not redirected
            }
        });
    });
});