# Protocolo de ativação Maton

## Entrada reconhecida

O usuário forneceu uma chave Maton e pediu para salvá-la no `.env`.

## Fase 1: armazenamento local

- Localize o arquivo de ambiente do perfil Hermes com `hermes config env-path`.
- Se o comando não existir, peça a localização do ambiente, não invente um caminho.
- Grave somente `MATON_API_KEY` no ambiente local do perfil atual.
- Garanta que o arquivo não seja legível por outros usuários quando o sistema suportar permissões POSIX.
- Nunca exiba a chave, não a coloque em comandos visíveis, logs, relatórios, commits, cards ou frontend.
- A gravação local não prova injeção no runtime hospedado.

**Gate:** existe exatamente uma entrada não vazia de `MATON_API_KEY`, sem expor o valor.

## Fase 2: validação mínima

Execute o inventário de leitura. Ele chama somente `GET /connections` e `GET /triggers`.

**Gate:** a resposta diferencia chave inválida, indisponibilidade de rede e inventário válido.

## Fase 3: mapa de capacidades

Relate somente app, método, status, quantidade de triggers e capacidade potencial ligada à documentação. Não exponha URLs OAuth, metadados de conta, headers ou payloads.

- `ACTIVE`: pode ser avaliada para operações do app.
- `PENDING`: precisa de OAuth concluído pelo titular.
- `FAILED`: precisa de reconexão ou investigação.

**Gate:** o relatório distingue conexão de automação. Uma conexão não significa que há trigger, cron, webhook ou ação em execução.

## Fase 4: execução posterior

- Leitura: pode ser executada quando o pedido for específico.
- Escrita reversível: mostrar operação, alvo e payload resumido, depois pedir aprovação.
- Envio, publicação, criação de agenda, criação de trigger, deploy ou alteração de dados: pedir aprovação explícita e reler o resultado.
- Exclusão, revogação, rotação de segredo ou pagamento: confirmação específica antes da ação.

## Rotas técnicas

- Rotina durável, digest, reconciliação ou cron: SDK Python.
- Endpoint serverless Vercel: SDK TypeScript ou HTTP nativo.
- Diagnóstico do operador: CLI Maton.
- Descoberta de ações desconhecidas: MCP em modo exploratório, antes de virar rotina.

## Atualização

Use as referências deste repositório e a documentação oficial Maton. Alterações de documentação devem gerar revisão versionada, não mudar comportamento de produção automaticamente.