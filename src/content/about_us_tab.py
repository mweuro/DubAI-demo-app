import gradio as gr


def about_us_tab():
    with gr.Tab("👥 O nas"):
        with gr.Column():
            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">👥 O nas</div>')

            gr.HTML("""
                <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                Jesteśmy studentami kierunku Sztuczna Inteligencja na Politechnice Wrocławskiej.  Projekt DubAI zrealizowaliśmy w ramach zajęć, łącząc naszą pasję do gier komputerowych z chęcią zdobywania nowych umiejętności i pogłębiania wiedzy z zakresu przetwarzania dźwięku i języka naturalnego. Naszym celem było stworzenie narzędzia do generowania dubbingu do gier komputerowych, ze szczególnym uwzględnieniem języka polskiego. Pragniemy dzięki temu zapewnić użytkownikom większą immersję oraz satysfakcję z gry.
                <br><br>
                W skład zespołu wchodzą: Natalia Iwańska, Klaudia Janicka, Wiktor Jeżowski, Kajetan Kołodziejczyk oraz Michał Wiktorowski. 
                <br>
                Opiekunami projektu są dr hab. inż. Maciej Piasecki oraz dr inż. Piotr Syga.
                </div>
            """)

            gr.HTML('<div style="font-size: 35px; font-family: Myriad, sans-serif; font-weight: bold; text-align: left;">📩 Kontakt</div>')

            gr.HTML("""
                <div style="font-size: 18px; font-family: Myriad, sans-serif;">
                <ul>
                <li>
                    Natalia Iwańska 📧
                    <a href="mailto:262270@student.pwr.edu.pl">262270@student.pwr.edu.pl</a>
                </li>
                <li>
                    Klaudia Janicka 📧
                    <a href="mailto:262268@student.pwr.edu.pl">262268@student.pwr.edu.pl</a>
                </li>
                <li>
                    Wiktor Jeżowski 📧
                    <a href="mailto:260426@student.pwr.edu.pl">260426@student.pwr.edu.pl</a>
                </li>
                <li>
                    Kajetan Kołodziejczyk 📧
                    <a href="mailto:259171@student.pwr.edu.pl">259171@student.pwr.edu.pl</a>
                </li>
                <li>
                    Michał Wiktorowski 📧
                    <a href="mailto:262330@student.pwr.edu.pl">262330@student.pwr.edu.pl</a>
                </li>
                </ul>
                </div>
            """)


