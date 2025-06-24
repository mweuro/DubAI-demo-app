import gradio as gr
from pathlib import Path


def get_files(dir_name):
    path = Path(__file__).resolve().parents[2] / 'examples' / dir_name
    files = sorted(path.glob("*.wav"))
    return files

ORIGINAL = get_files('original')
GENERATED = get_files('generated')

def results_tab():
    with gr.Tab("📊 Wyniki"):
        with gr.Column(elem_classes="results-tab"):
            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">🎵 Przykłady dubbingu</div>')
            with gr.Row():
                gr.HTML('<div style="font-size: 20px; font-family: Myriad, sans-serif; font-weight: bold; text-align: center;">Oryginalne nagranie</div>')
                gr.HTML('<div style="font-size: 20px; font-family: Myriad, sans-serif; font-weight: bold; text-align: center;">Wygenerowany dubbing</div>')
            for file1, file2 in zip(ORIGINAL, GENERATED):
                with gr.Row():
                    with gr.Column():
                        gr.Audio(file1, label='Oryginał', type="filepath")
                    with gr.Column():
                        gr.Audio(file2, label='Wygenerowany', type="filepath")
            
            gr.HTML('<br><br>')

            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">Przykłady wpływu kontekstu na tłumaczenie</div>')
            gr.HTML("""
                    <div style="display:flex; gap:20px; flex-wrap: wrap; color:#000;">

                    <div style="flex:1; background-color:#f5f5f5; color:#000; border:2px solid black; border-radius:20px; padding:15px; min-width:300px;">
                    <h3 style="color:#000;">Przykład 1</h3>
                    <b>Dialog:</b><br>
                    <div style="background-color:#e0e0e0; border-radius:10px; padding:10px; margin-top:5px; margin-bottom:10px; color:#000;">
                    Troll - Ick metal. Mouth stings.<br>
                    Lambert - <b style="color:black;">You nuts?!</b><br>
                    Geralt - Shut up and follow my lead.
                    </div>
                    <b style="color:black;">Oryginalne:</b> Zwariowałeś?! ⭐<br>
                    <b style="color:black;">Bez kontekstu:</b> Ty orzeszku?! <span>👎</span><br>
                    <b style="color:black;">Z kontekstem:</b> <b style="color:black;">Czy ty zwariowałeś?!</b> ✅
                    </div>

                    <div style="flex:1; background-color:#f5f5f5; color:#000; border:2px solid black; border-radius:20px; padding:15px; min-width:300px;">
                    <h3 style="color:#000;">Przykład 2</h3>
                    <b>Dialog:</b><br>
                    <div style="background-color:#e0e0e0; border-radius:10px; padding:10px; margin-top:5px; margin-bottom:10px; color:#000;">
                    Yennefer - Philippa, your eyesight, only just recovered and magically simulated. Didn’t you say you’d need some time to get accustomed?<br>
                    Philippa Eilhart - <b style="color:black;">Did I?</b><br>
                    Yennefer - I’d forgotten how irritating she can be. Come, Ciri.
                    </div>
                    <b style="color:black;">Oryginalne:</b> Tak mówiłam? ⭐<br>
                    <b style="color:black;">Bez kontekstu:</b> Czy ja? <span style="color:black;">👎</span><br>
                    <b style="color:black;">Z kontekstem:</b> <b style="color:black;">Czy ja tak powiedziałam?</b> ✅
                    </div>
                    </div>
                    """)


                                