import gradio as gr

def about_tab():
    with gr.TabItem("ℹ️ **O projekcie**"):
        gr.Markdown("## O DubAI")
        gr.Markdown("""
            DubAI to aplikacja typu end-to-end umożliwiająca:
            
            - transkrypcję mowy (ASR),
            - tłumaczenie na inny język,
            - oraz syntezę mowy z zachowaniem brzmienia głosu.

            **Zastosowania:** dubbing gier, AI-asystenci, tworzenie voice-overów.

            **Technologie:** Whisper, DeepL, XTTS, Gradio, Python.
        """)