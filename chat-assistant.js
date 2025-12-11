// AI Chat Assistant
class ChatAssistant {
    constructor() {
        this.messages = [];
        this.whatsappNumber = '201006307045'; // رقم الواتساب بتاعك
        this.init();
    }

    init() {
        this.createChatWidget();
        this.attachEventListeners();
        this.sendWelcomeMessage();
    }

    createChatWidget() {
        const widget = document.createElement('div');
        widget.className = 'chat-widget';
        widget.innerHTML = `
            <div class="chat-box" id="chatBox">
                <div class="chat-header">
                    <div class="chat-avatar"></div>
                    <div class="chat-header-info">
                        <h3>Amr's Assistant</h3>
                        <p><span class="chat-status"></span>Online now</p>
                    </div>
                </div>
                <div class="chat-messages" id="chatMessages"></div>
                <div class="chat-input-area">
                    <input type="text" class="chat-input" id="chatInput" placeholder="Type your message...">
                    <button class="chat-send" id="chatSend">
                        <i class="fas fa-paper-plane"></i>
                    </button>
                </div>
            </div>
            <button class="chat-button" id="chatButton">
                <span class="chat-badge">1</span>
            </button>
        `;
        document.body.appendChild(widget);
    }

    attachEventListeners() {
        const chatButton = document.getElementById('chatButton');
        const chatBox = document.getElementById('chatBox');
        const chatSend = document.getElementById('chatSend');
        const chatInput = document.getElementById('chatInput');

        chatButton.addEventListener('click', () => this.toggleChat());
        chatSend.addEventListener('click', () => this.sendMessage());
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.sendMessage();
        });
    }

    toggleChat() {
        const chatButton = document.getElementById('chatButton');
        const chatBox = document.getElementById('chatBox');
        const badge = document.querySelector('.chat-badge');

        chatButton.classList.toggle('active');
        chatBox.classList.toggle('active');

        if (chatBox.classList.contains('active')) {
            badge.style.display = 'none';
            document.getElementById('chatInput').focus();
        }
    }

    sendWelcomeMessage() {
        setTimeout(() => {
            this.addBotMessage(
                "مرحباً! 👋 أنا مساعد عمرو الشخصي\n\nأقدر أساعدك في:\n• معرفة خدماتنا وأعمالنا\n• الإجابة على أسئلتك\n• توصيلك بعمرو مباشرة\n\nإزاي أقدر أساعدك؟ 😊",
                [
                    { text: "🎨 شوف أعمالنا", action: "projects" },
                    { text: "💼 الخدمات المتاحة", action: "services" },
                    { text: "💬 كلم عمرو", action: "contact" }
                ]
            );
        }, 1000);
    }

    sendMessage() {
        const input = document.getElementById('chatInput');
        const message = input.value.trim();

        if (!message) return;

        this.addUserMessage(message);
        input.value = '';

        // Keep input focused and enabled
        setTimeout(() => {
            input.focus();
        }, 100);

        // Show typing indicator
        this.showTyping();

        // Process message
        setTimeout(() => {
            this.hideTyping();
            this.processMessage(message);
            // Re-focus input after bot response
            setTimeout(() => {
                input.focus();
            }, 100);
        }, 1500);
    }

    processMessage(message) {
        const lowerMessage = message.toLowerCase();

        // Greetings
        if (lowerMessage.match(/^(مرحب|هلا|السلام|صباح|مساء|hi|hello|hey)/)) {
            this.addBotMessage(
                "أهلاً وسهلاً! 😊\n\nأنا هنا عشان أساعدك تعرف أكتر عن:\n\n✨ خدمات التصميم الجرافيكي\n🎬 مونتاج وتحرير الفيديو\n📱 تصميم محتوى السوشيال ميديا\n🎨 الهوية البصرية للشركات\n\nعايز تعرف عن إيه بالتحديد؟",
                [
                    { text: "📁 شوف المشاريع", action: "view_projects" },
                    { text: "💰 عايز أعمل مشروع", action: "contact" }
                ]
            );
        }
        // Projects
        else if (lowerMessage.includes('project') || lowerMessage.includes('work') || lowerMessage.includes('portfolio') ||
            lowerMessage.includes('مشروع') || lowerMessage.includes('شغل') || lowerMessage.includes('أعمال')) {
            this.addBotMessage(
                "عندنا **853+ مشروع** منجز في مجالات مختلفة! 🎨\n\n**أبرز المجالات:**\n• تصميم الهوية البصرية للشركات\n• حملات تسويقية متكاملة\n• موشن جرافيك احترافي\n• مونتاج فيديوهات\n• محتوى سوشيال ميديا\n• تصميمات طباعة\n\nكل مشروع بنهتم بأدق التفاصيل! ✨",
                [
                    { text: "👀 شوف المشاريع", action: "view_projects" },
                    { text: "💬 عايز مشروع زيهم", action: "whatsapp" }
                ]
            );
        }
        // Services
        else if (lowerMessage.includes('service') || lowerMessage.includes('skill') || lowerMessage.includes('do') ||
            lowerMessage.includes('خدم') || lowerMessage.includes('بتعمل') || lowerMessage.includes('مهار')) {
            this.addBotMessage(
                "**الخدمات اللي بنقدمها:** 💼\n\n🎨 **تصميم جرافيك:**\n• تصميم شعارات وهويات بصرية\n• بوسترات وإعلانات\n• تصميمات طباعة\n\n🎬 **فيديو:**\n• مونتاج احترافي\n• موشن جرافيك\n• فيديوهات دعائية\n\n📱 **سوشيال ميديا:**\n• تصميم بوستات\n• محتوى تفاعلي\n• حملات إعلانية\n\n**الخبرة:** 9+ سنوات في المجال! 🏆",
                [
                    { text: "💰 كام التكلفة؟", action: "pricing" },
                    { text: "📞 عايز أتكلم معاك", action: "whatsapp" }
                ]
            );
        }
        // Pricing
        else if (lowerMessage.includes('price') || lowerMessage.includes('cost') || lowerMessage.includes('quote') ||
            lowerMessage.includes('سعر') || lowerMessage.includes('كام') || lowerMessage.includes('تكلف')) {
            this.addBotMessage(
                "الأسعار بتختلف حسب:\n• نوع المشروع\n• حجم العمل المطلوب\n• المدة الزمنية\n• التفاصيل والمتطلبات\n\n**عشان أديك سعر دقيق:**\nمحتاج أعرف تفاصيل مشروعك! 📋\n\nتعالى نتكلم على الواتساب وهقولك السعر المناسب ليك 💬",
                [
                    { text: "💬 يلا نتكلم!", action: "whatsapp" }
                ]
            );
        }
        // Order/Hire
        else if (lowerMessage.includes('order') || lowerMessage.includes('hire') || lowerMessage.includes('work with') ||
            lowerMessage.includes('عايز') || lowerMessage.includes('محتاج') || lowerMessage.includes('أطلب')) {
            this.addBotMessage(
                "ممتاز! 🎉\n\nعشان نبدأ مشروعك، محتاج أعرف:\n• نوع المشروع (تصميم/فيديو/سوشيال ميديا)\n• التفاصيل اللي عايزها\n• الميزانية المتاحة\n• الوقت المطلوب\n\nتعالى نتكلم على الواتساب وهنظبط كل حاجة! 📱",
                [
                    { text: "💬 فتح الواتساب", action: "whatsapp" }
                ]
            );
        }
        // Contact
        else if (lowerMessage.includes('contact') || lowerMessage.includes('email') || lowerMessage.includes('phone') ||
            lowerMessage.includes('whatsapp') || lowerMessage.includes('تواصل') || lowerMessage.includes('كلم')) {
            this.addBotMessage(
                "**طرق التواصل:** 📞\n\n📧 **Email:**\namrelsheikh151@gmail.com\n\n💼 **LinkedIn:**\nAmr Elsheikh\n\n💬 **WhatsApp:**\nمتاح 24/7 للرد على استفساراتك!\n\nأسرع طريقة هي الواتساب 🚀",
                [
                    { text: "💬 WhatsApp", action: "whatsapp" },
                    { text: "📧 Email", action: "email" }
                ]
            );
        }
        // Experience
        else if (lowerMessage.includes('experience') || lowerMessage.includes('years') ||
            lowerMessage.includes('خبر') || lowerMessage.includes('سن')) {
            this.addBotMessage(
                "**الخبرة العملية:** 🏆\n\n✨ **9+ سنوات** في التصميم الجرافيكي ومونتاج الفيديو\n\n💼 **الوظيفة الحالية:**\nMarketing Manager في Elsaihy Group Company\n\n📊 **الإنجازات:**\n• 853+ مشروع منجز\n• 524,123+ مشاهدة للأعمال\n• عملاء من مختلف الدول\n\nالخبرة مش بس في التصميم، كمان في فهم احتياجات السوق! 🎯",
                [
                    { text: "🎨 شوف الأعمال", action: "view_projects" },
                    { text: "💼 نشتغل مع بعض", action: "whatsapp" }
                ]
            );
        }
        // Thanks
        else if (lowerMessage.match(/(thank|شكر|متشكر)/)) {
            this.addBotMessage(
                "العفو! 😊 أنا موجود دايماً لو محتاج أي مساعدة.\n\nلو عايز تبدأ مشروع أو عندك أي استفسار، كلمني على الواتساب! 💬",
                [
                    { text: "💬 فتح الواتساب", action: "whatsapp" }
                ]
            );
        }
        // Default
        else {
            this.addBotMessage(
                "أقدر أساعدك في:\n\n🎨 **معرفة خدماتنا**\n(تصميم جرافيك، فيديو، سوشيال ميديا)\n\n📁 **مشاهدة أعمالنا**\n(853+ مشروع منجز)\n\n💰 **الاستفسار عن الأسعار**\n\n💬 **التواصل المباشر**\n(واتساب، إيميل، لينكد إن)\n\nإيه اللي تحب تعرفه؟ 😊",
                [
                    { text: "🎨 الخدمات", action: "services" },
                    { text: "📁 الأعمال", action: "projects" },
                    { text: "💬 تواصل", action: "contact" }
                ]
            );
        }
    }

    handleQuickReply(action) {
        switch (action) {
            case 'projects':
                this.addUserMessage("عايز أشوف المشاريع");
                this.showTyping();
                setTimeout(() => {
                    this.hideTyping();
                    this.processMessage("مشاريع");
                }, 1000);
                break;

            case 'services':
                this.addUserMessage("إيه الخدمات المتاحة؟");
                this.showTyping();
                setTimeout(() => {
                    this.hideTyping();
                    this.processMessage("خدمات");
                }, 1000);
                break;

            case 'contact':
                this.addUserMessage("عايز أتواصل مع عمرو");
                this.showTyping();
                setTimeout(() => {
                    this.hideTyping();
                    this.processMessage("تواصل");
                }, 1000);
                break;

            case 'pricing':
                this.addUserMessage("كام الأسعار؟");
                this.showTyping();
                setTimeout(() => {
                    this.hideTyping();
                    this.processMessage("سعر");
                }, 1000);
                break;

            case 'view_projects':
                window.location.href = '#work';
                setTimeout(() => {
                    this.addBotMessage("شوف المشاريع في القسم ده! 🎨\n\nلو عجبك أي مشروع وعايز حاجة زيه، كلمني على الواتساب! 💬",
                        [{ text: "💬 كلمني دلوقتي", action: "whatsapp" }]
                    );
                }, 500);
                break;

            case 'whatsapp':
                const message = "السلام عليكم يا عمرو! 👋\n\nأنا مهتم بخدماتك في التصميم، ممكن نتكلم؟";
                window.open(`https://wa.me/${this.whatsappNumber}?text=${encodeURIComponent(message)}`, '_blank');
                this.addBotMessage("فاتح الواتساب! 💬\n\nهكلمك في أسرع وقت ممكن! 😊");
                break;

            case 'email':
                window.location.href = 'mailto:amrelsheikh151@gmail.com?subject=استفسار عن الخدمات';
                this.addBotMessage("فاتح الإيميل! 📧\n\nابعت رسالتك وهرد عليك في أقرب وقت.");
                break;
        }
    }

    addUserMessage(text) {
        const messagesContainer = document.getElementById('chatMessages');
        const time = new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });

        const messageDiv = document.createElement('div');
        messageDiv.className = 'message user';
        messageDiv.innerHTML = `
            <div class="message-avatar">👤</div>
            <div class="message-content">
                <p class="message-text">${text}</p>
                <div class="message-time">${time}</div>
            </div>
        `;

        messagesContainer.appendChild(messageDiv);
        this.scrollToBottom();
    }

    addBotMessage(text, quickReplies = []) {
        const messagesContainer = document.getElementById('chatMessages');
        const time = new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });

        const messageDiv = document.createElement('div');
        messageDiv.className = 'message bot';

        let quickRepliesHTML = '';
        if (quickReplies.length > 0) {
            quickRepliesHTML = '<div class="quick-replies">';
            quickReplies.forEach(reply => {
                quickRepliesHTML += `<button class="quick-reply" data-action="${reply.action}">${reply.text}</button>`;
            });
            quickRepliesHTML += '</div>';
        }

        messageDiv.innerHTML = `
            <div class="message-avatar bot-avatar"></div>
            <div class="message-content">
                <p class="message-text">${text.replace(/\n/g, '<br>')}</p>
                <div class="message-time">${time}</div>
                ${quickRepliesHTML}
            </div>
        `;

        messagesContainer.appendChild(messageDiv);

        // Attach quick reply listeners
        if (quickReplies.length > 0) {
            messageDiv.querySelectorAll('.quick-reply').forEach(btn => {
                btn.addEventListener('click', () => {
                    this.handleQuickReply(btn.dataset.action);
                });
            });
        }

        this.scrollToBottom();
    }

    showTyping() {
        const messagesContainer = document.getElementById('chatMessages');
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot typing-message';
        typingDiv.innerHTML = `
            <div class="message-avatar">🤖</div>
            <div class="message-content">
                <div class="typing-indicator">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>
        `;
        messagesContainer.appendChild(typingDiv);
        this.scrollToBottom();
    }

    hideTyping() {
        const typingMessage = document.querySelector('.typing-message');
        if (typingMessage) {
            typingMessage.remove();
        }
    }

    scrollToBottom() {
        const messagesContainer = document.getElementById('chatMessages');
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
}

// Initialize chat assistant when page loads
document.addEventListener('DOMContentLoaded', () => {
    new ChatAssistant();
});
