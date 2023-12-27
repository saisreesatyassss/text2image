# import streamlit as st
# import requests
# from PIL import Image
# import io



# API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.content

# # Streamlit app
# st.title("Image Generation with Hugging Face Model")

# # User input prompt
# user_input = st.text_input("Enter a prompt:", "god is watching over earth")

# # Generate image button
# if st.button("Generate Image"):
#     # Query the model
#     image_bytes = query({"inputs": user_input})

#     # Access the image with PIL.Image
#     image = Image.open(io.BytesIO(image_bytes))

#     # Display the image using Streamlit
#     st.image(image, caption="Generated Image", use_column_width=True)
    
#     # Download image option
#     # if st.button("Download Image"):
#         # Download link instead of download button
#     st.download_button(
#             label="Download Image",
#             data=image_bytes,
#             file_name="generated_image.png",
#             key="download_button",
#             mime="image/png",  # Specify the MIME type for the download

#         )

