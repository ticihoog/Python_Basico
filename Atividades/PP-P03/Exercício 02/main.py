import json

def load_employees(filename="employees.json"):
    try:
        with open(filename, "r") as file:
            employees = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        employees = []

    return employees

def save_employees(employees, filename="employees.json"):
    with open(filename, "w") as file:
        json.dump(employees, file, indent=2)

def reajusta_dez_porcento(employees):
    for employee in employees:
        employee["salary"] *= 1.10  

def add_employee(employees):
    name = input("Digite o nome do empregado: ").capitalize()
    salary = float(input("Digite o salário do empregado: "))

    new_employee = {"name": name, "salary": salary}
    employees.append(new_employee)
    print("Empregado adicionado com sucesso!")

def delete_employee(employees):
    name_to_delete = input("Digite o nome do empregado a ser excluído: ")

    for employee in employees:
        if employee["name"] == name_to_delete:
            employees.remove(employee)
            print("Empregado excluído com sucesso!")
            return
    
    print("Empregado não encontrado.")

def consult_employee(employees):
    name_to_consult = input("Digite o nome do empregado para consultar informações: ")

    for employee in employees:
        if employee["name"] == name_to_consult:
            print(f"Informações sobre o empregado {employee['name']} - Salário: R${employee['salary']:.2f}")
            return
    
    print("Empregado não encontrado.")

def main():
    employees = load_employees()

    while True:
        print("\nMenu:")
        print("1. Adicionar empregado")
        print("2. Excluir empregado")
        print("3. Consultar informações de um empregado")
        print("4. Reajustar salários em 10%")
        print("5. Listar empregados")
        print("6. Sair")

        choice = input("Escolha a opção (1-6): ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            delete_employee(employees)
        elif choice == "3":
            consult_employee(employees)
        elif choice == "4":
            reajusta_dez_porcento(employees)
            print("\nReajuste de salários aplicado.")
        elif choice == "5":
            print("\nLista de Empregados:")
            for employee in employees:
                print(f"Nome: {employee['name']}, Salário: R${employee['salary']:.2f}")
        elif choice == "6":
            print("\nSaindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

    save_employees(employees)
    print("\nInformações salvas no arquivo.")

if __name__ == "__main__":
    main()
