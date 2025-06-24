import gradio as gr



def pdf_tab():
    with gr.Tab("📂 Inne"):
        with gr.Column():
            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">📂 Inne</div>')
            gr.HTML("""
                <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                Chciałbyś dowiedzieć się więcej? Poniżej znajdują się dodatkowe pliki związane z projektem, które udostępniamy do pobrania.
                <br><br>
                </div>
            """)
            gr.File(value="assets/G13_DUBAI.pdf", label="🖼️ Plakat", interactive=True)
            gr.File(value="assets/G13_DUBAI.pptx", label="📈 Prezentacja", interactive=True)
            