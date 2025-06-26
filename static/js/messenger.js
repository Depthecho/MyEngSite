// static/js/messenger.js

document.addEventListener('DOMContentLoaded', function() {
    console.log("Messenger script DOMContentLoaded fired."); // Для отладки

    // Получаем элемент, на котором висят data-атрибуты
    const messengerScript = document.querySelector('script[src*="messenger.js"]');

    if (!messengerScript) {
        console.error("messenger.js script tag not found or missing data attributes.");
        return; // Если скрипт не найден, дальнейшая работа бессмысленна
    }

    // Считываем данные из data-атрибутов
    const currentUserId = messengerScript.dataset.currentUserId;
    const initialConversationId = messengerScript.dataset.initialConversationId;

    // Устанавливаем глобальный флаг для предотвращения повторной инициализации.
    // Если этот скрипт загружается и выполняется дважды (чего быть не должно!),
    // этот флаг поможет предотвратить двойное навешивание событий.
    if (window.__messengerInitialized__) {
        console.warn("Messenger script already initialized. Preventing re-initialization.");
        return;
    }
    window.__messengerInitialized__ = true;


    const dialogItems = document.querySelectorAll('.dialog-item');
    const chatArea = document.getElementById('chatArea');
    let messagesList = document.getElementById('messagesList');
    let messageInput = document.getElementById('messageInput');
    const messengerWrapper = document.querySelector('.messenger-wrapper');

    // Флаг для предотвращения множественной отправки сообщения при одном клике/нажатии
    let isSendingMessage = false;

    // CSRF token retrieval function
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrfToken = getCookie('csrftoken');

    // Helper function to scroll messages down
    function scrollToBottom() {
        if (messagesList) {
            messagesList.scrollTop = messagesList.scrollHeight;
        }
    }

    // Function to render messages in the DOM
    function renderMessages(messages) {
        if (!messagesList) return;

        messagesList.innerHTML = ''; // CRITICAL: Clear container before adding messages

        messages.forEach(msg => {
            const messageItem = document.createElement('div');
            messageItem.classList.add('message-item');
            messageItem.classList.add(msg.is_my_message ? 'my-message' : 'other-message');

            const messageTime = new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

            const senderNameHtml = (!msg.is_my_message && msg.sender_username) ? `<p class="message-sender-name">${msg.sender_username}</p>` : '';

            messageItem.innerHTML = `
                <div class="message-bubble">
                    ${senderNameHtml}
                    <p>${msg.content}</p>
                    <span class="message-time">${messageTime}</span>
                    ${msg.is_my_message && msg.is_read !== undefined ? `<span class="message-status">${msg.is_read ? '✓✓' : '✓'}</span>` : ''}
                </div>
            `;
            messagesList.appendChild(messageItem);
        });
        scrollToBottom();
    }

    // Function to load conversation data by ID
    async function loadConversation(conversationId, updateUrl = true) {
        try {
            dialogItems.forEach(d => d.classList.remove('active'));
            const currentDialogItem = document.querySelector(`.dialog-item[data-conversation-id="${conversationId}"]`);
            if (currentDialogItem) {
                currentDialogItem.classList.add('active');
            }

            const response = await fetch(`/messenger/api/conversations/${conversationId}/messages/`);
            if (!response.ok) {
                throw new Error('Failed to load messages');
            }
            const data = await response.json();

            const chatHeader = chatArea.querySelector('.chat-header');
            if (chatHeader) {
                chatHeader.querySelector('.chat-header-avatar').src = data.other_participant_avatar_url;
                chatHeader.querySelector('.chat-header-name').textContent = data.other_participant_username;
            } else {
                const newChatHtml = `
                    <div class="chat-header">
                        <div class="chat-header-info">
                            <img src="${data.other_participant_avatar_url}" alt="Avatar" class="chat-header-avatar">
                            <span class="chat-header-name">${data.other_participant_username}</span>
                        </div>
                    </div>
                    <div class="messages-list" id="messagesList"></div>
                    <div class="message-input-area">
                        <textarea id="messageInput" placeholder="Write a message..."></textarea>
                        <button id="sendMessageBtn" class="send-message-btn">
                            <i class="fas fa-paper-plane"></i>
                        </button>
                    </div>
                `;
                chatArea.innerHTML = newChatHtml;
                messagesList = document.getElementById('messagesList');
                messageInput = document.getElementById('messageInput');
            }

            renderMessages(data.messages);

            const currentSendMessageBtn = chatArea.querySelector('#sendMessageBtn');
            if (currentSendMessageBtn) {
                currentSendMessageBtn.dataset.conversationId = conversationId;
            }

            const noChatSelectedDiv = chatArea.querySelector('.no-chat-selected');
            if (noChatSelectedDiv) {
                noChatSelectedDiv.style.display = 'none';
            }
            if (chatArea.querySelector('.chat-header')) chatArea.querySelector('.chat-header').style.display = 'flex';
            if (messagesList) messagesList.style.display = 'block';
            if (chatArea.querySelector('.message-input-area')) chatArea.querySelector('.message-input-area').style.display = 'flex';

            if (updateUrl) {
                const newUrl = new URL(window.location.href);
                newUrl.searchParams.set('conversation_id', conversationId);
                window.history.pushState({path: newUrl.href}, '', newUrl.href);
            }

            if (window.innerWidth <= 768 && messengerWrapper) {
                messengerWrapper.classList.add('show-chat');
            }

        } catch (error) {
            console.error('Error loading conversation:', error);
            if (chatArea.querySelector('.chat-header')) chatArea.querySelector('.chat-header').style.display = 'none';
            if (messagesList) messagesList.innerHTML = '<div class="no-messages">Failed to load messages.</div>';
            if (chatArea.querySelector('.message-input-area')) chatArea.querySelector('.message-input-area').style.display = 'none';
            const noChatSelectedDiv = chatArea.querySelector('.no-chat-selected');
            if (noChatSelectedDiv) noChatSelectedDiv.style.display = 'flex';
        }
    }

    // Event handler for sending message - uses isSendingMessage flag
    async function handleSendMessageClick(event) {
        const clickedButton = event.target.closest('#sendMessageBtn');
        if (!clickedButton) return;

        if (isSendingMessage) {
            console.warn('Message already being sent. Ignoring duplicate click.');
            return;
        }

        const content = messageInput.value.trim();
        const conversationId = clickedButton.dataset.conversationId;

        if (content === '' || !conversationId) {
            return;
        }

        isSendingMessage = true;
        clickedButton.disabled = true;
        messageInput.disabled = true;

        try {
            const response = await fetch(`/messenger/api/conversations/${conversationId}/messages/send/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ content: content })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || `Failed to send message: ${response.status}`);
            }

            const data = await response.json();

            const messageItem = document.createElement('div');
            messageItem.classList.add('message-item', 'my-message');
            const messageTime = new Date(data.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            messageItem.innerHTML = `
                <div class="message-bubble">
                    <p>${data.content}</p>
                    <span class="message-time">${messageTime}</span>
                    ${data.is_my_message && data.is_read !== undefined ? `<span class="message-status">${data.is_read ? '✓✓' : '✓'}</span>` : ''}
                </div>
            `;
            if (messagesList) {
                messagesList.appendChild(messageItem);
                scrollToBottom();
            }
            messageInput.value = '';

            const activeDialog = document.querySelector(`.dialog-item[data-conversation-id="${conversationId}"]`);
            if (activeDialog) {
                const lastMessageDiv = activeDialog.querySelector('.dialog-last-message');
                if (lastMessageDiv) {
                    lastMessageDiv.textContent = data.content.substring(0, 30) + (data.content.length > 30 ? '...' : '');
                }
                const timeDiv = activeDialog.querySelector('.dialog-time');
                if (timeDiv) {
                     timeDiv.textContent = new Date(data.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
                }
                const parentList = activeDialog.parentNode;
                if (parentList && parentList.firstChild !== activeDialog) {
                    parentList.prepend(activeDialog);
                }
            }

        } catch (error) {
            console.error('Error sending message:', error);
            alert('Error sending message: ' + error.message);
        } finally {
            isSendingMessage = false;
            clickedButton.disabled = false;
            messageInput.disabled = false;
            messageInput.focus();
        }
    }

    // Event handler for Enter key in textarea - checks isSendingMessage flag
    function handleMessageInputKeydown(event) {
        if (event.target.id === 'messageInput' && event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            if (!isSendingMessage) { // Prevent click if already sending
                const currentSendMessageBtn = chatArea.querySelector('#sendMessageBtn');
                if (currentSendMessageBtn) {
                    currentSendMessageBtn.click();
                }
            }
        }
    }

    // Event handler for auto-adjusting textarea height
    function handleMessageInputHeightAdjust(event) {
        if (event.target.id === 'messageInput') {
            event.target.style.height = 'auto';
            event.target.style.height = (event.target.scrollHeight) + 'px';
        }
    }

    // ATTACHING EVENT LISTENERS USING DELEGATION to chatArea
    chatArea.addEventListener('click', handleSendMessageClick);
    chatArea.addEventListener('keydown', handleMessageInputKeydown);
    chatArea.addEventListener('input', handleMessageInputHeightAdjust);

    // Event listener for clicks on dialog items in the sidebar
    document.getElementById('dialogsList').addEventListener('click', function(event) {
        const dialogItem = event.target.closest('.dialog-item');
        if (dialogItem) {
            const conversationId = dialogItem.dataset.conversationId;
            if (conversationId) {
                loadConversation(conversationId, true);
            }
        }
    });

    // Mobile adaptation
    function setupMobileBackButton() {
        const chatHeader = chatArea.querySelector('.chat-header');
        if (!chatHeader) return;

        let backBtn = chatHeader.querySelector('.back-to-dialogs');
        if (backBtn) {
            backBtn.remove();
        }

        if (window.innerWidth <= 768) {
            backBtn = document.createElement('button');
            backBtn.classList.add('back-to-dialogs');
            backBtn.innerHTML = '<i class="fas fa-arrow-left"></i>';
            chatHeader.prepend(backBtn);

            backBtn.addEventListener('click', function() {
                messengerWrapper.classList.remove('show-chat');
            });
        }
    }

    setupMobileBackButton();
    window.addEventListener('resize', setupMobileBackButton);

    // Initial load logic
    if (initialConversationId) {
        // Загружаем беседу, если ID передан
        loadConversation(initialConversationId, false); // false, чтобы не менять URL снова
        if (window.innerWidth <= 768 && messengerWrapper) {
            messengerWrapper.classList.add('show-chat');
        }
    } else {
        if (window.innerWidth > 768 && chatArea) {
             const noChatSelectedDiv = chatArea.querySelector('.no-chat-selected');
             if (noChatSelectedDiv) {
                noChatSelectedDiv.style.display = 'flex';
                const chatHeader = chatArea.querySelector('.chat-header');
                if (chatHeader) chatHeader.style.display = 'none';
                if (messagesList) messagesList.style.display = 'none';
                const messageInputArea = chatArea.querySelector('.message-input-area');
                if (messageInputArea) messageInputArea.style.display = 'none';
             }
        }
    }
});