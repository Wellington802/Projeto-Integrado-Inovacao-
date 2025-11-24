pacientes = []

def cadastrar_paciente():
    print("\n--- Cadastrar Paciente ---")
    nome = input("Nome completo: ").strip()
    while not nome.replace(" ", "").isalpha():
        print("Nome inválido. Digite apenas letras e espaços.")
        nome = input("Nome completo: ").strip()

    telefone = input("Telefone (apenas números): ").strip()
    while not telefone.isdigit():
        print("Telefone inválido. Digite apenas números.")
        telefone = input("Telefone (apenas números): ").strip()

    idade = input("Idade (apenas números): ").strip()
    while not idade.isdigit():
        print("Idade inválida. Digite apenas números.")
        idade = input("Idade (apenas números): ").strip()

    paciente = {
        "nome": nome,
        "telefone": telefone,
        "idade": int(idade)
    }
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def ver_estatisticas():
    print("\n--- Estatísticas ---")
    total = len(pacientes)
    print(f"Total de pacientes cadastrados: {total}")
    if total > 0:
        media = sum(p["idade"] for p in pacientes) / total
        print(f"Idade média: {media:.1f}")

def buscar_por_nome():
    print("\n--- Buscar paciente pelo nome ---")
    termo = input("Digite o nome ou parte do nome: ").strip().lower()
    resultados = [p for p in pacientes if termo in p["nome"].lower()]
    if resultados:
        print(f"Encontrados {len(resultados)} paciente(s):")
        for p in resultados:
            print(f"- {p['nome']} | Tel: {p['telefone']} | Idade: {p['idade']}")
    else:
        print("Nenhum paciente encontrado.")

def listar_todos():
    print("\n--- Lista de todos os pacientes ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p['nome']} | Tel: {p['telefone']} | Idade: {p['idade']}")

def menu():
    while True:
        print("\n==== Clínica Vida+ ====")
        print("1. Cadastrar Paciente")
        print("2. Ver Estatísticas")
        print("3. Buscar paciente pelo nome")
        print("4. Listar todos os pacientes")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            ver_estatisticas()
        elif opcao == "3":
            buscar_por_nome()
        elif opcao == "4":
            listar_todos()
        elif opcao == "5":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
