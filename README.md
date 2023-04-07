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
Dane zostają również podzielone na dane treningowe, walidacyjne oraz testowe w proporcji 8:1:1
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

<h2>EN</h2>
<h3>Requirements</h3>
Python 3.6 or later, modules in requirements.txt
<h3>Problem description</h3>
Detection of A, B, C characters of American Sign Language. In addition, the model detects the lack of a sign.
<h3>Importing data</h3>
The data is imported from the "data" folder, which contains the subfolders "A", "B", "C", "0", respectively.
The image_dataset_from_directory() method from the keras.utils module was used to load the data. It allows you to easily import data, scale it to the required dimensions and divide it into batches.
<h3>Data preprocessing</h3>
The data is divided by the number 255 corresponding to the maximum value from the 8-bit RGB space.
The data is also divided into training, validation and test data in the 8:1:1 ratio
<h3>Creating a model</h3>
The model is created from convolutional layers - Conv2D, discretizing layers - MaxPooling2D, Dense connecting layers. In addition, a model responsible for data augmentation by random rotation of training data was added to the model.
The model was compiled using the RMSprop optimizer, the SparseCategoricalCrossentropy loss function and the Accuracy metric.
In addition, the model is saved or (if it exists) loaded from a file.
<h3>Accuracy and loss function</h3>
The graphs show the dependencies of the loss function and the accuracy of the training and validation data depending on the successive epochs
<h3>Calculation of metrics</h3>
Accuracy, Precision, Recall, and F1 metrics are calculated. The metrics are calculated over successive data series.
<h3>Results</h3>
10 random different pictures with random labels are shown.
The actual label and the label predicted by the model are shown.
<h3>Notes<h3>
<ul>
<li>The model was trained on 8 epochs, with more iterations, the model began to learn noise, which slightly decreased the accuracy</li>
<li>The model has been trained on an input of dimensions (300,300). Images with other dimensions are scaled to this character</li>
<li>Methods from the os.path module were used for taking path of files. This allows you to navigate through files without specializing your file system</li>
<li>The finished model can be downloaded from the link: https://drive.google.com/file/d/1prAAd1BhDwLMDxx7u9IW6Fzy4Ky6sdoG/view?usp=sharing</li>
</ul>
