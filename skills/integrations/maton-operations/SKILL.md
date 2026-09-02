---
name: maton-operations
description: Opera Maton com inventário seguro e aprovação explícita.
version: 0.1.0
author: José Carlos Amorim, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Maton, integrations, OAuth, triggers, security]
    related_skills: []
---

# Operações Maton

Use Maton como camada de conexões, gateway e eventos. Esta skill descobre capacidades pela conta conectada, mantém leitura como padrão e transforma automações recorrentes em scripts verificáveis, não em inferências livres.

## Quando usar

- O usuário fornece uma API key Maton e pede armazenamento no ambiente do Hermes.
- O usuário quer listar conexões, triggers ou capacidades Maton.
- Uma rotina precisa acessar Gmail, Calendar, Vercel ou outro app já conectado no Maton.
- Uma nova automação Maton precisa de cron, eventos ou webhook.

Não use para enviar, publicar, apagar, pagar, criar agendas ou criar triggers sem pedido específico e aprovação explícita.

## Pré-requisitos

- `MATON_API_KEY` existe somente no ambiente secreto do perfil atual.
- Use `hermes config env-path` para descobrir o arquivo de ambiente. Não assuma caminhos.
- O endpoint base é `https://api.maton.ai`.
- Use a conexão explícita quando existir mais de uma conta para o mesmo app.

## Procedimento

1. **Guardar a chave quando o titular pedir.** Escreva `MATON_API_KEY` no env canônico, com modo restrito quando aplicável. Não mostre seu valor. Critério: uma entrada não vazia, sem vazamento em output.
2. **Validar sem efeitos externos.** Execute `terminal(command="python3 skills/integrations/maton-operations/scripts/inventory_maton.py")`. Critério: o resultado identifica chave inválida, erro de rede ou inventário válido.
3. **Inventariar antes de propor automação.** Relate conexões por app, método e estado, depois triggers por fonte e estado. Critério: conexão e automação aparecem como conceitos separados.
4. **Descobrir capacidade sob demanda.** Leia `references/capability-map.md`, confirme a documentação oficial da integração e faça a menor chamada de leitura possível. Critério: a capacidade tem app, conexão e endpoint ou ação identificados.
5. **Escolher a rota.** SDK Python para cron, digest e reconciliação. TypeScript para função Vercel. CLI para diagnóstico. MCP só para explorar ações desconhecidas antes de padronizar uma rotina. Critério: a escolha reduz dependências e permite evidência.
6. **Classificar risco antes de escrever.** Leia `../../../policies/action-classification.yaml`. Leitura pode seguir o pedido específico. Escrita exige aprovação explícita. Envio, publicação, agenda, trigger e deploy exigem aprovação e releitura. Exclusão, revogação, rotação ou pagamento exigem confirmação específica. Critério: a autorização corresponde exatamente à operação.
7. **Verificar toda alteração.** Depois de escrita externa, leia o alvo final e informe ID, URL ou campo verificável. Critério: não declarar resultado com base apenas na resposta inicial.

## Gmail em lote

Para digests em horário fixo, crie somente após aprovação um trigger `google-mail` `email.received`, inicialmente sem destino. O cron Hermes consulta os eventos posteriores ao cursor, organiza o digest e grava o novo cursor somente após entrega confirmada. Não marque mensagens como lidas, não responda e não crie compromissos por padrão.

## Armadilhas

- `ACTIVE` significa conexão autorizada, não permissão para agir sem pedido.
- Uma chave salva localmente não prova que foi injetada no runtime hospedado.
- Não exponha a API key no frontend, em URL, em Git ou em logs.
- Não use webhook sem receptor HTTPS que valide assinatura e deduplique `event_id`.
- Não transforme descoberta MCP em automação permanente sem script, testes e política de aprovação.

## Verificação

- `PROCESS_MANIFEST.json` é válido.
- `inventory_maton.py` só usa GET para `/connections` e `/triggers`.
- O relatório não contém chave, OAuth URL, metadata de conta ou payload de terceiros.
- Para alterações externas, há leitura final com identificador verificável.
