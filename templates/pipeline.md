## ⚙️ Przetwarzanie wstępne
Proces rozpoczyna się od oczyszczenia nagrań z zakłóceń tła przy użyciu modelu Demucs, który skutecznie wydziela sygnał mowy. Następnie zastosowano Mossformer2 do separacji mówców, co pozwala rozdzielić wypowiedzi różnych osób w nagraniu. Kolejnym krokiem jest transkrypcja i segmentacja audio za pomocą modelu Whisper, znanego z wysokiej jakości rozpoznawania mowy. Otrzymane wypowiedzi są grupowane przy użyciu algorytmu DBSCAN, co umożliwia identyfikację spójnych segmentów konwersacyjnych.

<br>

## 🔄 Tłumaczenie
Do tłumaczenia wykorzystano polski wielojęzyczny model językowy Bielik, który efektywnie przekłada teksty zachowując ich znaczenie. Unikalnym aspektem naszego podejścia jest uwzględnianie kontekstu w postaci sąsiadujących fragmentów dialogu — zarówno wypowiedzi poprzedzających, jak i następujących po tłumaczonym fragmencie. Jakość tłumaczeń jest oceniana automatycznie za pomocą metryk takich jak COMET, BERTScore i BLEU, które zapewniają obiektywną ocenę pod kątem zgodności semantycznej oraz płynności tłumaczonego tekstu. 

### Przykłady wpływu kontekstu na tłumaczenie

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

<br>

## 🔊 Generacja dźwięku
Synteza mowy realizowana jest przy użyciu modelu XTTS-v2, obsługującego 17 języków i umożliwiającego generowanie naturalnego głosu na podstawie jedynie 6-sekundowego nagrania referencyjnego. Model ten został wybrany ze względu na wysoką jakość dźwięku, szybkie działanie oraz lepszą kompatybilność z językiem polskim niż inne dostępne rozwiązania.

