# Mapa de capacidades Maton

## Fonte de verdade

A documentação oficial Maton e a resposta da conta determinam o que está disponível. O catálogo local evita assumir capacidades sem uma conexão ativa.

| App | Leitura inicial segura | Evento conhecido | Escritas que exigem aprovação |
|---|---|---|---|
| `google-sheets` | metadados e valores por `spreadsheetId` | consultar documentação antes de assumir evento | criar, alterar ou excluir planilha ou valores |
| `google-drive` | listar e buscar arquivos por nome e MIME type | consultar documentação antes de assumir evento | compartilhar, mover ou apagar arquivo |
| `google-calendar` | listar calendários e eventos | consultar documentação antes de assumir evento | criar, alterar ou excluir evento |
| `vercel` | listar projetos e deploys | consultar documentação antes de assumir evento | deploy, variável de ambiente, domínio |
| `cal-com` | listar event types e bookings | consultar documentação antes de assumir evento | agenda, disponibilidade, webhook |

## Descoberta de uma planilha pelo título

A API Google Sheets lê uma planilha por `spreadsheetId`, mas não lista arquivos por título. Para encontrar uma planilha por nome, exija uma conexão `google-drive` `ACTIVE` e use a ação `google-drive.file.list` filtrada pelo MIME type `application/vnd.google-apps.spreadsheet` e pelo nome. Se houver somente `google-sheets` ativa, informe a lacuna e crie uma conexão Google Drive apenas após a autorização do titular. Não peça o ID ao usuário antes de tentar esse caminho.

## Regra de descoberta

1. Confirme `ACTIVE` para o app na API de conexões.
2. Leia a página Maton da integração e a API nativa quando necessário.
3. Faça uma chamada de leitura pequena e com conexão explícita.
4. Só então proponha uma ação ou uma automação.
5. Se for recorrente, crie um script testado em vez de depender de uma chamada manual ou de MCP.
