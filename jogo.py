class Player:
    def __init__(self):
        self.inventory = []
        self.score = 0
        self.alive = True

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"[INVENTÁRIO] Você pegou: {item}")

    def has_item(self, item):
        return item in self.inventory

    def add_score(self, points):
        self.score += points
        print(f"[+{points} pontos] Pontuação atual: {self.score}")


def start_game():
    print("=== A MALDIÇÃO DO TEMPLO ESQUECIDO ===")
    player = Player()
    continuar = entrada_templo(player)

    print("\n=== FIM DO JOGO ===")
    print(f"🎯 Sua pontuação final: {player.score}")


def entrada_templo(player):
    print("\nVocê acorda em uma sala escura. Há uma tocha na parede e duas saídas.")
    print("1) Pegar a tocha")
    print("2) Ignorar e sair pela porta")

    escolha = input("> ")

    if escolha == "1":
        player.add_item("tocha")
        player.add_score(10)
    else:
        print("Você tropeça no escuro e bate a cabeça. Fim prematuro.")
        return False

    return corredor(player)


def corredor(player):
    print("\nVocê entra em um corredor com uma bifurcação.")
    print("Um espírito aparece flutuando em frente à bifurcação.")

    dialogo_npc()

    print("1) Ir para a esquerda (luz fraca)")
    print("2) Ir para a direita (cheiro estranho)")
    escolha = input("> ")

    if escolha == "1":
        return sala_espelhos(player)
    else:
        return sala_serpente(player)


def dialogo_npc():
    print("\n👻 Espírito: 'Nem tudo é o que parece... Às vezes, a luz revela o caminho.'")
    print("👻 Espírito: 'Ah, e cuidado com o que pisa. Nem todos os caminhos levam à saída.'")


def sala_espelhos(player):
    print("\nVocê entra em uma sala cheia de espelhos. Há uma inscrição antiga:")
    print("\"Só quem decifrar o enigma encontrará o caminho.\"")
    print("Inscrição: 'Tenho cidades, mas não casas; montanhas, mas não árvores; e água, mas não peixes. O que sou eu?'")

    resposta = input("Digite sua resposta: ").strip().lower()

    if resposta == "mapa":
        print("A parede se abre! Você resolveu o enigma!")
        player.add_score(30)

        if player.has_item("tocha"):
            print("A tocha ilumina uma passagem secreta que leva à saída.")
            print("✨ FINAL BOM: Você escapou com sabedoria e um mapa antigo!")
            player.add_score(50)
        else:
            print("Você avança na escuridão, mas eventualmente acha a saída às cegas.")
            print("✨ FINAL NEUTRO: Sobreviveu, mas perdeu relíquias valiosas.")
            player.add_score(20)
    else:
        print("Nada acontece... Você fica preso na sala para sempre.")
        print("💀 FINAL RUIM: Preso para sempre.")
        player.add_score(-10)

    return False


def sala_serpente(player):
    print("\nVocê entra em uma sala com uma enorme serpente adormecida.")
    print("1) Tentar passar sem acordá-la")
    print("2) Atacar a serpente")

    escolha = input("> ")

    if escolha == "1":
        print("Você pisa em um osso seco... a serpente acorda e te devora.")
        print("💀 FINAL RUIM: Morto pela serpente.")
        player.add_score(-20)
    else:
        if player.has_item("tocha"):
            print("Você queima a serpente com a tocha! Uma porta se abre.")
            print("✨ FINAL NEUTRO: Escapou ferido, mas sobreviveu.")
            player.add_score(25)
        else:
            print("Você está desarmado e é devorado.")
            print("💀 FINAL RUIM: Morto pela serpente.")
            player.add_score(-15)

    return False


if __name__ == "__main__":
    start_game()
