import streamlit as st
import requests

st.title("🌦️ Weather Intelligent Agent")

user_input = st.text_input("Type your message:")

if st.button("Send"):
    response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",
        json={"sender": "user", "message": user_input}
    )

    for r in response.json():
        st.write("Bot:", r.get("text", ""))
