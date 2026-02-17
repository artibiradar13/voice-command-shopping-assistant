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
# INIT DB
# -------------------------

init_db()


# SESSION STATE

if "messages" not in st.session_state:
    st.session_state.messages = []



# HANDLE COMMAND

def handle_command(command):

    intent, item, qty = process_command(command)

    if not item and intent != "show":
        return "⚠️ I couldn't identify the item."

    if intent == "add":

        add_item(item, qty)   # FIXED METHOD (db_helper)

        category = get_category(item)
        suggestions = get_suggestions(item)

        reply = f"✅ Added **{qty} {item}** to **{category.title()}**"

        if suggestions:
            reply += f"\n\n💡 You may also need: **{', '.join(suggestions)}**"

        return reply


    elif intent == "remove":

        remove_item(item)

        return f"❌ Removed **{item}**"


    elif intent == "show":

        return "🧾 Here is your shopping list"


    return "⚠️ Command not understood"



# HEADER


st.title("🛒 AI Voice Shopping Assistant")

st.caption(
    "Smart voice-powered shopping list manager"
)


# -------------------------
# INPUT SECTION
# -------------------------

col1, col2 = st.columns([4,1])

with col1:
    user_input = st.chat_input("Type command like: Add 2 apples")

with col2:
    speak_clicked = st.button("🎤 Speak", use_container_width=True)


# -------------------------
# HANDLE TEXT INPUT
# -------------------------

if user_input:

    st.session_state.messages.append(("user", user_input))

    reply = handle_command(user_input)

    st.session_state.messages.append(("assistant", reply))

    st.rerun()


# -------------------------
# HANDLE VOICE INPUT
# -------------------------

if speak_clicked:

    with st.spinner("🎧 Listening..."):

        command = get_voice_command()

    if command:

        st.session_state.messages.append(
            ("user", f"🎤 {command}")
        )

        reply = handle_command(command)

        st.session_state.messages.append(
            ("assistant", reply)
        )

    else:

        st.session_state.messages.append(
            ("assistant", "⚠️ Could not understand voice input.")
        )

    st.rerun()

# CHAT DISPLAY

for sender, msg in st.session_state.messages:

    with st.chat_message(sender):

        st.markdown(msg)



st.divider()

# SHOPPING LIST

col1, col2 = st.columns([5,1])

with col1:

    st.subheader("🧾 Shopping List")

with col2:

    if st.button("🗑 Clear", use_container_width=True):

        clear_items()

        st.rerun()



items = get_items()



# -------------------------
# DISPLAY ITEMS
# -------------------------

if not items:

    st.info("Your shopping list is empty")

else:

    for index, (item, qty, category) in enumerate(items):

        st.container()

        c1, c2, c3, c4, c5 = st.columns([3,1,1,1,1])


        # ITEM

        with c1:

            st.markdown(

                f"""
                **{item}**

                <small style='color:gray'>
                📂 {category}
                </small>
                """,

                unsafe_allow_html=True
            )


        # DECREASE

        with c2:

            if st.button(

                "➖",

                key=f"dec_{index}"

            ):

                update_quantity(item, qty-1)

                st.rerun()



        # QTY

        with c3:

            st.markdown(

                f"<center><b>{qty}</b></center>",

                unsafe_allow_html=True
            )



        # INCREASE

        with c4:

            if st.button(

                "➕",

                key=f"inc_{index}"

            ):

                update_quantity(item, qty+1)

                st.rerun()



        # DELETE

        with c5:

            if st.button(
                "🗑",
                key=f"del_{index}"

            ):

                remove_item(item)
                st.rerun()



st.divider()

st.caption("Built with Streamlit + Voice + NLP")