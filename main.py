import gradio as gr
from src.models.pipeline import PIPELINE
from src.content.transcription_tab import transcription_tab
from src.content.about_tab import about_tab
from src.content.contact_tab import contact_tab
from src.content.front_image import image_tab
from src.content.method_tab import method_tab






with gr.Blocks(theme='Taithrah/Minimal') as demo:

    
    image_tab()
    with gr.Tabs():
        about_tab()
        method_tab()
        transcription_tab(PIPELINE)
        contact_tab()

if __name__ == "__main__":
    demo.launch()