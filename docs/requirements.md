# Requisitos do Sistema — TopTech AI

## 1. Visão geral

O TopTech AI é um agente virtual de atendimento ao cliente para uma loja fictícia de eletrônicos.

O objetivo é automatizar parte do atendimento, interpretar solicitações em linguagem natural, consultar informações de pedidos por meio de ferramentas e encaminhar situações que necessitam de intervenção humana.

O projeto utiliza Python, um modelo de linguagem integrado pela API da Groq e banco de dados SQLite para consulta de pedidos.

## 2. Requisitos funcionais

Os requisitos funcionais descrevem as funcionalidades que o sistema deverá oferecer.

| Código | Requisito | Estado |
|---|---|---|
| RF01 | Identificar solicitações dos clientes por palavras-chave. | Implementado parcialmente |
| RF02 | Priorizar solicitações de atendimento humano. | Implementado parcialmente |
| RF03 | Consultar pedidos fictícios pelo número. | Implementado |
| RF04 | Informar o status e as informações disponíveis dos pedidos. | Implementado |
| RF05 | Registrar solicitações de cancelamento após confirmação do cliente. | Planejado |
| RF06 | Registrar histórico persistente de atendimento. | Planejado |
| RF07 | Informar quando um pedido não for encontrado. | Implementado |
| RF08 | Encaminhar solicitações de cancelamento para atendimento humano. | Planejado |
| RF09 | Interpretar mensagens dos clientes utilizando um modelo de linguagem. | Implementado |
| RF10 | Executar ferramentas para consultar informações dos pedidos. | Implementado |
| RF11 | Manter o contexto das conversas durante a sessão de atendimento. | Implementado |

## 3. Requisitos não funcionais

| Código | Requisito |
|---|---|
| RNF01 | O sistema deverá evitar solicitar informações sensíveis desnecessárias. |
| RNF02 | O código deverá ser organizado em funções e módulos reutilizáveis. |
| RNF03 | O sistema não deverá inventar informações sobre pedidos ou reembolsos. |
| RNF04 | O sistema deverá informar claramente quando uma operação não puder ser realizada. |
| RNF05 | As credenciais de acesso às APIs deverão ser armazenadas em variáveis de ambiente, sem exposição no repositório. |
| RNF06 | O sistema deverá utilizar testes automatizados para validar funcionalidades importantes. |

## 4. Regras de negócio

- RN01: solicitações explícitas de atendimento humano deverão receber prioridade.
- RN02: solicitações de reembolso deverão ser encaminhadas para atendimento humano.
- RN03: o sistema não poderá confirmar operações sem confirmação real.
- RN04: consultas de pedidos deverão utilizar apenas dados disponíveis na base fictícia.
- RN05: o agente deverá solicitar confirmação explícita antes de registrar uma solicitação de cancelamento.
- RN06: registrar uma solicitação de cancelamento não significa que o pedido foi efetivamente cancelado.

## 5. Tecnologias

**Atualmente utilizadas:**

- Python 3.12
- SQLite
- SQL
- Groq API
- Modelo de linguagem `openai/gpt-oss-20b`
- Tool Calling (chamadas de ferramentas)
- JSON
- python-dotenv
- unittest
- unittest.mock
- Git e GitHub

**Planejadas:**

- Interface de atendimento.
- Persistência do histórico de conversas.
- Fluxo completo de cancelamento e encaminhamento humano.

## 6. Organização do projeto

O projeto utiliza uma arquitetura modular para separar as responsabilidades:

| Módulo | Responsabilidade |
|---|---|
| `app/main.py` | Ponto de entrada da aplicação e interação com o usuário. |
| `app/llm_client.py` | Integração com a Groq, gerenciamento do histórico e comunicação com o modelo de linguagem. |
| `app/tools.py` | Registro e execução das ferramentas disponíveis para o agente. |
| `app/orders.py` | Consulta e processamento de informações dos pedidos. |
| `app/database.py` | Gerenciamento da conexão com o banco de dados SQLite. |
| `app/tests/test_orders.py` | Testes automatizados das consultas de pedidos. |
| `docs/requirements.md` | Documentação dos requisitos do sistema. |
| `toptech.db` | Banco de dados local com informações fictícias dos pedidos. |

**Observação:** o banco de dados e o arquivo `.env` são mantidos localmente e não devem ser publicados no GitHub.

## 7. Histórico de evolução

| Data | Alteração |
|---|---|
| 06/11/2026 | Conclusão da Fase 1: identificação de solicitações e priorização do atendimento humano. |
| 06/11/2026 | Criação da documentação inicial de requisitos. |
| 06/11/2026 | Inclusão dos requisitos de consulta de pedidos e cancelamentos. |
| 08/11/2026 | Conclusão da Fase 2: implementação da consulta de pedidos em Python, com validação de entradas e tratamento de erros. |
| 08/11/2026 | Organização do código em funções e publicação da implementação no GitHub. |
| 10/11/2026 | Integração com SQLite, criação do módulo `database.py` e centralização da conexão. |
| 11/11/2026 | Conclusão da integração SQLite e modularização da consulta de pedidos. |
| 11/11/2026 | Implementação dos primeiros testes automatizados utilizando `unittest` e `unittest.mock`, com três testes aprovados. |
| 16/11/2026 | Integração com a Groq API utilizando o modelo `openai/gpt-oss-20b`. |
| 16/11/2026 | Implementação de chamadas de ferramentas (Tool Calling) para consulta de pedidos no SQLite. |
| 16/11/2026 | Implementação do histórico de conversas em memória e modularização da aplicação. |
| 16/11/2026 | Validação da integração entre IA, ferramentas e banco de dados, com três testes automatizados aprovados. |

## 8. Próximas evoluções

- Integrar a identificação de solicitações ao fluxo principal do agente.
- Implementar o encaminhamento efetivo para atendimento humano.
- Implementar o fluxo de cancelamento com confirmação do cliente.
- Desenvolver o registro persistente do histórico de atendimento.
- Melhorar o tratamento de erros e validação das chamadas de ferramentas.
- Desenvolver uma interface para demonstração do agente.
- Criar instruções de instalação e inicialização do banco de dados para novos usuários.
- Ampliar os testes automatizados para as ferramentas e integrações com a IA.