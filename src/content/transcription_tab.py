import gradio as gr

def transcription_tab(full_pipeline):
    with gr.Tab("🎙️ Aplikacja"):
        with gr.Column(elem_classes="method-tab"):
            gr.HTML('<div style="font-size: 40px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">🎙️ Aplikacja</div>')
            gr.HTML("""
                    <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                    Jesteś ciekawy, jak Twój głos brzmi w innym języku? Możesz to sprawdzić! W ramach projektu udostępniamy wersję demonstracyjną naszej aplikacji. Wystarczy nagrać swoją wypowiedź w języku polskim, a aplikacja automatycznie przetłumaczy ją na język angielski i wygeneruje syntezę głosu. Wystarczy kliknąć przycisk "Uruchom", aby rozpocząć proces.
                    <br><br>
                    A może masz już gotowy plik audio z wypowiedzią w języku polskim? Możesz go przesłać, przeciągając go do pola poniżej lub klikając na nie, aby otworzyć okno wyboru pliku. Aplikacja obsługuje pliki w formacie WAV.
                    <br><br>
                    Architektura owej wersji demonstracyjnej jest okrojoną wersją naszego pełnego rozwiązania, jednak zawiera najważniejsze funkcjonalności pozwalające na relatywnie szybkie działanie. Składa się ona z modelu transkrypcji mowy Whisper Large v3 Turbo, modułu tłumaczenia wykorzystującego API od DeepL, oraz modelu syntezy mowy XTTS.
                    """)

            audio_input = gr.Audio(type="filepath", label="🎙️ Nagranie mowy (PL)")
            tts_output = gr.Audio(label="🗣️ Synteza głosu (EN)", type="filepath")

            run_btn = gr.Button("▶️ Uruchom")

            run_btn.click(
                fn=full_pipeline,
                inputs=audio_input,
                outputs=[tts_output]
            )