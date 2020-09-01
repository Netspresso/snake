import pygame, sys
from game import Game

# stworzenie okna
# aktualizacja logiki gry
# obsłużyć dane wejściowe
# użyć danych by wygenerować grafikę

# wyczyszczenie ekarnu
# aktualizacja gry
# rozpoczęcie gry
'''
Zasady gry:
    Game Over:
        - gdy wąż dotknie ściany
        - gdy wąż się ugryzie
    Poruszanie się węża:
        - kierunek zmienia głowa, ogon ciągnie się za głową nie zachaczając o inne punkty niż zachaczyła głowa
    Wąż:
        - po zjedzeniu jabłka rośnie o jeden
    Wynik:
        - ile jabłek zjadł wąż
    Menu:
        - pokazuje się raz na początku gry
        - znika przy naciśnieciu dowolnego klawisza
        - pojawia się po porażce w grze
    Klawisze:
    - strzałki do sterowania wężem
'''
'''
Co jest stałą w grze?
- kolory
- wymiary okna
- rozmiar komórek w grze
- częstotliwość wyświetlania klatek
'''


def main():
    game = Game()
    game.run()
    sys.exit()


if __name__ == '__main__':
    main()