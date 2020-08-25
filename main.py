import pygame, sys

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

pygame.init()

DISPLAY_SURF = pygame.display.set_mode(
    (800, 600))  # tworzy powierzchnię (okienko gry)
BASIC_FONT = pygame.font.Font('freesansbold.ttf', 18)
CLOCK = pygame.time.Clock(
)  # tworzy nowy obiekt zegara który może być użyty do śledzenia upływu czasu
pygame.display.set_caption(
    'Weselny Pyton')  # tworzy napis wyświetlany na górnym pasku

while True:  # Main game loop
    for event in pygame.event.get(
    ):  # ta funkcja bierze i usuwa wiadomości z kolejki (można w argumencie funkcji zadać typ który jako jedyny ma być obsługiwany)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    DISPLAY_SURF.fill(
        (255, 255, 255)
    )  # funkcją display utworzyłem obiekt Surface - fill to metoda dla obiektu Surface która wypełnia powierzchnię okna jednolitym kolorem
    pygame.display.update(
    )  # metoda która odświeża wyświetlane okno - w mojej pętli będzie odświeżana za każdym zdarzeniem
    CLOCK.tick(
        60
    )  # ustala ilość cyknięć w milisekundach, w moim przypadku determinuje to że gra będzie działać w 60 klatkach na sekundę
