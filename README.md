# TaskFlow

TaskFlow é um gerenciador de tarefas simples e eficiente que utiliza **Python** e **MongoDB** para ajudar na organização e controle de atividades. Ele suporta funcionalidades como adicionar, listar, concluir, remover e exportar tarefas. Além disso, possui integração para exportar dados em formato JSON no diretório `Documentos/tarefas`.

---

## 🛠️ Funcionalidades

1. **Adicionar Tarefa**: Inclua uma tarefa com detalhes opcionais.
2. **Listar Tarefas**: Exiba todas as tarefas com status (pendente ou concluída) e descrição.
3. **Concluir Tarefa**: Marque uma tarefa como concluída.
4. **Remover Tarefa**: Delete uma tarefa por número ou nome.
5. **Exportar para JSON**: Gere um arquivo JSON com todas as tarefas armazenadas.
6. **Importar Tarefas de JSON**: Carregue tarefas a partir de um arquivo JSON externo (próxima funcionalidade!).

---

## 🚀 Tecnologias

- **Python**: Linguagem principal utilizada.
- **MongoDB**: Banco de dados para armazenar tarefas.
- **Pymongo**: Biblioteca Python para integração com MongoDB.
- **JSON**: Formato para exportação de dados.

---

## 📦 Configuração

### Pré-requisitos
1. Instale o Python 3.x.
2. Certifique-se de ter o MongoDB rodando localmente.

### Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/RamosGuilherme2/TaskFlow
   cd TaskFlow

2. Instale as dependencias:
   ```bash
   pip install pymongo


## 📂 Estrutura do Projeto
- TaskFlow.py: Arquivo principal com o código do gerenciador de tarefas.
- Documents/tarefas: Diretório onde os arquivos JSON exportados são salvos automaticamente.

## 🌐 Configuração da Conexão com o MongoDB
O TaskFlow utiliza uma conexão padrão com o MongoDB rodando localmente, com o seguinte URI:
mongodb://localhost:27017/

**Alteração da Conexão**
Caso seja necessário utilizar uma instância diferente (como um banco remoto ou MongoDB Atlas), você pode alterar a conexão diretamente no código, na seguinte linha:
client = MongoClient("mongodb://localhost:27017/")

Substitua o URI pelo endereço do seu banco. Por exemplo:
- Banco remoto:client = MongoClient("mongodb://seu-banco-remoto:27017/")
- MongoDB Atlas:client = MongoClient("mongodb+srv://usuario:senha@cluster.mongodb.net/TaskFlow")

**Requisitos**
Certifique-se de que o banco de dados TaskFlow e a coleção tarefas estão criados na instância especificada ou serão criados automaticamente na primeira execução do programa.



## ⚙️ Uso
Inicie o programa
Execute o arquivo principal:
   **python TaskFlow.py**


Funcionalidades disponíveis
- Escolha uma opção no menu interativo para gerenciar suas tarefas.
- Use a exportação para salvar tarefas localmente em JSON.

## 🛡️ Melhorias Planejadas
- Suporte a categorias e prioridades.
- Sistema de histórico para preservar tarefas concluídas ou removidas.
- Opção para buscar tarefas por nome ou detalhes.
- Relatórios e estatísticas para análise do progresso.
- Exportação e importação de dados em formato CSV.
- Interface gráfica (GUI) com Tkinter ou PyQt.

## 🤝 Contribuição
Contribuições são bem-vindas! Siga os passos abaixo:
- Faça um fork do projeto.
- Crie uma nova branch: git checkout -b minha-melhoria.
- Commit suas mudanças: git commit -m 'Adicionei nova funcionalidade'.
- Envie suas alterações: git push origin minha-melhoria.

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🧑‍💻 Autor
Guilherme
- LinkedIn: [Guilherme Ramos](https://www.linkedin.com/in/guilherme-ramos-90517b235/)
- GitHub: [RamosGuilherme2](https://github.com/RamosGuilherme2)















