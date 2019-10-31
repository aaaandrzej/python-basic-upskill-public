# Python Upskill - podstawowy

Do rozpoczęcia pracy niezbędne są pliki wejściowe, zawarte w katalogu `data`. Zakładamy, że dane wejściowe będą zgodne z danymi w tych plikach.

## Etapy / sprinty:

### 1. Stworzenie MVP (Minimum Viable Product)
#### Opis etapu:
W tym etapie należy stworzyć aplikację/skrypt, który:
- wczyta uczestników z pliku:
    - dopuszczamy dwa formaty `json` oraz `csv` 
- wylosuje wygranych spośród wczytanych uczestników
    - ilość zwycięzców powinna być sparametryzowana
- wydrukuje zwycięzców na ekran

#### wymagane techniki i biblioteki:
- kod powinien być podzielony na logicznie nazwane funkcje i moduły
- moduły ze standardowej biblioteki:
    - `pathlib`
    - `json`
    - `csv`
    
    
### 2. Rozszerzenie aplikacji o szablon loterii
#### Opis etapu:
W tym etapie należy rozszerzyć aplikację o:
- podział nagród pomiędzy zwycięzców zgodnie z wybranym szablonem z `data/lottery_templates`
- zapis wyników losowania:
    - zrozumiały dla użytkownika komunikat wypisywany na ekran
    - zapis do pliku, tylko format JSON
- uruchamianie aplikacji z linii poleceń z parametrami:
    - wskazanie pliku z uczestnikami wraz z jego formatem (domyślnie JSON)
    - wskazanie pliku z szablonem loterii (domyślnie pierwszy alfabetycznie w katalogu `data/lottery_templates`.
    - wskazanie pliku, do którego pisany będzie rezultat losowania (domyślnie `result.json`)
    
Ponatdo należy przygotować wirtualne środowisko używając `virtualenv` lub `pipenv` i w nim umieścić zależności aplikacji. 
    
#### wymagane techniki i biblioteki:
- `virtualenv` lub `pipenv`
- zewnętrzny pakiet `click` (https://click.palletsprojects.com)

### 3. Refaktor kodu z myślą o wprowadzeniu elementów programowania obiektowego, oraz wprowadzenie testów jednostkowych
W tym etapie należy zmodyfikować kod tak, aby aplikacja do wykonania swojego zadania wykorzystywała poniższe klasy/obiekty:
- obiekt klasy `Participant`, który przechowuje dane o uczestniku, pobrane z pliku.
- obiekt klasy `Prize`, który przechowuje dane o nagrodzie, pobrane z pliku.
- obiekt klasy `Lottery`, który przechowuje listę uczestników i listę nagród oraz potrafi dokonać losowania i wyprodukować wynik.

Ponadto, do aplikacji należy dołączyć testy jednostkowe napisanych funkcji i metod klas.

#### wymagane techniki i biblioteki:
- programowanie obiektowe
- zewnętrzny pakiet `pytest` (https://docs.pytest.org/en/latest/)


Powodzenia!

![](http://static.skaip.org/img/emoticons/180x180/f6fcff/hendance.gif)
 