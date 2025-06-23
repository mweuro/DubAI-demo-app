import gradio as gr
from src.utils import get_base64_image

def method_tab():
    with gr.Tab("⚙️ Metoda"):
        with gr.Column(elem_classes="method-tab"):
            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">⚙️ Metoda</div>')

            gr.HTML("""
                <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                Proces rozpoczęto od oczyszczenia nagrań z zakłóceń tła przy użyciu modelu Demucs, który umożliwił skuteczne wydzielenie sygnału mowy. Następnie zastosowano Mossformer2 do separacji mówców, co pozwoliło rozdzielić wypowiedzi różnych osób w nagraniu. Transkrypcja i segmentacja audio zostały przeprowadzone za pomocą modelu Whisper, znanego z wysokiej jakości rozpoznawania mowy. Otrzymane wypowiedzi pogrupowano przy użyciu algorytmu DBSCAN, co ułatwiło identyfikację spójnych segmentów konwersacyjnych.
                <br><br>
                Do tłumaczenia wykorzystano polski wielojęzyczny model językowy Bielik, który efektywnie przekłada teksty zachowując ich znaczenie. Unikalnym aspektem naszego podejścia jest uwzględnianie kontekstu w postaci sąsiadujących fragmentów dialogu — zarówno wypowiedzi poprzedzających, jak i następujących po tłumaczonym fragmencie. Jakość tłumaczeń jest oceniana automatycznie za pomocą metryk takich jak COMET, BERTScore i BLEU, które zapewniają obiektywną ocenę pod kątem zgodności semantycznej oraz płynności tłumaczonego tekstu. 
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
            
        