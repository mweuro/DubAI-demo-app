import gradio as gr

def contact_tab():
    with gr.TabItem("📩 Kontakt"):
        gr.Markdown("## Formularz kontaktowy")
        gr.Textbox(label="📧 Twój email")
        gr.Textbox(label="💬 Wiadomość", lines=4)
        gr.Button("✉️ Wyślij (do zaimplementowania)")