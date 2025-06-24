import gradio as gr
from src.models.pipeline import PIPELINE
from src.content.transcription_tab import transcription_tab
from src.content.about_tab import about_tab
from src.content.front_image import image_tab
from src.content.results_tab import results_tab
from src.content.about_us_tab import about_us_tab

from dotenv import load_dotenv
load_dotenv()



with gr.Blocks(theme='Taithrah/Minimal') as demo:

    
    image_tab()
    with gr.Tabs():
        about_tab()
        results_tab()
        transcription_tab(PIPELINE)
        about_us_tab()

if __name__ == "__main__":
    demo.launch()