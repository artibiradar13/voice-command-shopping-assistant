import streamlit as st
from utils.db_helper import *
from utils.voice_helper import get_voice_command
from utils.nlp_helper import process_command
from utils.suggestion_helper import get_suggestions
from utils.categories_helper import get_category


# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI Voice Shopping Assistant",
    page_icon="🛒",
    layout="centered"
)

# -------------------------
# INITIALIZE DATABASE
# -------------------------

init_db()

# -------------------------
# SESSION STATE
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# HANDLE COMMAND
# -------------------------

def handle_command(command):

    intent, item, qty = process_command(command)

    if not item and intent != "show":
        return "⚠️ I couldn't identify the item. Please try again."

    if intent == "add":
        add_item(item, qty)

        category = get_category(item)
        suggestions = get_suggestions(item)

        reply = f"✅ Added **{qty} {item}** to **{category.title()}** category."

        if suggestions:
            reply += f"\n\n💡 You may also need: **{', '.join(suggestions)}**"

        return reply

    elif intent == "remove":
        remove_item(item)
        return f"❌ Removed **{item}** from your list."

    elif intent == "show":
        return "🧾 Here is your current shopping list."

    else:
        return "⚠️ Sorry, I didn’t understand that command."

# -------------------------
# HEADER
# -------------------------

st.title("🛒 AI Voice Shopping Assistant")
st.caption("Smart voice-powered shopping list manager with intelligent suggestions")

st.divider()

# -------------------------
# INPUT SECTION
# -------------------------

col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.chat_input("Type a command (e.g., Add 2 apples)")

with col2:
    speak_clicked = st.button("🎤 Speak", use_container_width=True)

# -------------------------
# HANDLE TEXT INPUT
# -------------------------

if user_input:
    st.session_state.messages.append(("user", user_input))

    with st.spinner("Processing..."):
        reply = handle_command(user_input)

    st.session_state.messages.append(("assistant", reply))
    st.rerun()

# -------------------------
# HANDLE VOICE INPUT
# -------------------------

if speak_clicked:
    with st.spinner("Listening..."):
        command = get_voice_command()

    if command:
        st.session_state.messages.append(("user", f"🎤 {command}"))

        reply = handle_command(command)

        st.session_state.messages.append(("assistant", reply))
    else:
        st.session_state.messages.append(
            ("assistant", "⚠️ Could not understand voice input.")
        )

    st.rerun()

# -------------------------
# CHAT DISPLAY
# -------------------------

for sender, msg in st.session_state.messages:
    with st.chat_message(sender):
        st.markdown(msg)

st.divider()

# -------------------------
# SHOPPING LIST SECTION
# -------------------------

col1, col2 = st.columns([5,1])

with col1:
    st.subheader("🧾 Shopping List")

with col2:
    if st.button("🗑 Clear All", use_container_width=True):
        clear_items()
        st.session_state.messages.append(
            ("assistant", "🗑 Shopping list cleared.")
        )
        st.rerun()

# -------------------------
# DISPLAY ITEMS
# -------------------------

items = get_items()

if not items:
    st.info("Your shopping list is empty.")
else:
    for item, qty, category in items:

        container = st.container()
        with container:

            col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])

            # Item + category
            with col1:
                st.markdown(
                    f"**{item}**  \n<small style='color:gray;'>📂 {category}</small>",
                    unsafe_allow_html=True
                )

            # Decrease
            with col2:
                if st.button("−", key=f"dec_{item}"):
                    update_quantity(item, qty - 1)
                    st.rerun()

            # Quantity
            with col3:
                st.markdown(
                    f"<div style='text-align:center; font-weight:600;'>{qty}</div>",
                    unsafe_allow_html=True
                )

            # Increase
            with col4:
                if st.button("+", key=f"inc_{item}"):
                    update_quantity(item, qty + 1)
                    st.rerun()

            # Delete
            with col5:
                if st.button("❌", key=f"del_{item}"):
                    remove_item(item)
                    st.rerun()

# -------------------------
# FOOTER
# -------------------------

st.divider()
st.caption("Built with Streamlit + OpenAI Whisper API + NLP + Smart Suggestions")
