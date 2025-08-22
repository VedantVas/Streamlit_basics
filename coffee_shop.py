import streamlit as st

st.title("Welcome to Coffee Shop")

name = st.text_input("Enter Your name")
if name:
    st.write(f"Welcome {name},Please make your order..😊")

coffee_type = st.radio("Select your Coffee",[
    "Espresso",
    "Americano",
    "Latte",
    "Cappuccino",
    "Mocha",
    "Cold Brew",
    "French Press",
    "Turkish Coffee",
    "Arabica",
    "Dark Roast"
])

st.write(f"You selected {coffee_type}, Excellent choice")

add_base = st.checkbox("Add Base")

if add_base:
    base = st.selectbox("Choose your base",["Milk","Almond Milk","Coconut Milk","Mineral Water"])
    st.write(f"Your selected base is {base}")

sugar = st.slider("Sugar level",0,5,2)    
st.write(f"Your sugar level is {sugar}")

cups = st.number_input("How Many cups you want", min_value=1, max_value=10, step=1)
st.write(f"Total cups for order {cups}")

if st.button("Make Coffee"):
    st.success("Your Coffee is being brewed")    


Snacks = st.checkbox("Add snacks")

if Snacks:
    choice = st.radio("Select your Snacks",[
    "Croissant",
    "Muffins",
    "Cookies",
    "Doughnuts",
    "Brownies",
    "Sandwiches",
    "Bagels",
    "Scones",
    "Cakes & Pastries",
    "Toast / Garlic Bread"
])
    st.write(f"Snack you selected is {choice}.")
    if choice == "Cakes & Pastries":
        cake = st.radio("Choose pastry or cake",[
    "Cheesecake",
    "Chocolate Cake",
    "Red Velvet Cake",
    "Black Forest Cake",
    "Carrot Cake",
    "Éclair",
    "Croissant Pastry",
    "Danish Pastry",
    "Napoleon / Mille-feuille",
    "Tart"
])
        st.write(f"{cake} is a nice choice.. {name} 🤗")

    st.success("Soon you will recieve your order")

st.success(f"Thanks for your time {name}❤️")    
    
