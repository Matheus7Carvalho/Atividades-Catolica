class Book:
    def __init__(self, title, author, book_type, min_age, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.min_age = min_age
        self.pages = pages

    def __gt__(self, other):
        if isinstance(other, Book): return self.title.lower() > other.title.lower()
        return self.title.lower() > str(other).lower()

    def __lt__(self, other):
        if isinstance(other, Book): return self.title.lower() < other.title.lower()
        return self.title.lower() < str(other).lower()

    def __eq__(self, other):
        if isinstance(other, Book): return self.title.lower() == other.title.lower()
        return self.title.lower() == str(other).lower()
    
    def __str__(self):
        return f"[{self.title}] Autor: {self.author} | Tipo: {self.book_type} | {self.min_age}+ anos | {self.pages} págs"

class Node:
    def __init__(self, content):
        self.left: Node = None   
        self.right: Node = None
        self.content: Book = content
    
class Tree:
    def __init__(self):
        self.root: Node = None
    
    def add(self, content, root = None):
        if self.root is None:
            self.root = Node(content)
            return
        
        if root is None:
            root = self.root
        
        if content > root.content:
            if (root.right is None):
                root.right = Node(content)
            else:
                self.add(content, root.right)
        else:
            if (root.left is None):
                root.left = Node(content)
            else:
                self.add(content, root.left)

    def printTree(self, root=None, filter_attr=None, filter_value=None):
        if root is None and self.root is not None:
            root = self.root
        
        if root:
            if root.left: self.printTree(root.left, filter_attr, filter_value)
            
            book = root.content
            if filter_attr is None:
                print(f" - {book}")
            else:
                val = getattr(book, filter_attr)
                if str(val).lower() == str(filter_value).lower():
                    print(f" [ENCONTRADO] {book}")
            
            if root.right: self.printTree(root.right, filter_attr, filter_value)

    def remove(self, title, root=None):
        if self.root is None:
            return None
        
        if root is None:
            self.root = self._remove_node(self.root, title)
        else:
            return self._remove_node(root, title)

    def _remove_node(self, root, title):
        if root is None:
            return root

        # Busca o nó a ser removido
        if title.lower() < root.content.title.lower():
            root.left = self._remove_node(root.left, title)
        elif title.lower() > root.content.title.lower():
            root.right = self._remove_node(root.right, title)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            
            temp = self._min_value_node(root.right)
            root.content = temp.content
            root.right = self._remove_node(root.right, temp.content.title)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# --- MENU INTERATIVO ---
def menu():
    biblioteca = Tree()
    
    # Dados iniciais
    biblioteca.add(Book("O Hobbit", "Tolkien", "Fantasia", 10, 310))
    biblioteca.add(Book("1984", "Orwell", "Distopia", 14, 416))
    biblioteca.add(Book("Clean Code", "Robert Martin", "Técnico", 16, 464))

    while True:
        print("\n" + "="*40)
        print("      SISTEMA DE BIBLIOTECA COMPLETO")
        print("="*40)
        print("1. Cadastrar Livro (Adição)")
        print("2. Listar Acervo (Listagem)")
        print("3. Remover Livro (Remoção)")
        print("4. Buscar por Autor")
        print("5. Buscar por Tipo")
        print("6. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\n--- Cadastro ---")
            t = input("Título: ")
            a = input("Autor: ")
            tp = input("Tipo: ")
            i = input("Idade Recomendada: ")
            p = input("Páginas: ")
            biblioteca.add(Book(t, a, tp, i, p))
            print(f"'{t}' adicionado com sucesso!")

        elif opcao == "2":
            print("\n--- Acervo (Ordem Alfabética) ---")
            if biblioteca.root is None:
                print("A biblioteca está vazia.")
            else:
                biblioteca.printTree()

        elif opcao == "3":
            t = input("\nDigite o TÍTULO exato do livro para remover: ")
            biblioteca.remove(t)
            print(f"Comando de remoção executado para: {t}")

        elif opcao == "4":
            autor = input("\nDigite o nome do autor: ")
            print(f"Resultados para '{autor}':")
            biblioteca.printTree(filter_attr="author", filter_value=autor)

        elif opcao == "5":
            tipo = input("\nDigite o tipo de livro: ")
            print(f"Resultados para '{tipo}':")
            biblioteca.printTree(filter_attr="book_type", filter_value=tipo)

        elif opcao == "6":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
