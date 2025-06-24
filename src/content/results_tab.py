import gradio as gr
from pathlib import Path
from src.utils import get_base64_image


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
            gr.HTML("""
                <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                Poniżej przedstawiamy efekty naszego rozwiązania — przykładowe pary nagrań oryginalnych i wygenerowanych. Wśród nich znajdują się zarówno nagrania pojedyńczych wypowiedzi, jak i rozbudowane dialogi z muzyką w tle. Poszczególne wypowiedzi można odsłuchać, klikając na przycisk uruchamiający odtwarzacz audio.
                </div>
            """)
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

# WPŁYW KONTEKSTU NA TŁUMACZENIE

            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">🈲 Przykłady wpływu kontekstu na tłumaczenie</div>')
            gr.HTML("""
                    <div style="display:flex; gap:20px; flex-wrap: wrap; color:#000;">

                    <div style="flex:1; background-color:#f5f5f5; color:#000; border:2px solid black; border-radius:20px; padding:15px; min-width:300px;">
                    <h3 style="color:#000;">Przykład 1</h3>
                    <b>Dialog:</b><br>
                    <div style="background-color:#e0e0e0; border-radius:10px; padding:10px; margin-top:5px; margin-bottom:10px; color:#000;">
                    Troll &mdash; Ick metal. Mouth stings.<br>
                    Lambert &mdash; <b style="color:black;">You nuts?!</b><br>
                    Geralt &mdash; Shut up and follow my lead.
                    </div>
                    <b style="color:black;">Oryginalne:</b> Zwariowałeś?! ⭐<br>
                    <b style="color:black;">Bez kontekstu:</b> Ty orzeszku?! <span>❌</span><br>
                    <b style="color:black;">Z kontekstem:</b> <b style="color:black;">Czy ty zwariowałeś?!</b> ✅
                    </div>

                    <div style="flex:1; background-color:#f5f5f5; color:#000; border:2px solid black; border-radius:20px; padding:15px; min-width:300px;">
                    <h3 style="color:#000;">Przykład 2</h3>
                    <b>Dialog:</b><br>
                    <div style="background-color:#e0e0e0; border-radius:10px; padding:10px; margin-top:5px; margin-bottom:10px; color:#000;">
                    Yennefer &mdash; Philippa, your eyesight, only just recovered and magically simulated. Didn’t you say you’d need some time to get accustomed?<br>
                    Philippa Eilhart &mdash; <b style="color:black;">Did I?</b><br>
                    Yennefer &mdash; I’d forgotten how irritating she can be. Come, Ciri.
                    </div>
                    <b style="color:black;">Oryginalne:</b> Tak mówiłam? ⭐<br>
                    <b style="color:black;">Bez kontekstu:</b> Czy ja? <span style="color:black;">❌</span><br>
                    <b style="color:black;">Z kontekstem:</b> <b style="color:black;">Czy ja tak powiedziałam?</b> ✅
                    </div>
                    </div>

                    <br>

                    <div style="display:flex; gap:20px; flex-wrap: wrap; color:#000;">
                    <div style="flex:2; background-color:#f5f5f5; color:#000; border:2px solid black; border-radius:20px; padding:15px; min-width:300px;">
                    <h3 style="color:#000;">Przykład 3</h3>
                    <b>Dialog:</b><br>
                    <div style="background-color:#e0e0e0; border-radius:10px; padding:10px; margin-top:5px; margin-bottom:10px; color:#000;">
                    Chamberlain Emhyr &mdash; Bow before His Imperial Majesty, The White Flame Dancing on the Graves of his Foes, Emhyr var Emreis!<br>
                    Chamberlain Emhyr &mdash; <b style="color:black;">Bow.</b><br>
                    Emhyr &mdash; I thought you bowed before no man.<br>
                    </div>
                    <b style="color:black;">Oryginalne:</b> Ukłon. ⭐<br>
                    <b style="color:black;">Bez kontekstu:</b> Łuk. <span>❌</span><br>
                    <b style="color:black;">Z kontekstem:</b> <b style="color:black;">Ukłon.</b> ✅
                    </div>

                    <div style="flex:2; background-color:#f5f5f5; color:#000; border:2px solid black; border-radius:20px; padding:15px; min-width:300px;">
                    <h3 style="color:#000;">Przykład 4</h3>
                    <b>Dialog:</b><br>
                    <div style="background-color:#e0e0e0; border-radius:10px; padding:10px; margin-top:5px; margin-bottom:10px; color:#000;">
                    Keira Metz &mdash; Find him immediately. We’re close to unraveling this, I can feel it.<br>
                    Keira Metz &mdash; <b style="color:black;">What was that? It sounded for a moment like you’d joined the wraiths yourself...</b><br>
                    Geralt &mdash; Had to fight a pesta.<br>
                    </div>
                    <b style="color:black;">Oryginalne:</b> Co to było? Brzmiało, jakbyś postanowił dołączyć do drużyny upiorów... ⭐<br>
                    <b style="color:black;">Bez kontekstu:</b> Co to było? Brzmiało przez chwilę, jakbyś dołączył do cieni sam <span>❌</span><br>
                    <b style="color:black;">Z kontekstem:</b> <b style="color:black;">Co to było? Na chwilę brzmiało to tak, jakbyś sam dołączył do upiorów...</b> ✅
                    </div>
                    </div>
                    """)
            
            gr.HTML('<br><br>')
            
