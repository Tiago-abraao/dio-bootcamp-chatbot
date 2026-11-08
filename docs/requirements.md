# Requisitos do Sistema — TopTech AI

## 1. Visão geral

O TopTech AI é um projeto de agente virtual de atendimento ao cliente para uma loja fictícia de eletrônicos.

O objetivo é automatizar parte do atendimento, identificar solicitações, consultar informações de pedidos e encaminhar situações que necessitam de intervenção humana.

## 2. Requisitos funcionais

Os requisitos funcionais descrevem as funcionalidades que o sistema deverá oferecer.

| Código | Requisito | Estado |
|---|---|---|
| RF01 | Identificar solicitações dos clientes por palavras-chave. | Implementado |
| RF02 | Priorizar solicitações de atendimento humano. | Implementado |
| RF03 | Consultar pedidos fictícios pelo número. | Planejado |
| RF04 | Informar o status e as informações disponíveis dos pedidos. | Planejado |
| RF05 | Registrar solicitações de cancelamento após confirmação do cliente. | Planejado |
| RF06 | Registrar histórico de atendimento. | Planejado |
| RF07 | Informar quando um pedido não for encontrado. | Planejado |
| RF08 | Encaminhar solicitações de cancelamento para atendimento humano. | Planejado |

## 3. Requisitos não funcionais

| Código | Requisito |
|---|---|
| RNF01 | O sistema deverá evitar solicitar informações sensíveis desnecessárias. |
| RNF02 | O código deverá ser organizado em funções e módulos reutilizáveis. |
| RNF03 | O sistema não deverá inventar informações sobre pedidos ou reembolsos. |
| RNF04 | O sistema deverá informar claramente quando uma operação não puder ser realizada. |

## 4. Regras de negócio

- RN01: solicitações explícitas de atendimento humano terão prioridade.
- RN02: solicitações de reembolso deverão ser encaminhadas para atendimento humano.
- RN03: o sistema não poderá confirmar operações sem confirmação real.
- RN04: consultas de pedidos deverão utilizar apenas dados disponíveis na base fictícia.
- RN05: o agente deverá solicitar confirmação explícita antes de registrar uma solicitação de cancelamento.
- RN06: registrar uma solicitação de cancelamento não significa que o pedido foi efetivamente cancelado.

## 5. Tecnologias

**Atualmente utilizadas:**
- Python 3.12
- Git e GitHub

**Planejadas:**
- SQLite
- Integração com modelo de linguagem
- Interface de atendimento

## 6. Histórico de evolução

| Data | Alteração |
|---|---|
| 06/11/2026 | Conclusão da Fase 1: identificação de solicitações e priorização do atendimento humano. |
| 06/11/2026 | Criação da documentação inicial de requisitos. |
| 06/11/2026 | Inclusão dos requisitos de consulta de pedidos e cancelamentos. |