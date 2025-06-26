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

            gr.HTML('<br><br>')
            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">Repozytorium</div>')
            gr.HTML("""
                <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                <ul>
                <li>
                    <a href="https://github.com/mweuro/DubAI-demo-app">https://github.com/mweuro/DubAI-demo-app</a>
                </li>
                <li>
                    <a href="https://github.com/klaudynka245/DubAI">https://github.com/klaudynka245/DubAI</a>
                </li>
                </ul>
                </div>
            """)
            