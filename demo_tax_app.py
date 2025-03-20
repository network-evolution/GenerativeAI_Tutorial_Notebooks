import streamlit as st

st.title("🧾 Tax Calculator")

price = st.number_input("Enter the item price (before tax):", value=0, step=1, format="%d", min_value=0)
tax_percentage = st.number_input("Enter the tax percentage:", value=18, step=1, format="%d", min_value=0, max_value=100)

tax_amount = (price * tax_percentage) / 100
total_price = price + tax_amount

st.subheader("Calculation Result")

st.write(f"**Tax Amount:** ₹{tax_amount:.2f}")
st.write(f"**Total Price (after tax):** ₹{total_price:.2f}")
