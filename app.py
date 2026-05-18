import streamlit as st
from openai import OpenAI

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="EduGenie AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to bottom right, #0f172a, #111827);
    color: white;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Title */
.main-title {
    font-size: 3rem;
    font-weight: 700;
    text-align: center;
    color: white;
    margin-bottom: 0;
}

.sub-title {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 30px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #1f2937;
}

/* Chat Messages */
.stChatMessage {
    padding: 15px;
    border-radius: 18px;
    margin-bottom: 12px;
    backdrop-filter: blur(10px);
}

/* User Message */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background: rgba(59,130,246,0.15);
    border: 1px solid rgba(59,130,246,0.3);
}

/* Assistant Message */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
}

/* Buttons */
.stButton button {
    width: 100%;
    border-radius: 12px;
    height: 45px;
    border: none;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    font-weight: 600;
}

/* Input Box */
.stChatInput input {
    border-radius: 15px !important;
    background-color: #1f2937 !important;
    color: white !important;
}

/* Text Area */
textarea {
    background-color: #1f2937 !important;
    color: white !important;
}

/* Select Box */
div[data-baseweb="select"] {
    background-color: #1f2937;
    border-radius: 10px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SESSION
# ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

SYSTEM_PROMPT = """
You are EduGenie AI, a smart study assistant.
Explain topics simply and clearly.
"""

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:

    st.markdown("## ⚙️ Settings")

    api_key = st.text_input(
        "Groq API Key",
        type="password"
    )

    model_name = st.selectbox(
        "AI Model",
        [
            "llama-3.1-8b-instant",
            "llama-3.3-70b-versatile",
            "gemma2-9b-it"
        ]
    )

    st.markdown("---")

    st.markdown("## 📝 Quick Notes")

    notes = st.text_area(
        "Paste notes",
        height=180
    )

    if st.button("✨ Summarize"):

        if api_key and notes:

            client = OpenAI(
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1"
            )

            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {
                        "role": "user",
                        "content": f"Summarize:\n{notes}"
                    }
                ]
            )

            st.success("Done!")

            st.markdown(response.choices[0].message.content)

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown(
    '<div class="main-title">🧠 EduGenie AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Your futuristic AI study assistant</div>',
    unsafe_allow_html=True
)

# ─────────────────────────────────────────────
# FEATURE CARDS
# ─────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📚 Learn Faster</h3>
    <p>Understand difficult concepts easily.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>📝 Smart Summaries</h3>
    <p>Convert long notes into quick revision points.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>⚡ AI Explanations</h3>
    <p>Get instant beginner-friendly answers.</p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CHAT HISTORY
# ─────────────────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ─────────────────────────────────────────────
# CHAT INPUT
# ─────────────────────────────────────────────
prompt = st.chat_input(
    "Ask me anything about studies..."
)

if prompt:

    if not api_key:
        st.error("Please enter API key")
        st.stop()

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        stream = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *st.session_state.messages[-6:]
            ],
            stream=True
        )

        response = st.write_stream(
            chunk.choices[0].delta.content or ""
            for chunk in stream
        )

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })