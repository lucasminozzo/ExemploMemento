# Este é o código de um jogo em que há a possibilidade de realizar o carregamento de um Save antigo...    
# Finalize o código com os requisitos necessários para que o padrão Memento seja aplicado corretamente:


# --- O MEMENTO ---
# Esta classe vai armazenar o estado.
class SaveState:
    def __init__(self, vida: int, mana: int, posicao: tuple):
        # O Memento armazena os dados do estado
        self._vida = vida
        self._mana = mana
        self._posicao = posicao
        print(f" (Memento criado: Vida={self._vida}, Mana={self._mana})")

    # O Originador (Jogador) precisa de getters para se restaurar
    def get_vida(self) -> int:
        return self._vida
    
    def get_mana(self) -> int:
        return self._mana

    def get_posicao(self) -> tuple:
        return self._posicao

# --- O ORIGINADOR ---
# O Jogador possui o estado real.
class Jogador:
    def __init__(self, nome: str):
        self._nome = nome
        self._vida = 100
        self._mana = 50
        self._posicao = (0, 0) # (x, y)
        print(f"Jogador '{self._nome}' criado.")
        self.mostrar_status()

    def mostrar_status(self):
        print(f"--- STATUS [{self._nome}]: Vida={self._vida}, Mana={self._mana}, Pos={self._posicao} ---")

    def andar(self, x: int, y: int):
        self._posicao = (self._posicao[0] + x, self._posicao[1] + y)
        print(f"{self._nome} andou para {self._posicao}")

    def receber_dano(self, dano: int):
        self._vida -= dano
        print(f"{self._nome} recebeu {dano} de dano! Vida restante: {self._vida}")

    # REQUISITO 1: Implemente o método de salvar
    def cria_memento(self) -> SaveState:
        ...

    # REQUISITO 2: Implemente o método de restaurar
    def restaurar(self, memento: SaveState):
        ...


# --- O ZELADOR (CARETAKER) ---
# Gerencia o histórico de saves, mas não sabe o que há neles.
class GerenciadorDeSaves:
    def __init__(self, jogador: Jogador):
        self._jogador = jogador
        self._checkpoint = None # Armazena apenas UM memento (o último checkpoint)
        print("Gerenciador de Saves pronto.")

    # REQUISITO 3: Implemente o salvamento
    def salvar_checkpoint(self):
        ...

    # REQUISITO 4: Implemente o carregamento
    def carregar_checkpoint(self):
        ...
# --- FLUXO DE TESTE (Para você verificar sua implementação) ---

print("--- Início da Aventura ---")
jogador1 = Jogador("Herói")
gerenciador = GerenciadorDeSaves(jogador1)

# 1. Jogador chega ao primeiro checkpoint
gerenciador.salvar_checkpoint()

# 2. Jogador explora e se machuca
jogador1.andar(10, 5)
jogador1.receber_dano(30)
jogador1.mostrar_status()

# 3. Jogador encontra outro checkpoint
gerenciador.salvar_checkpoint()

# 4. Jogador entra em uma batalha difícil
jogador1.andar(5, 5)
jogador1.receber_dano(75)

# 5. O jogador "morre" ou decide recarregar
print("\n... O jogador foi derrotado! ...")
gerenciador.carregar_checkpoint()

# 6. Verifique o status. O jogador deve ter 70 de vida e estar na posição (10, 5)
print("\n--- Verificação Final ---")
jogador1.mostrar_status()