# MOS
            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">📋 Test MOS')
            gr.HTML("""
                <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                Jednym z najważniejszych wyznaczników jakości mowy syntetycznej jest opinia drugiego człowieka. W tym celu przeprowadziliśmy test MOS (ang. <i>Mean Opinion Score</i>), który polega na subiektywnej ocenie jakości dźwięku przez słuchaczy. W badaniu wzięło udział 63 uczestników, którzy mieli za zadanie wysłuchać fragmentów nagrań i ocenić je w skali od 1 do 5, gdzie 1 oznaczało bardzo niską jakość, a 5 bardzo wysoką. Sprawdzona została zarówno naturalność wygenerowanego dźwięku (nMOS), jak i jakość transferu cech mowy (sMOS).
                <br><br>
                W <a href="#mosTable">tabeli</a> przedstawiamy średnie wyniki testów nMOS i sMOS, zarówno dla tłumaczenia z języka angielskiego na polski, jak i odwrotnie. Rezultaty są w obu przypadkach na wysokim poziomie, aczkolwiek nieco gorsze wyniki uzyskano dla syntezy z języka angielskiego na polski. Wynika to głównie ze złożoności fleksyjnej języka polskiego oraz znacznie mniejszego wsparcia modeli dla tego języka. Na <a href="#nmos">wykresach</a> przedstawiono szczegółowy rozkład ocen dla nMOS i sMOS.
                </div>
                <br><br>
                <table id="mosTable" style="margin: 0 auto; border-collapse: collapse; max-width: 600px; width: 100%; font-size: 20px;">
                    <thead>
                        <tr style="border-bottom: 2px solid #000;">
                            <th style="padding: 10px;"></th>
                            <th style="padding: 10px;"><strong>EN &rarr; PL</strong></th>
                            <th style="padding: 10px;"><strong>PL &rarr; EN</strong></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid #ccc;">
                            <td style="padding: 10px;"><strong>nMOS</strong></td>
                            <td style="padding: 10px;">4,02</td>
                            <td style="padding: 10px;">4,38</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px;"><strong>sMOS</strong></td>
                            <td style="padding: 10px;">4,08</td>
                            <td style="padding: 10px;">4,51</td>
                        </tr>
                    </tbody>
                </table>
                <div style="text-align: center; font-size: 16px; font-family: Myriad, sans-serif; margin-top: 8px;">
                    Średnie wyniki testu MOS.
                </div>
                <style>
                    table tbody tr:hover {
                        background-color: #f0f0f0;
                    }
                </style>
            """)
            
            gr.HTML("""
            <style>
            .scaled-img-container {
                display: flex;
                justify-content: center;
                padding: 0.1em 0;
            }
            .scaled-img {
                transform-origin: top center;
            }
            </style>
            """)

            img_nmos = get_base64_image("assets/nmos.png")
            img_smos = get_base64_image("assets/smos.png")
            imgs_with_labels = f"""
            <div style="display: flex; justify-content: center; gap: 40px; flex-wrap: wrap; text-align: center;">
                <div>
                    <img id="nmos" src="{img_nmos}" class="scaled-img" alt="nmos" style="max-width: 100%; height: auto;" />
                    <div style="margin-top: 10px; font-size: 16px; font-family: Myriad, sans-serif;">Wyniki testu nMOS.</div>
                </div>
                <div>
                    <img id="smos" src="{img_smos}" class="scaled-img" alt="smos" style="max-width: 100%; height: auto;" />
                    <div style="margin-top: 10px; font-size: 16px; font-family: Myriad, sans-serif;">Wyniki testu sMOS.</div>
                </div>
            </div>
            """
            gr.HTML(imgs_with_labels)

                                