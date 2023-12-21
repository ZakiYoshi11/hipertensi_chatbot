import streamlit as st
from chatbot import get_response
from cek_hipertensi import cek_hipertensi
from util.jenis_hipertensi import detect_hypertension


# ===============SETUP===============
# hide_st_style = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}

# </style>
# """
st.set_page_config(
    page_title="Tensibot",
    page_icon="⛑"
)
# st.markdown(hide_st_style, unsafe_allow_html=True)

# Inisialisasi variabel st.session_state.messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Pesan awal dari chatbot
if "tensibot_greeted" not in st.session_state:
    tensibot_greeting = "Hai, aku Tensibot. Bagaimana kabarmu saat ini?"
    st.session_state.messages.append({"role": "🩸", "content": tensibot_greeting})
    st.session_state.tensibot_greeted = True

# Main App
st.title(":drop_of_blood: Tensibot")
st.write("---")
st.sidebar.success("Pilih Halaman Di Atas")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# ==================CHATBOT SYSTEM==========
# input pesan
if prompt := st.chat_input("Ketik pesan.."):
    # msg user
    with st.chat_message("user"):
        st.markdown(prompt)
    # add to history msg
    st.session_state.messages.append({"role": "user", "content": prompt})

    # msg chatbot
    with st.chat_message("🩸"):
        response = ""
        if "#cek" in prompt:
            response = cek_hipertensi(prompt)
        elif "#st" in prompt and "#dt" in prompt:
            response = detect_hypertension(prompt)
        else:
            response = f"{get_response(prompt)}"
        st.markdown(response)
    st.session_state.messages.append({"role": "🩸", "content": response})
