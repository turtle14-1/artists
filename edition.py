import random
import time

print("\nEditionsbox AUSPACKEN \n_____________________\n")

artists =  ["Alder Noldi",
            "Alder Ueli",
            "Berweger David", 
            "Berweger Zora",
            "Böniger Nicole",
            "Bühler Karin Karinna", 
            "Bürki Urs",
            "Finger Michael", 
            "Fricker HR",
            "Gatsas Georg",
            "Graf Florian",
            "Graf Rolf",
            "Graf Sarah", 
            "Häusermann Pascal",
            "Hörler Christian",
            "Keller Katrin",
            "Kopainig Aurelio", 
            "Krapf Gabriela", 
            "Liechti Peter", 
            "Müller Markus", 
            "Osterwalder Pascale",
            "Palla Ursula", 
            "Rekade Nora", 
            "Schnyder Rebecca C.", 
            "Sierra Francisco", 
            "Signer Stefan",
            "Slamanig Monika", 
            "Stoffel Peter",
            "Stricker Thomas", 
            "Sturzenegger Miriam", 
            "Stüssi Thomas",
            "Suhner Reto",
            "Vece Costa Mauro", 
            "Walser Pablo",
            "Wen-Ching Wang", 
            "Sabine Widmer Birgit"] 

random.shuffle(artists)


i = 0
while i < len(artists):
    print(random.choice(artists) + "")
    i +=1
    time.sleep(60)

print("\n----------------------------\nDANKE für die Aufmerksamkeit\n")