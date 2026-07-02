---
title: "Preços por uso da X API e créditos"
source: https://docs.x.com/pt/x-api/getting-started/pricing
path: pt/x-api/getting-started/pricing
---

A X API utiliza um modelo de preços por uso, sem assinaturas. Pague apenas pelo que usar e ganhe até 20% de volta em créditos gratuitos da xAI API.

A X API utiliza preços **por uso**. Sem assinaturas—pague apenas pelo que usar.

<Button href="https://developer.x.com/#pricing">Ver preços e comprar créditos</Button>

***

## Como funciona

<CardGroup>
  <Card title="Baseado em créditos" icon="coins">
    Compre créditos antecipadamente no Developer Console. Os créditos são deduzidos conforme você faz requisições à API.
  </Card>

  <Card title="Preços por endpoint" icon="code">
    Endpoints diferentes têm custos diferentes. Veja as tarifas atuais no Developer Console.
  </Card>

  <Card title="Sem compromissos" icon="unlock">
    Sem contratos, assinaturas ou gasto mínimo. Comece e pare quando quiser.
  </Card>

  <Card title="Monitoramento em tempo real" icon="gauge-high">
    Acompanhe o uso e os custos ao vivo no Developer Console.
  </Card>
</CardGroup>

<Tip>
  Ganhe créditos gratuitos da [xAI API](https://docs.x.ai) ao comprar créditos da X API—até 20% de volta com base no seu gasto. [Saiba mais](#free-xai-api-credits)
</Tip>

***

## Detalhes do consumo de créditos

Todos os preços são por recurso obtido (leituras) ou por requisição (escritas/ações). [Compre créditos](https://console.x.com) no Developer Console.

### Operações de leitura

Cobradas por recurso retornado na resposta.

| Recurso                       | Custo Unitário      |
| :---------------------------- | :------------------ |
| **Posts: Read**               | \$0.005 por recurso |
| **User: Read**                | \$0.010 por recurso |
| **DM Event: Read**            | \$0.010 por recurso |
| **Following/Followers: Read** | \$0.010 por recurso |
| **List: Read**                | \$0.005 por recurso |
| **Space: Read**               | \$0.005 por recurso |
| **Community: Read**           | \$0.005 por recurso |
| **Note: Read**                | \$0.005 por recurso |
| **Like: Read**                | \$0.001 por recurso |
| **Mute: Read**                | \$0.001 por recurso |
| **Block: Read**               | \$0.001 por recurso |
| **Profile Update: Read**      | \$0.005 por recurso |

### Operações de escrita

Cobradas por requisição.

| Ação                         | Custo Unitário         |
| :--------------------------- | :--------------------- |
| **Post: Create**             | \$0.015 por requisição |
| **Post: Create (with URL)**  | \$0.200 por requisição |
| **Post: Create (summoned)**  | \$0.010 por requisição |
| **DM Interaction: Create**   | \$0.015 por requisição |
| **User Interaction: Create** | \$0.015 por requisição |
| **Interaction: Delete**      | \$0.010 por requisição |
| **Content: Manage**          | \$0.005 por requisição |
| **List: Create**             | \$0.010 por requisição |
| **List: Manage**             | \$0.005 por requisição |
| **Bookmark**                 | \$0.005 por requisição |
| **Media Metadata**           | \$0.005 por requisição |
| **Privacy: Update**          | \$0.010 por requisição |
| **Mute: Delete**             | \$0.005 por requisição |
| **Counts: Recent**           | \$0.005 por requisição |
| **Counts: All**              | \$0.010 por requisição |
| **Trends**                   | \$0.010 por requisição |

<Note>
  Os preços estão sujeitos a alterações. As tarifas atuais estão sempre disponíveis no [Developer Console](https://console.x.com) e na [página de preços do developer.x.com](https://developer.x.com/#pricing).
</Note>

### Eventos de webhook

Os eventos de webhook entregues através da [X Activity API](/x-api/activity/introduction) são cobrados por evento entregue, usando os mesmos nomes de evento mostrados na documentação da Activity API. Você é cobrado uma vez por cada evento faturável, desduplicado dentro da mesma janela de 24 horas UTC que os demais recursos.

| Evento                   | Custo por evento |
| :----------------------- | :--------------- |
| `post.create`            | \$0.005          |
| `post.delete`            | Não cobrado      |
| `follow.follow`          | \$0.010          |
| `follow.unfollow`        | \$0.010          |
| `profile.update.*`       | \$0.005          |
| `chat.received`          | \$0.010          |
| `chat.sent`              | Não cobrado      |
| `chat.conversation_join` | Não cobrado      |
| `dm.received`            | \$0.010          |
| `dm.sent`                | Não cobrado      |
| `dm.read`                | Não cobrado      |
| `dm.indicate_typing`     | Não cobrado      |
| `news.new`               | \$0.005          |
| `spaces.start`           | \$0.005          |
| `spaces.end`             | \$0.005          |

***

## Owned Reads

Owned Reads são requisições feitas pelo seu próprio aplicativo de desenvolvedor para os seus próprios dados (posts, bookmarks, seguidores, curtidas, listas e mais). Esses endpoints custam **\$0.001 por recurso** (1.000 recursos por \$1).

Os seguintes endpoints se qualificam para o preço de Owned Read quando `{id}` corresponde ao usuário autenticado e esse usuário é o proprietário do aplicativo de desenvolvedor:

| Endpoint                             | Descrição                       |
| :----------------------------------- | :------------------------------ |
| `GET /2/users/{id}/tweets`           | Seus próprios posts             |
| `GET /2/users/{id}/mentions`         | Suas menções                    |
| `GET /2/users/{id}/liked_tweets`     | Posts que você curtiu           |
| `GET /2/users/{id}/bookmarks`        | Seus bookmarks                  |
| `GET /2/users/{id}/followers`        | Seus seguidores                 |
| `GET /2/users/{id}/following`        | Contas que você segue           |
| `GET /2/users/{id}/blocking`         | Contas que você bloqueou        |
| `GET /2/users/{id}/muting`           | Contas que você silenciou       |
| `GET /2/users/{id}/owned_lists`      | Listas que você possui          |
| `GET /2/users/{id}/followed_lists`   | Listas que você segue           |
| `GET /2/users/{id}/list_memberships` | Listas das quais você participa |
| `GET /2/users/{id}/pinned_lists`     | Suas listas fixadas             |

<Tip>
  Os Owned Reads tornam significativamente mais barato construir aplicativos que trabalham com os dados do próprio usuário, como aplicativos de dashboard, análises pessoais ou ferramentas de gerenciamento de conta.
</Tip>

***

## Deduplicação

Todos os recursos são deduplicados dentro de uma janela de **dia de 24 horas em UTC**. Se você solicitar e for cobrado por um recurso (como um Post), solicitar o mesmo recurso novamente dentro dessa janela não gerará uma cobrança adicional.

Isso significa que:

* Solicitar o mesmo Post várias vezes em um dia conta como uma única cobrança
* A janela de deduplicação é reiniciada à meia-noite UTC
* Isso se aplica a todos os recursos faturáveis (Posts, usuários, etc.)

<Note>
  A deduplicação é uma **garantia flexível**. Embora ocorra na grande maioria dos casos, podem existir casos específicos, como interrupções de serviço, em que os recursos não sejam deduplicados.
</Note>

***

## Saldo de créditos

O seu saldo de créditos é exibido no Developer Console. Os créditos são deduzidos em tempo real conforme você faz requisições à API.

<Warning>
  Monitore seu saldo de créditos regularmente para evitar interrupções no serviço. Adicione créditos antes que seu saldo chegue a zero para garantir acesso ininterrupto à API.

  ***Observação:** É possível que o saldo de créditos de uma conta fique ligeiramente negativo. Nesse caso, as requisições à API serão bloqueadas até que você adicione créditos para cobrir o saldo negativo.*
</Warning>

### Recarga automática

Ative a recarga automática para reabastecer seu saldo de créditos automaticamente e evitar interrupções no serviço. Configure isso no Developer Console:

| Configuração              | Descrição                                                                         |
| :------------------------ | :-------------------------------------------------------------------------------- |
| **Valor da recarga**      | O valor a ser adicionado quando a recarga automática for acionada (ex.: \$25)     |
| **Limite de acionamento** | A recarga automática é ativada quando seu saldo cai abaixo deste valor (ex.: \$5) |

<Note>
  A recarga automática exige um método de pagamento salvo definido como padrão. Você pode cancelar a qualquer momento no Developer Console ou entrando em contato com o suporte.
</Note>

#### Salvaguardas da recarga automática

Para proteger você contra cobranças descontroladas ou inesperadamente altas, a recarga automática conta com dois limites integrados:

* **Uma recarga por janela de 5 minutos.** As cobranças automáticas podem ser acionadas no máximo uma vez a cada 5 minutos, de modo que um pico repentino de uso não consegue acumular várias recargas em sequência.
* **Pausada com saldo zero ou negativo.** A recarga automática não é executada enquanto o saldo da sua conta estiver em zero ou negativo. Adicione créditos manualmente para retomar as recargas automáticas.

<Warning>
  Se seu uso for intermitente o suficiente para esgotar uma recarga completa em menos de 5 minutos, você ainda poderá ver erros de "sem créditos" mesmo com a recarga automática ativada. Aumente o seu **Valor da recarga** para que uma única recarga supere com folga uma janela de 5 minutos do seu consumo de pico.
</Warning>

***

### Limites de gastos

Defina um valor máximo que você pode gastar por ciclo de cobrança para controlar os custos. Quando o limite for atingido, as requisições à API serão bloqueadas até o próximo ciclo de cobrança.

| Opção                | Descrição                                                                         |
| :------------------- | :-------------------------------------------------------------------------------- |
| **Limite de gastos** | Defina um valor específico em dólares como seu gasto máximo por ciclo de cobrança |

<Tip>
  Use limites de gastos para evitar cobranças inesperadas, especialmente durante o desenvolvimento e os testes.
</Tip>

***

## Créditos gratuitos da xAI API

Ao comprar créditos da X API, você pode ganhar créditos gratuitos da [xAI API](https://docs.x.ai) com base no seu gasto acumulado durante um ciclo de cobrança.

<Note>
  Para receber créditos gratuitos da xAI, você deve vincular sua equipe da xAI à sua conta de desenvolvedor da X. Você pode fazer isso visitando as configurações da sua conta no [developer console](https://console.x.com).
</Note>

### Como funciona

Seu gasto acumulado é monitorado ao longo de cada ciclo de cobrança. À medida que você ultrapassa os limiares de gastos, desbloqueia taxas de recompensa mais altas. Quando um novo ciclo de cobrança começa, seu gasto acumulado é redefinido para \$0.

| Gasto acumulado | Taxa |
| :-------------- | :--- |
| \$0 – \$199     | 0%   |
| \$200 – \$499   | 10%  |
| \$500 – \$999   | 15%  |
| \$1,000+        | 20%  |

<Note>
  A taxa se aplica ao seu **saldo acumulado total**, mas você recebe apenas a diferença—o que é recém-devido menos o que já foi creditado.
</Note>

### Exemplo

Suponha que você faça várias compras ao longo de um ciclo de cobrança:

| Compra      | Taxa | Total devido | Já creditado | Você recebe |
| :---------- | :--- | :----------- | :----------- | :---------- |
| \$100       | 0%   | \$0          | \$0          | **\$0**     |
| \$100       | 10%  | \$20         | \$0          | **\$20**    |
| \$150       | 10%  | \$35         | \$20         | **\$15**    |
| \$150       | 15%  | \$75         | \$35         | **\$40**    |
| \$250       | 15%  | \$112.50     | \$75         | **\$37.50** |
| \$250       | 20%  | \$200        | \$112.50     | **\$87.50** |
|             |      |              |              |             |
| **\$1,000** |      |              |              | **\$200**   |

Este é o mesmo valor que você receberia de uma única compra de \$1,000—a ordem e o tamanho das compras não afetam o total das suas recompensas.

<Tip>
  Veja seu saldo de créditos da xAI e gerencie sua conta em [console.x.ai](https://console.x.ai). Para mais detalhes sobre a cobrança da xAI API, consulte a [documentação de cobrança da xAI](https://docs.x.ai/docs/key-information/billing).
</Tip>

***

## Monitorando o uso

Acompanhe o uso da sua API de forma programática com o [endpoint de Usage](/x-api/usage/introduction):

```bash theme={null}
curl "https://api.x.com/2/usage/tweets" \
  -H "Authorization: Bearer $BEARER_TOKEN"
```

Isso retorna a contagem diária de consumo de Posts, ajudando você a:

* Acompanhar o consumo em relação ao seu orçamento
* Configurar alertas ao se aproximar dos limites
* Identificar endpoints de alto consumo
* Gerar relatórios de uso

***

## Próximos passos

<CardGroup>
  <Card title="Developer Console" icon="grid-2" href="https://console.x.com">
    Compre créditos e veja os preços atuais.
  </Card>

  <Card title="Usage API" icon="chart-line" href="/x-api/usage/introduction">
    Monitore o uso de forma programática.
  </Card>
</CardGroup>
