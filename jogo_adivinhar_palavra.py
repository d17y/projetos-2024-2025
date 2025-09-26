import random
import time


print('******************************************')
print('----Bem vindos ao jogo da adivinhação----')
print('******************************************')

time.sleep(1)
print('Esse é um jogo igual o da forca')
time.sleep(1)
print("Mas o tema é de POKÉMON!")
time.sleep(1)
print("Lembrando que é só os 151 primeiros <:")
time.sleep(1)
print("BOA SORTE!!!")
time.sleep(1)
print("...Estou escolhendo o pokémon...")
time.sleep(2)
print(".")
time.sleep(2)
print(".")
time.sleep(2)
print(".")

pokemon_escolhido = [  "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot",
    "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok",
    "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina",
    "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable",
    "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat",
    "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat",
    "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck",
    "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag",
    "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop",
    "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool",
    "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash",
    "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch’d", "Doduo",
    "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder",
    "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee",
    "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute",
    "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung",
    "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela",
    "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu",
    "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar",
    "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto",
    "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte",
    "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno",
    "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo",
    "Mew"]

# Escolher o pokémon e deixar ele em minúsculo
pokemon = random.choice(pokemon_escolhido).lower()
letras_acertadas = []

# print(pokemon)  # Descomente para debugar a palavra sorteada

letra_errada = 0
while True:
    exibicao = ""
    for letra in pokemon:
        if letra in letras_acertadas or not letra.isalpha():
            exibicao += letra  # Mostra letras acertadas ou símbolos como '.
        else:
            exibicao += "_"
    time.sleep(2)
    print(f"Você errou {letra_errada}x")  
    time.sleep(1)
    print("QUAL É ESSE POKÉMON?:", exibicao)

    if "_" not in exibicao:
        time.sleep(2)
       
        time.sleep(2)
        print(f"ÉÉÉ o {pokemon}")
        break

    tentativa = input("Digite uma letra: ").lower()

    if len(tentativa) != 1 or not tentativa.isalpha():
        time.sleep(2)
        print("Por favor, digite apenas UMA letra válida.")
        continue

    if tentativa in letras_acertadas:
        time.sleep(2)
        print("Você já tentou essa letra.")
        continue

    if tentativa in pokemon:
        letras_acertadas.append(tentativa)
        time.sleep(2)
      
        print("\033[32mBoa! Letra correta.\033[0m")

    else:

        letra_errada+=1
        time.sleep(2)
        print("\033[31mLetra Errada. Tente Novamente.\033[0m")


