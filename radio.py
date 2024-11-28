import vlc
import time

# Funkcja do odtwarzania strumienia radiowego
def play_radio(player, url):
    media = instance.media_new(url)
    player.set_media(media)
    player.play()
    print(f"Odtwarzanie stacji: {url}")

# Funkcja do zatrzymania odtwarzania
def stop_radio(player):
    player.stop()
    print("Odtwarzanie zostało zatrzymane.")

# Tworzenie instancji VLC i odtwarzacza
instance = vlc.Instance()
player = instance.media_player_new()

# Przykładowy URL stacji radiowej
# Rock radio; RMF FM
radio_urls = ["https://radiostream.pl/tuba9004-1.mp3","http://195.150.20.244/rmf_fm",""]

# Przykładowy program
while True:
    print("\nMenu:")
    print("1-3 - Rozpocznij odtwarzanie wybranej stacji")
    print("0 - Zatrzymaj odtwarzanie")
    print("q - Wyjście")
    choice = input("Wybierz opcję: ")

    if choice == "0":
        stop_radio(player)
    elif choice == "q":
        print("Zamykam program.")
        break
    if int(choice) in range(1,4):
        play_radio(player, radio_urls[int(choice)-1])
    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")
