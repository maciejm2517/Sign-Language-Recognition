# Sign-Language-Recognition
<h2>PL</h2>
<h3>Wymagania</h3>
Python 3.6 lub nowszy, moduły w pliku requirements.txt
<h3>Opis problemu</h3>
Wykrywanie znaków A, B, C Amerykańskiego Języka Migowego. Dodatkowo model wykrywa brak znaku.
<h3>Importowanie danych</h3>
Dane zostają importowane z folderu "data", który zawiera odpowiednio podfoldery "A", "B", "C", "0".
Do załadowania danych została wykorzystana metoda image_dataset_from_directory() z modułu keras.utils. Pozwala z łatwy sposób importować dane, przeskalować na wymagane wymiary oraz podzielić na partie (ang. batches).
<h3>Wstępne przetwarzanie danych</h3>
Dane zostają podzielone przez liczbę 255 odpowiadającą maksymalną wartością z 8 bitowej przestrzeni RGB.
Dane zostają również na podzielone dane treningowe, walidacyjne oraz testowe w proporcji 8:1:1
<h3>Utworzenie modelu</h3>
Model zostaje utworzony z warstw splotowych - Conv2D, warstw dyskretyzujących - MaxPooling2D, warstw łączących Dense. Dodatkowo do modelu został dodany model odpowiadający za augmentacje danych przez losowe obracanie danych treningowych.
Model został skompilowany za pomocą optymalizatora RMSprop, funkcji strat SparseCategoricalCrossentropy oraz metryki Accuracy.
Dodatkowo model jest zapisywany lub (jeśli istnieje) ładowany z pliku.
<h3>Dokładność i funkcja strat</h3>
Wykresy pokazują zależności funkcji strat oraz dokładności danych treningowych oraz walidacyjnych w zależności od kolejnych epok
<h3>Obliczanie metryk</h3>
Obliczane są metryki dokładności, precyzji, czułości (ang. recall) oraz F1. Metryki są obliczane w kolejnych seriach danych.
<h3>Wyniki</h3>
Pokazywane jest 10 losowych obrazków różnych o losowych etykietach.
Pokazywana jest rzeczywista etykieta oraz etykieta przewidziana przez model.
<h3>Uwagi<h3>
<ul>
<li>Model został wytrenowany na 8 epokach, przy większej ilości iteracji model zaczynał uczyć się szumu przez co dokładność nieznacznie spadała</li>
<li>Model został wytrenowany na dane wejściowe o wymiarach (300,300). Obrazy o innych wymiarach są skalowane do tej postaci</li>
<li>Do pobierania plików z folderów zostały wykorzystane metody z modułu os.path. Umożliwia to poruszanie się po plikach bez specjalizowania systemu plików użytkownika</li>
<li>Gotowy model można pobrać z linku: https://drive.google.com/file/d/1prAAd1BhDwLMDxx7u9IW6Fzy4Ky6sdoG/view?usp=sharing</li>
</ul>
