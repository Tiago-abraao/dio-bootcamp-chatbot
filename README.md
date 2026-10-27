# 🤖 Agente de Atendimento ao Cliente — TopTech

Agente virtual de atendimento ao cliente desenvolvido com foco em engenharia de prompts e inteligência artificial. O projeto simula o atendimento de uma loja de eletrônicos, auxiliando clientes com dúvidas sobre pedidos, entregas, trocas e reembolsos.

## 📌 Sobre o projeto

O objetivo deste projeto é criar um agente de IA capaz de conduzir conversas de atendimento de forma clara, cordial, profissional e segura.

O agente segue instruções específicas para identificar o problema do cliente, fornecer orientações adequadas e encaminhar solicitações para atendimento humano quando necessário.

## 🎯 Objetivos

- Praticar engenharia de prompts.
- Desenvolver instruções para agentes conversacionais.
- Simular situações reais de atendimento ao cliente.
- Aplicar regras de negócio e critérios de decisão.
- Priorizar a segurança dos dados e a precisão das informações.

## ⚙️ Funcionalidades

### 📦 Pedidos atrasados
- Orienta o cliente a consultar o status da entrega.
- Indica a área "Meus pedidos" do site, quando disponível.
- Evita inventar prazos ou informações de rastreamento.

### 💰 Reembolsos
- Encaminha obrigatoriamente solicitações de estorno para atendimento humano.
- Explica a necessidade do encaminhamento.
- Não promete prazos nem afirma que o reembolso foi realizado sem confirmação.

### 🔄 Produtos incorretos ou com defeito
- Identifica o problema relatado pelo cliente.
- Orienta sobre os procedimentos disponíveis para troca ou correção.
- Não promete um novo envio sem confirmação.

### 🔐 Segurança e precisão
- Não solicita senhas, códigos SMS, CPF ou número completo do cartão.
- Solicita somente informações necessárias para entender o problema.
- Não inventa protocolos, valores, prazos ou políticas comerciais.
- Informa suas limitações quando não possui acesso aos sistemas da loja.

## 🧠 Regras de comportamento

O agente segue esta ordem de prioridade:

1. Segurança e proteção dos dados do cliente.
2. Encaminhamento obrigatório para atendimento humano.
3. Resolução correta, sem inventar informações ou ações.
4. Rapidez, clareza e satisfação do cliente.

### Estilo de comunicação

- Linguagem simples, cordial e profissional.
- Respostas diretas, adequadas para dispositivos móveis.
- No máximo cinco linhas por resposta.
- Listas numeradas quando houver várias etapas.
- Uma pergunta objetiva ao final de cada resposta, quando aplicável.

## 🔄 Fluxo de atendimento

1. Identificar o problema principal.
2. Consultar informações disponíveis, quando houver ferramentas autorizadas.
3. Apresentar orientações ou solicitar um esclarecimento necessário.
4. Encaminhar para atendimento humano nos casos obrigatórios.
5. Confirmar se a dúvida foi resolvida.

## 💬 Exemplos de cenários testados

| Cenário | Comportamento esperado |
|---|---|
| Pedido atrasado | Orientar a consulta do rastreamento |
| Cliente encontrou o pedido | Confirmar se precisa de mais ajuda |
| Produto recebido incorretamente | Orientar sobre as opções de troca |
| Cliente deseja receber outro produto imediatamente | Não prometer envio sem confirmação |
| Pedido cancelado com solicitação de estorno | Encaminhar para atendimento humano |
| Cliente solicita atendente | Orientar o acesso ao canal humano |
| Cliente confirma que resolveu o problema | Encerrar cordialmente o atendimento |

## 🛠️ Tecnologias e conceitos

- Inteligência Artificial (IA)
- Engenharia de prompts
- Agentes conversacionais
- Regras de negócio
- Segurança da informação
- Simulação e avaliação de conversas

