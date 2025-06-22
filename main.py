from src.asr import ASR
from src.translation import TRANSLATOR
from src.tts import TTS
import gradio as gr
import os

OUTPUT_WAV_PATH = "output.wav"

# Przykładowe pliki audio do tabeli wyników
results_audio_pairs = [
    ("audio/witcher_en_2.wav", "audio/witcher_en_2.wav"),
    ("audio/witcher_en_2.wav", "audio/witcher_en_2.wav"),
    ("audio/witcher_en_2.wav", "audio/witcher_en_2.wav"),
]


def full_pipeline(audio_file):
    # 1. Transkrypcja z Whisper
    transcript = ASR.transcribe(audio_file)

    # 2. Tłumaczenie
    translation = TRANSLATOR.translate(transcript, source_lang="PL", target_lang="EN-US")

    # 3. Synteza (z użyciem głosu z tego samego audio)
    if os.path.exists(OUTPUT_WAV_PATH):
        os.remove(OUTPUT_WAV_PATH)

    TTS.synthesize(
        text=translation,
        reference_wav=audio_file,
        output_path=OUTPUT_WAV_PATH,
        language="en"
    )

    return transcript, translation, OUTPUT_WAV_PATH


with gr.Blocks(theme='Taithrah/Minimal') as demo:
    # Styl i logo
    gr.HTML("""
    <style>
    #logo-img img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 100%;
        max-width: 800px;
        height: auto;
    }
    </style>
    """)

    with gr.Row():
        with gr.Column():
            gr.Image("assets/logo.png", show_label=False, elem_id="logo-img")

    # Tytuł i opis (nad zakładkami)
    gr.Markdown("# 🎧 DubAI")
    gr.Markdown("Inteligentna platforma do transkrypcji, tłumaczenia i syntezy mowy – napędzana modelem Whisper i XTTS.")

    # Zakładki
    with gr.Tabs():
        
        # --- Transkrypcja + Tłumaczenie + TTS ---
        with gr.TabItem("🎙️ Transkrypcja"):
            gr.Markdown("## Transkrypcja mowy, tłumaczenie i synteza głosu")
            gr.Markdown("Wgraj swoje nagranie głosowe. Aplikacja transkrybuje je (PL), przetłumaczy na angielski i wygeneruje mowę w twoim głosie!")

            audio_input = gr.Audio(type="filepath", label="🎙️ Nagranie mowy (PL)")
            transcript_output = gr.Textbox(label="📄 Transkrypcja (PL)")
            translation_output = gr.Textbox(label="🌍 Tłumaczenie (EN)")
            tts_output = gr.Audio(label="🗣️ Synteza głosu (EN)", type="filepath")

            run_btn = gr.Button("▶️ Uruchom")

            run_btn.click(
                fn=full_pipeline,
                inputs=audio_input,
                outputs=[transcript_output, translation_output, tts_output]
            )

        # --- O projekcie ---
        with open("templates/about_project.md", "r", encoding="utf-8") as f:
            project_content = f.read()
        with open("templates/pipeline.md", "r", encoding="utf-8") as f:
            pipeline_content = f.read()
        with gr.TabItem("ℹ️ O projekcie"):
            gr.Markdown(project_content)
            gr.Image("assets/pipeline.png", show_label=False, width=1000)
            gr.Markdown(pipeline_content)


        # --- Wyniki ----
        with gr.TabItem("📊 Wyniki"):

            gr.Markdown("### Przykładowe nagrania")
            with gr.Row():
                gr.Markdown("#### Oryginał")
                gr.Markdown("#### Wygenerowany dubbing")

            for original_path, generated_path in results_audio_pairs:
                with gr.Row():
                    gr.Audio(original_path, type="filepath", label="Oryginał")
                    gr.Audio(generated_path, type="filepath", label="Wygenerowany")




        # --- Kontakt ---
        with open("templates/contact.md", "r", encoding="utf-8") as f:
            md_content = f.read()

        with gr.TabItem("📩 Kontakt"):
            gr.Markdown(md_content)

        
        with open("templates/about_us.md", "r", encoding="utf-8") as f:
            about_us = f.read()

        with gr.TabItem("👥 O nas"):
            gr.Markdown(about_us)

if __name__ == "__main__":
    demo.launch()
