import gradio as gr

def about_tab():
    with gr.TabItem("ℹ️ O projekcie"):
        with gr.Column():
            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">🎮 Motywacja</div>')
            gr.HTML("""
                <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                Podczas analizy recenzji gier publikowanych na popularnych serwisach, wielokrotnie natrafialiśmy na głosy graczy wyrażających niezadowolenie z braku polskiego dubbingu w produkcjach zagranicznych. Wielu z nich podkreślało, że brak lokalizacji głosowej negatywnie wpływa na immersję i znacznie obniża jakość doświadczenia płynącego z rozgrywki. Zaintrygowani tym problemem postanowiliśmy zgłębić temat. Nasze obserwacje potwierdziły, że główną barierą we wdrażaniu lokalizacji na mniejsze rynki takie jak polski są wysokie koszty oraz długi czas realizacji. W odpowiedzi na tę lukę rynkową podjęliśmy decyzję o stworzeniu systemu do automatycznego generowania dubbingu w języku polskim z wykorzystaniem AI.
                </div>
            """)

            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">🎯 Cel</div>')
            gr.HTML("""
                <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                Celem naszego projektu jest dostarczenie rozwiązania, które znacząco obniży koszty lokalizacji oraz skróci czas jej realizacji, jednocześnie zachowując wysoką jakość audio i naturalność wypowiedzi.
                </div>
            """)

            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">🛠️ Architektura</div>')
            gr.HTML("""
                <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                Aby osiągnąć nasz cel, opracowaliśmy modularną architekturę systemu umożliwiającego generowanie dubbingu z użyciem nowoczesnych modeli AI. Cały proces został podzielony na trzy główne etapy: przetwarzanie wstępne, tłumaczenie oraz generowanie dźwięku. Każdy z tych komponentów działa niezależnie, co pozwala na łatwą modyfikację lub wymianę modelu na bardziej zaawansowany bez konieczności przebudowy całego potoku przetwarzania.
                </div>
            """)

