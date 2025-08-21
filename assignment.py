import streamlit as st

st.title("Favorite Programming Language Selector")

st.subheader("Here you will choose your favorite programming language")

st.text("All you have to do is to select your favorite Programming langauge from the below downbar")

lang = st.selectbox("Choose Language", ["Python","Java","C++","C","PHP","Javascript"])

st.write(f"You chose {lang}, Excellent choice")

st.success("Your Langauge choice is noted")

st.write("Thankyou ❤️")