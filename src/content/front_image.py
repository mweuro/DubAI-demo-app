import gradio as gr
from src.utils import get_base64_image

def image_tab():
    gr.HTML("""
    <style>
    .full-width-img-container {
        width: 100%;
        overflow: hidden;
        margin: 0;
        padding: 0;
    }
    .full-width-img {
        width: 100%;
        height: auto;
        display: block;
    }
    </style>
    """)
    
    img_data = get_base64_image("assets/logo.png")
    logo_html = f"""
    <div class="full-width-img-container">
        <img src="{img_data}" 
             class="full-width-img"
             alt="Logo" />
    </div>
    """
    gr.HTML(logo_html)