import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def insert_product(products):
    code = input("Digite o código do produto: ")
    name = input("Digite o nome do produto: ").capitalize()
    price = float(input("Digite o preço do produto: "))
    
    product = {"code": code, "name": name, "price": price}
    products.append(product)
    print("Produto inserido com sucesso!")

def delete_product(products):
    code_to_delete = input("Digite o código do produto a ser excluído: ")
    
    for product in products:
        if product["code"] == code_to_delete:
            products.remove(product)
            print("Produto excluído com sucesso!")
            return
    
    print("Produto não encontrado.")

def list_products(products):
    print("\nLista de Produtos:")
    for i, product in enumerate(products, start=1):
        print(f"{i}. Código: {product['code']}, Nome: {product['name']}, Preço: R${product['price']:.2f}")

def consult_price(products):
    code_to_consult = input("Digite o código do produto para consultar o preço: ")
    
    for product in products:
        if product["code"] == code_to_consult:
            print(f"O preço do produto {product['name']} é R${product['price']:.2f}.")
            return
    
    print("Produto não encontrado.")

def main():
    products = []

    while True:
        print("\nMenu:")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("5. Sair")

        choice = input("Escolha a opção (1-5): ")

        if choice == "1":
            insert_product(products)
        elif choice == "2":
            delete_product(products)
        elif choice == "3":
            list_products(products)
        elif choice == "4":
            consult_price(products)
        elif choice == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
