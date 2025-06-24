import gradio as gr
from src.utils import get_base64_image

def image_tab():
    gr.HTML("""
    <style>
    .scaled-img-container {
        display: flex;
        justify-content: center;
        padding: 0.1em 0;
    }
    .scaled-img {
        transform-origin: top center;
    }
    </style>
    """)

    img_data = get_base64_image("assets/DubAI.png")
    logo_html = f"""
    <div class="scaled-img-container">
        <img src="{img_data}" 
             class="scaled-img"
             alt="Logo" />
    </div>
    """
    gr.HTML(logo_html)
