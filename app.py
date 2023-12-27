
import streamlit as st
import requests
from PIL import Image, UnidentifiedImageError
import io



API_URLS = {
    "Stable Diffusion": "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4",
    "Stable Diffusion XL": "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
    "Stable Diffusion V1-5": "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5",
    # "SDXL DPO TURBO": "https://api-inference.huggingface.co/models/thibaud/sdxl_dpo_turbo",
    # "Stable Diffusion 2": "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
    # "Stable Diffusion 2-1": "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1",
    "Stable Diffusion V1-4": "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4",
    "SSD 1B": "https://api-inference.huggingface.co/models/segmind/SSD-1B",
    # "IP Adapter": "https://api-inference.huggingface.co/models/h94/IP-Adapter",
    # "DALLE 3 XL": "https://api-inference.huggingface.co/models/openskyml/dalle-3-xl",
    # "Animagine XL 2.0": "https://api-inference.huggingface.co/models/Linaqruf/animagine-xl-2.0",
    "Segmind Vega": "https://api-inference.huggingface.co/models/segmind/Segmind-Vega",
    # "OrangeMixs": "https://api-inference.huggingface.co/models/WarriorMama777/OrangeMixs",
    # "Lora": "https://api-inference.huggingface.co/models/JujoHotaru/lora", 

    

    # Add more API URLs as needed
}

headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response

# Streamlit app
st.title("Image Generation with Hugging Face Model")




selected_api = st.selectbox("Select API URL", list(API_URLS.keys()))

API_URL = API_URLS[selected_api]

# User input prompt
user_input = st.text_input("Enter a prompt:", "Astronaut riding a horse")

# Generate image button
if st.button("Generate Image"):
    try:
        # Query the model
        response = query({"inputs": user_input})

        # Check if the API call was successful (status code 200)
        if response.status_code == 200:
            # Access the image with PIL.Image
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))

            # Display the image using Streamlit
            st.image(image, caption="Generated Image", use_column_width=True)

            # Download image option
            st.download_button(
                label="Download Image",
                data=image_bytes,
                file_name="generated_image.png",
                key="download_button",
                mime="image/png",  # Specify the MIME type for the download
            )
        else:
            st.error(f"Error during API request. Status code: {response.status_code}")
            st.write("Try different Model ")
    except UnidentifiedImageError:
        st.error("Unable to identify the image. The API response may not contain valid image data.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error during request: {e}")
