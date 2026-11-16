# 🤖 TopTech AI — Agente Inteligente de Atendimento

Agente virtual de atendimento ao cliente desenvolvido com Python e Inteligência Artificial, utilizando um modelo de linguagem integrado à API da Groq e ferramentas capazes de consultar informações reais em um banco de dados SQLite.

O projeto simula o atendimento de uma loja fictícia de eletrônicos, permitindo que clientes consultem informações sobre seus pedidos por meio de conversas em linguagem natural.

## 🎯 Sobre o projeto

O TopTech AI nasceu como um projeto de estudos em engenharia de prompts e evoluiu para uma aplicação com integração de LLM, execução de ferramentas e persistência de dados.

O objetivo é desenvolver um agente capaz de interpretar solicitações, consultar informações disponíveis e fornecer respostas contextualizadas, respeitando regras de negócio e critérios de segurança.

O desenvolvimento faz parte da minha jornada de aprendizado em Python, Inteligência Artificial e construção de agentes inteligentes.

## ✨ Funcionalidades implementadas

- **Atendimento conversacional:** interpretação de mensagens em linguagem natural utilizando modelo de linguagem.
- **Consulta de pedidos:** busca de pedidos fictícios pelo número informado pelo cliente.
- **Tool Calling:** o modelo identifica quando precisa utilizar uma ferramenta e solicita sua execução.
- **Integração com SQLite:** consulta de informações persistidas em banco de dados.
- **Histórico de conversa:** manutenção do contexto durante a sessão de atendimento.
- **Tratamento de pedidos inexistentes:** identificação de pedidos que não estão cadastrados.
- **Testes automatizados:** validação da lógica de consulta de pedidos com `unittest` e `unittest.mock`.

## 🧠 Inteligência Artificial

O agente utiliza a API da Groq integrada ao modelo:

`openai/gpt-oss-20b`

A integração permite que o modelo interprete solicitações e solicite a execução de ferramentas Python quando necessário.

### Como funciona o Tool Calling?

1. O cliente envia uma mensagem.
2. O modelo de linguagem interpreta a solicitação.
3. Quando necessário, o modelo solicita uma ferramenta.
4. A aplicação Python executa a função correspondente.
5. A ferramenta consulta o banco SQLite.
6. O resultado retorna ao modelo de linguagem.
7. O agente apresenta uma resposta ao cliente.

## 🏗️ Arquitetura do projeto

O projeto utiliza uma estrutura modular para separar responsabilidades.

```text
dio-bootcamp-chatbot/
│
├── app/
│   ├── main.py
│   ├── llm_client.py
│   ├── tools.py
│   ├── orders.py
│   ├── database.py
│   │
│   └── tests/
│       └── test_orders.py
│
├── docs/
│   └── requirements.md
│
├── .env
├── .gitignore
├── README.md
└── toptech.db
```

### Responsabilidades dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Inicialização e interação com o usuário. |
| `llm_client.py` | Comunicação com a Groq, histórico e processamento das respostas. |
| `tools.py` | Registro e execução das ferramentas disponíveis para o agente. |
| `orders.py` | Consulta e processamento de informações dos pedidos. |
| `database.py` | Gerenciamento da conexão com SQLite. |
| `test_orders.py` | Testes automatizados das consultas de pedidos. |

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python 3.12 | Linguagem principal |
| Groq API | Integração com modelo de linguagem |
| GPT-OSS 20B | Modelo utilizado pelo agente |
| SQLite | Banco de dados |
| SQL | Consultas ao banco de dados |
| JSON | Comunicação entre ferramentas e modelo |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| unittest | Testes automatizados |
| unittest.mock | Simulação de dependências |
| Git e GitHub | Versionamento e documentação |

## 🧪 Testes automatizados

O projeto utiliza `unittest` para validar a consulta de pedidos.

Atualmente, existem três testes implementados:

- Consulta de pedido existente.
- Consulta de pedido inexistente.
- Consulta utilizando mock para simular o retorno da função de busca.

Para executar os testes:

```bash
PYTHONPATH=app python3 -m unittest discover -s app/tests -p "test_*.py" -v
```

**Resultado da última validação:** 3 testes aprovados.

## ⚙️ Configuração do ambiente

### Pré-requisitos

- Python 3.12 ou superior.
- pip.
- Uma chave de API da Groq.

### 1. Clone o repositório

```bash
git clone https://github.com/Tiago-abraao/dio-bootcamp-chatbot.git
```

### 2. Acesse o projeto

```bash
cd dio-bootcamp-chatbot
```

### 3. Crie um ambiente virtual

```bash
python3 -m venv .venv
```

Ative o ambiente:

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install groq python-dotenv
```

### 5. Configure a variável de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_api
```

Não compartilhe sua chave de API nem publique o arquivo `.env`.

### 6. Execute a aplicação

Após configurar o banco de dados SQLite conforme a estrutura utilizada pelo projeto:

```bash
python3 app/main.py
```

**Observação:** o banco `toptech.db` é local e não está versionado no GitHub. A preparação automática do banco para novas instalações está prevista como melhoria futura.

## 📌 Próximas evoluções

- Integrar a identificação de solicitações ao fluxo principal do agente.
- Implementar o fluxo de cancelamento com confirmação do cliente.
- Desenvolver o encaminhamento efetivo para atendimento humano.
- Implementar o armazenamento persistente do histórico de atendimento.
- Ampliar os testes automatizados para ferramentas e integração com IA.
- Melhorar o tratamento de erros e validação das chamadas de ferramentas.
- Desenvolver uma interface para demonstração do agente.
- Automatizar a inicialização e preparação do banco de dados.

## 👨‍💻 Autor

**Tiago Abraão**

Estudante de Análise e Desenvolvimento de Sistemas, interessado em desenvolvimento de software, Inteligência Artificial e construção de agentes inteligentes.

- GitHub: [Tiago-abraao](https://github.com/Tiago-abraao)
- LinkedIn: [Perfil profissional](https://www.linkedin.com/in/tiago-abraao-94a07025b/)

---

Projeto desenvolvido para fins educacionais e de portfólio, com foco em aprendizado prático de Python, integração com modelos de linguagem e desenvolvimento de agentes de IA.