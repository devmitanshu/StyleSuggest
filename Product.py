import streamlit as st

# Product information
product_name = "Awesome Product"
product_description = "This is the most amazing product you've ever seen!"
product_price = 19.99
product_image_url = "./adidas.jpeg"

# Display product information
st.image(product_image_url, caption=product_name, use_column_width=True)
st.write(f"*{product_name}* - ${product_price:.2f}")
st.write(product_description)

# Add to cart button
if st.button("Add to Cart"):
    st.write("Product added to cart!")