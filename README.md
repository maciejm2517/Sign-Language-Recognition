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
Dane zostają również na dane treningowe, walidacyjne oraz testowe w proprcji 8:1:1
<h3>Utworzenie modelu</h3>
Model zostaje utworzony z wartstw splotowych - Conv2D(), wartstw dyskretyzujących - MaxPooling2D(), warstw łączących Dense(). Dodatkowo do modelu został dodany model odpowiadający za augmentacje danych przez losowe obracanie danych treningowych.
Model został skompilowany za pomocą optymalizatora RMSprop(), funkcji strat SparseCategoricalCrossentropy() oraz metryki Accuracy().
Dodatkowo gdy model jest zapisywany lub (jeśli istnieje) jest ładowany z pliku.
