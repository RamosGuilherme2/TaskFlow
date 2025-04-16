from pymongo import MongoClient
from bson import ObjectId
import json
import os


# Conexão com MongoDB (local)

client = MongoClient("mongodb://localhost:27017/")
db = client["TaskFlow"]

colecao_tarefas = db["tarefas"]

def import_tasks_from_json(file_name):
    try:
        # Abrir e carregar os dados do arquivo JSON
        with open(file_name, "r", encoding="utf-8") as file:
            tarefas = json.load(file)
        
        # Verificação de estrutura
        for tarefa in tarefas:
            if "descricao" in tarefa and "concluida" in tarefa:
                # Evitar duplicatas com base na descrição
                if not colecao_tarefas.find_one({"descricao": tarefa["descricao"]}):
                    colecao_tarefas.insert_one({
                        "descricao": tarefa["descricao"],
                        "detalhes": tarefa.get("detalhes", ""),
                        "concluida": tarefa["concluida"]
                    })
                    print(f"Tarefa '{tarefa['descricao']}' importada com sucesso!")
                else:
                    print(f"Tarefa '{tarefa['descricao']}' já existe e não foi importada.")
            else:
                print("Erro: Uma das tarefas no arquivo JSON está em um formato inválido.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{file_name}' não está em um formato JSON válido.")

def export_tasks_to_json(file_name):
    if not file_name.endswith(".json"):
        file_name += ".json"

    home_dir = os.path.expanduser("~")  # Diretório do usuário
    target_dir = os.path.join(home_dir, "Documents", "tarefas")
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Diretório criado: {target_dir}")
    
    file_path = os.path.join(target_dir, file_name)
    tarefas = list(colecao_tarefas.find())
    for tarefa in tarefas:
        tarefa["_id"] = str(tarefa["_id"]) 

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(tarefas, file, ensure_ascii=False, indent=4)
    
    print(f"Tarefas exportadas para o arquivo '{file_path}' com sucesso!")

def add_task(description, details=""):
    if colecao_tarefas.find_one({"descricao": description}):
        print("Erro: Já existe uma tarefa com esse nome!")
        return

    tarefa = {"descricao": description, "detalhes": details, "concluida": False}
    colecao_tarefas.insert_one(tarefa)
    print("Tarefa adicionada!")

def list_tasks():
        tarefas = list(colecao_tarefas.find())

        for i, tarefa in enumerate(tarefas):
            status = "✔" if tarefa["concluida"] else "✘"
            print(f"{i + 1}. {tarefa['descricao']} [{status}]")
            if "detalhes" in tarefa and tarefa["detalhes"]:
                print(f"   Descrição: {tarefa['detalhes']}")
                
def complete_task(index):
    tarefas = list(colecao_tarefas.find())
    if 0 <= index < len(tarefas):
        task_id = tarefas[index]["_id"]
        colecao_tarefas.update_one({"_id": task_id}, {"$set": {"concluida": True}})
        print("Tarefa marcada como concluída!")
    else:
        print("Erro: Número inválido!")

def remove_task(input_value):
    tarefas = list(colecao_tarefas.find())
    # Remover por Número
    if input_value.isdigit():
        index = int(input_value) - 1
        if 0 <= index < len(tarefas):
            task_id = tarefas[index]["_id"]
            colecao_tarefas.delete_one({"_id": task_id})
            print("Tarefa removida!")
        else:
            print("Erro: Número inválido!")
    else:
        # Remover por Nome
        result = colecao_tarefas.delete_one({"descricao": input_value})
        if result.deleted_count > 0:
            print("Tarefa removida!")
        else:
            print("Erro: Tarefa não encontrada!")


# Menu principal e guia de comandos
while True:
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar como concluída")
    print("4. Remover tarefa")
    print("5. Exportar tarefas para JSON")
    print("6. Importar tarefas de JSON")
    print("7. Sair")


    choice = input("Escolha uma opção: ")
    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            description = input("Digite o nome da tarefa: ")
            details = input("Digite uma descrição para a tarefa (opcional): ")
            add_task(description, details)

        elif choice == 2:
            list_tasks()

        elif choice == 3:
            index = input("Digite o número da tarefa para marcar como concluída: ")
            if index.isdigit():
                complete_task(int(index) - 1)
            else:
                print("Entrada inválida! Certifique-se de digitar um número.")

        elif choice == 4:
            input_value = input("Digite o número ou nome da tarefa para remover: ")
            remove_task(input_value)

        elif choice == 5:
            file_name = input("digite o nome do arquivo para exportar (ex: 'tarefas'): ")
            export_tasks_to_json(file_name)

        elif choice == 6:
            file_name = input("digite o caminho do arquivo JSON para importar: ")
            import_tasks_from_json(file_name)

        elif choice == 7:
            print("Saindo...")
            break

        else:
            print("Opção inválida! Escolha entre 1 e 7.")
    else:
        print("Entrada inválida! Certifique-se de digitar um número.")

