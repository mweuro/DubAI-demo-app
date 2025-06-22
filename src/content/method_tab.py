import gradio as gr
from src.utils import get_base64_image

def method_tab():
    with gr.Tab("⚙️ Metoda"):
        with gr.Column(elem_classes="method-tab"):
            gr.HTML('<div style="font-size: 40px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">⚙️ Metoda</div>')

            gr.HTML("""
                <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                Proces rozpoczęto od oczyszczenia nagrań z zakłóceń tła przy użyciu modelu Demucs, który umożliwił skuteczne wydzielenie sygnału mowy. Następnie zastosowano Mossformer2 do separacji mówców, co pozwoliło rozdzielić wypowiedzi różnych osób w nagraniu. Transkrypcja i segmentacja audio zostały przeprowadzone za pomocą modelu Whisper, znanego z wysokiej jakości rozpoznawania mowy. Otrzymane wypowiedzi pogrupowano przy użyciu algorytmu DBSCAN, co ułatwiło identyfikację spójnych segmentów konwersacyjnych.
                <br><br>
                Do tłumaczenia wykorzystano polski wielojęzyczny model językowy Bielik, który dobrze radzi sobie z przekładem tekstów. Jakość tłumaczeń oceniano przy użyciu metryk COMET, BERTScore i BLEU, zapewniających obiektywną ocenę pod względem zgodności semantycznej i płynności.
                <br><br>
                Syntezę mowy zrealizowano przy użyciu modelu XTTS-v2, obsługującego 17 języków i umożliwiającego generowanie naturalnego głosu na podstawie jedynie 6-sekundowego nagrania referencyjnego. Został on wybrany ze względu na dobrą jakość dźwięku, szybkość działania oraz lepszą kompatybilność z językiem polskim niż inne dostępne modele. Na końcu przeprowadzono subiektywną ocenę końcowego dźwięku w formie testów odsłuchowych.
                <br><br>
                Na poniższym schemacie przedstawiono szczegółowy przebieg procesu.
                </div>
            """)

            img_data = get_base64_image("assets/schema.png")
            schema_html = f"""
            <div style="display: flex; justify-content: center; padding: 20px;">
                <img src="{img_data}" 
                    style="
                        width: 100%;
                        max-width: 1000px;
                        border: none;
                        object-fit: contain;
                    " 
                    alt="Schemat procesu"
                />
            </div>
            """
            gr.HTML(schema_html)
            gr.HTML('<div style="text-align: center; font-size: 18px; font-family: Myriad, sans-serif;"><strong>Schemat 1.</strong> Przebieg procesu przetwarzania nagrania.</div>')
            
            gr.HTML('<div style="font-size: 40px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">📊 Wyniki</div>')

            gr.HTML('<div style="font-size: 40px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">🎵 Nagrania przykładowe</div>')
            with gr.Row():
                with gr.Column():
                    gr.Audio("examples/0x000f7780.wav", label="Nagranie 1", type="filepath")
                with gr.Column():
                    gr.Audio("examples/0x000faf94.wav", label="Nagranie 2", type="filepath")
            with gr.Row():
                with gr.Column():
                    gr.Audio("examples/0x0006de19.wav", label="Nagranie 3", type="filepath")
                with gr.Column():
                    gr.Audio("examples/0x0008d8e5.wav", label="Nagranie 4", type="filepath")
            with gr.Row():
                with gr.Column():
                    gr.Audio("examples/0x0011ce99.wav", label="Nagranie 5", type="filepath")
                with gr.Column():
                    gr.Audio("examples/0x0011cedc.wav", label="Nagranie 6", type="filepath")
            with gr.Row():
                with gr.Column():
                    gr.Audio("examples/dialogue_1.wav", label="Dialog 1", type="filepath")
                with gr.Column():
                    gr.Audio("examples/dialogue_9.wav", label="Dialog 2", type="filepath")
