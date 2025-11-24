from datetime import datetime

# --- A Classe Memento ---
# Armazena o estado do Originador.
# Deve ser o mais simples possível (idealmente imutável).
class EditorMemento:
    def __init__(self, content: str):
        self._state = content
        self._timestamp = datetime.now() ## <- timestamp para representar momento salvo do snapshot. (não obrigatório)

    def get_saved_state(self) -> str: 
        # Este método é usado pelo Originador para se restaurar
        return self._state

    def get_info(self) -> str:
        # O Zelador pode ver metadados, mas não o estado em si
        return f"Memento salvo em {self._timestamp} (conteúdo oculto)"

# --- A Classe Originador ---
# Possui o estado real e sabe como salvar e restaurar a si mesmo.
class Editor:
    def __init__(self):
        self._content = "" # O estado interno
        print("Editor iniciado.")

    def type(self, text: str):
        print(f"Digitando: '{text}'")
        self._content += text
        self.show_content()

    def show_content(self):
        print(f"--- Conteúdo Atual: '{self._content}' ---")

    def save(self) -> EditorMemento:
        # Cria um Memento com o estado ATUAL
        print(f"Editor: Salvando estado atual no Memento...")
        return EditorMemento(self._content)

    def restore(self, memento: EditorMemento):
        # Restaura seu estado a partir de um Memento
        self._content = memento.get_saved_state()
        print(f"Editor: Estado restaurado com sucesso.")
        self.show_content()

# --- A Classe Zelador (Caretaker) ---
# Gerencia o histórico de Mementos. Não sabe o que há neles.
class History:
    def __init__(self, editor: Editor):
        self._mementos = [] # A pilha de "undo" (ctrl+z)
        self._editor = editor # Referência ao Originador
        print("Zelador (Histórico) pronto.")

    def make_backup(self):
        # Pede ao editor um memento e o guarda
        print("\nZelador: Pedindo backup para o Editor...")
        memento = self._editor.save()
        self._mementos.append(memento)
        print(f"Zelador: Backup salvo. {memento.get_info()}")

    def undo(self):
        if not self._mementos:
            print("\nZelador: Histórico vazio. Nada para desfazer.")
            return

        # Pega o último memento da pilha
        memento = self._mementos.pop()
        
        print(f"\nZelador: Solicitando 'Undo'...")
        print(f"Zelador: Restaurando estado de {memento.get_info()}")
        
        try:
            # Entrega o memento ao editor para que ele se restaure
            self._editor.restore(memento)
        except Exception as e:
            print(f"Zelador: Falha ao restaurar! {e}")
            # Se falhar, devolve o memento à pilha
            self._mementos.append(memento)

# --- O Fluxo de Uso ---

# Configuração inicial
editor_principal = Editor()
historico = History(editor_principal)

# 1. Usuário digita e salva
editor_principal.type("Olá, ")
historico.make_backup() # Salva "Olá, "

# 2. Usuário digita mais e salva
editor_principal.type("Mundo!")
historico.make_backup() # Salva "Olá, Mundo!"

# 3. Usuário digita algo que vai se arrepender
editor_principal.type(" (Isso é um erro)")

# 4. Usuário pede "Desfazer" (Undo)
historico.undo()
# O editor deve voltar para "Olá, Mundo!"

# 5. Usuário pede "Desfazer" (Undo) novamente
historico.undo()
# O editor deve voltar para "Olá, "

# 6. Usuário pede "Desfazer" mais uma vez
historico.undo()
# O histórico deve informar que está vazio