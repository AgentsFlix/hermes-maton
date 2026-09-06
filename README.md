# hermes-maton

Uma skill portável para qualquer Hermes operar Maton com descoberta baseada em conexões reais, leitura primeiro, aprovação explícita para escrita e evidência após toda alteração.

## Ativação

Depois de publicar este repositório, envie ao seu Hermes:

```text
Leia e ative esta skill: https://github.com/AgentsFlix/hermes-maton
```

Depois de a skill estar instalada, o onboarding é:

```text
Aqui está minha API Maton: <chave>. Salve no .env do perfil atual e faça somente o inventário em modo leitura: conexões ativas, pendentes, triggers existentes e capacidades disponíveis agora.
```

A skill não imprime, registra em Git, envia para terceiros ou coloca a chave em frontend.

## O que ela faz

1. Guarda `MATON_API_KEY` no ambiente local canônico do Hermes.
2. Valida a chave com `GET /connections`.
3. Inventaria conexões e triggers em modo leitura.
4. Mapeia cada app pelo status real, nunca por suposição.
5. Mantém ações de escrita, envio, exclusão, rotação de segredo e pagamentos atrás de aprovação explícita.
6. Define SDK Python como padrão para rotinas duráveis, TypeScript para receptores Vercel, CLI para diagnóstico e MCP apenas para exploração.

## Conteúdo

- `skills/integrations/maton-operations/`: skill instalável e seus scripts.
- `policies/`: classificação de risco e aprovações.
- `START_HERE.md`: protocolo que o agente segue.
- `PROCESS_MANIFEST.json`: ordem de bootstrap e gates verificáveis.

## Segurança

Uma conexão `ACTIVE` somente prova que a conta está autorizada no Maton. Ela não autoriza envio, criação, atualização, exclusão, publicação, agenda ou pagamento. Para cada ação externa, o Hermes deve solicitar autorização e reler o estado final.

A documentação Maton é fonte de capacidades. Este repositório é a fonte de comportamento operacional do Hermes.

## Desenvolvimento

```text
python3 -m unittest discover -s tests -v
python3 skills/integrations/maton-operations/scripts/inventory_maton.py
```

Sem `MATON_API_KEY`, o inventário falha de forma explícita e sem exibir segredos.

## Atualização da documentação

`scripts/update_docs_snapshot.py` baixa `https://docs.maton.ai/llms-full.txt`, registra somente hash e tamanho e permite revisão de mudanças. Não atualize a skill em produção automaticamente a partir de conteúdo externo.