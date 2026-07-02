---
title: "Precios de la X API por uso y créditos"
source: https://docs.x.com/es/x-api/getting-started/pricing
path: es/x-api/getting-started/pricing
---

La X API usa precios de pago por uso, sin suscripciones. Paga solo por lo que consumas y gana hasta un 20% de devolución en créditos gratuitos de la xAI API.

La X API utiliza precios de **pago por uso**. Sin suscripciones: paga solo por lo que usas.

<Button href="https://developer.x.com/#pricing">Ver precios y comprar créditos</Button>

***

## Cómo funciona

<CardGroup>
  <Card title="Basado en créditos" icon="coins">
    Compra créditos por adelantado en la Developer Console. Los créditos se deducen a medida que realizas solicitudes a la API.
  </Card>

  <Card title="Precios por endpoint" icon="code">
    Diferentes endpoints tienen distintos costos. Consulta las tarifas actuales en la Developer Console.
  </Card>

  <Card title="Sin compromisos" icon="unlock">
    Sin contratos, suscripciones ni gasto mínimo. Comienza y detente cuando quieras.
  </Card>

  <Card title="Seguimiento en tiempo real" icon="gauge-high">
    Monitorea el uso y los costos en vivo desde la Developer Console.
  </Card>
</CardGroup>

<Tip>
  Gana créditos gratuitos de la [xAI API](https://docs.x.ai) cuando compras créditos de la X API: hasta un 20% de devolución según tu gasto. [Más información](#free-xai-api-credits)
</Tip>

***

## Detalles de consumo de créditos

Todos los precios son por recurso obtenido (lecturas) o por solicitud (escrituras/acciones). [Compra créditos](https://console.x.com) en la Developer Console.

### Operaciones de lectura

Se cobra por cada recurso devuelto en la respuesta.

| Recurso                       | Costo unitario      |
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

### Operaciones de escritura

Se cobra por solicitud.

| Acción                       | Costo unitario        |
| :--------------------------- | :-------------------- |
| **Post: Create**             | \$0.015 por solicitud |
| **Post: Create (with URL)**  | \$0.200 por solicitud |
| **Post: Create (summoned)**  | \$0.010 por solicitud |
| **DM Interaction: Create**   | \$0.015 por solicitud |
| **User Interaction: Create** | \$0.015 por solicitud |
| **Interaction: Delete**      | \$0.010 por solicitud |
| **Content: Manage**          | \$0.005 por solicitud |
| **List: Create**             | \$0.010 por solicitud |
| **List: Manage**             | \$0.005 por solicitud |
| **Bookmark**                 | \$0.005 por solicitud |
| **Media Metadata**           | \$0.005 por solicitud |
| **Privacy: Update**          | \$0.010 por solicitud |
| **Mute: Delete**             | \$0.005 por solicitud |
| **Counts: Recent**           | \$0.005 por solicitud |
| **Counts: All**              | \$0.010 por solicitud |
| **Trends**                   | \$0.010 por solicitud |

<Note>
  Los precios están sujetos a cambios. Las tarifas actuales siempre están disponibles en la [Developer Console](https://console.x.com) y en la [página de precios de developer.x.com](https://developer.x.com/#pricing).
</Note>

### Eventos de webhook

Los eventos de webhook entregados a través de la [X Activity API](/x-api/activity/introduction) se cobran por evento entregado, usando los mismos nombres de evento que se muestran en la documentación de la Activity API. Se te cobra una vez por cada evento facturable, deduplicado dentro de la misma ventana de 24 horas UTC que los demás recursos.

| Evento                   | Costo por evento |
| :----------------------- | :--------------- |
| `post.create`            | \$0.005          |
| `post.delete`            | No se cobra      |
| `follow.follow`          | \$0.010          |
| `follow.unfollow`        | \$0.010          |
| `profile.update.*`       | \$0.005          |
| `chat.received`          | \$0.010          |
| `chat.sent`              | No se cobra      |
| `chat.conversation_join` | No se cobra      |
| `dm.received`            | \$0.010          |
| `dm.sent`                | No se cobra      |
| `dm.read`                | No se cobra      |
| `dm.indicate_typing`     | No se cobra      |
| `news.new`               | \$0.005          |
| `spaces.start`           | \$0.005          |
| `spaces.end`             | \$0.005          |

***

## Owned Reads

Las Owned Reads son solicitudes realizadas por tu propia developer app para acceder a tus propios datos (posts, marcadores, seguidores, likes, listas y más). Estos endpoints tienen un precio de **\$0.001 por recurso** (1,000 recursos por \$1).

Los siguientes endpoints califican para los precios de Owned Read cuando `{id}` coincide con el usuario autenticado y ese usuario es el propietario de la developer app:

| Endpoint                             | Descripción                 |
| :----------------------------------- | :-------------------------- |
| `GET /2/users/{id}/tweets`           | Tus propios posts           |
| `GET /2/users/{id}/mentions`         | Tus menciones               |
| `GET /2/users/{id}/liked_tweets`     | Posts a los que diste like  |
| `GET /2/users/{id}/bookmarks`        | Tus marcadores              |
| `GET /2/users/{id}/followers`        | Tus seguidores              |
| `GET /2/users/{id}/following`        | Cuentas que sigues          |
| `GET /2/users/{id}/blocking`         | Cuentas que bloqueaste      |
| `GET /2/users/{id}/muting`           | Cuentas que silenciaste     |
| `GET /2/users/{id}/owned_lists`      | Listas que posees           |
| `GET /2/users/{id}/followed_lists`   | Listas que sigues           |
| `GET /2/users/{id}/list_memberships` | Listas a las que perteneces |
| `GET /2/users/{id}/pinned_lists`     | Tus listas fijadas          |

<Tip>
  Las Owned Reads hacen que sea significativamente más económico construir aplicaciones que trabajen con los datos del propio usuario, como dashboards, analítica personal o herramientas de gestión de cuentas.
</Tip>

***

## Deduplicación

Todos los recursos se deduplican dentro de una **ventana de 24 horas UTC**. Si solicitas un recurso (como un Post) y se te cobra por él, volver a solicitar el mismo recurso dentro de esa ventana no generará un cargo adicional.

Esto significa que:

* Solicitar el mismo Post varias veces en un día cuenta como un solo cargo
* La ventana de deduplicación se reinicia a la medianoche UTC
* Esto aplica a todos los recursos facturables (Posts, usuarios, etc.)

<Note>
  La deduplicación es una **garantía blanda**. Si bien ocurre en la gran mayoría de los casos, pueden existir situaciones específicas, como interrupciones del servicio, en las que los recursos no se dedupliquen.
</Note>

***

## Saldo de créditos

Tu saldo de créditos se muestra en la Developer Console. Los créditos se deducen en tiempo real a medida que realizas solicitudes a la API.

<Warning>
  Monitorea tu saldo de créditos con regularidad para evitar interrupciones del servicio. Agrega créditos antes de que tu saldo llegue a cero para asegurar un acceso ininterrumpido a la API.

  ***Nota:** Es posible que el saldo de créditos de una cuenta se vuelva ligeramente negativo. En ese caso, las solicitudes a la API serán bloqueadas hasta que agregues créditos para cubrir el saldo negativo.*
</Warning>

### Recarga automática

Activa la recarga automática para reponer tu saldo de créditos de forma automática y evitar interrupciones del servicio. Configura esto en la Developer Console:

| Configuración            | Descripción                                                                                |
| :----------------------- | :----------------------------------------------------------------------------------------- |
| **Monto de recarga**     | El monto que se agrega cuando se activa la recarga automática (p. ej., \$25)               |
| **Umbral de activación** | La recarga automática se activa cuando tu saldo cae por debajo de este monto (p. ej., \$5) |

<Note>
  La recarga automática requiere un método de pago guardado como predeterminado. Puedes cancelarla en cualquier momento desde la Developer Console o contactando con soporte.
</Note>

#### Salvaguardas de la recarga automática

Para protegerte de cargos descontrolados o inesperadamente grandes, la recarga automática incluye dos límites integrados:

* **Una recarga por ventana de 5 minutos.** Los cargos automáticos pueden activarse como máximo una vez cada 5 minutos, de modo que un pico repentino de uso no puede acumular varias recargas consecutivas.
* **Pausada con saldo cero o negativo.** La recarga automática no se ejecuta mientras el saldo de tu cuenta sea cero o negativo. Agrega créditos manualmente para reanudar las recargas automáticas.

<Warning>
  Si tu uso es lo suficientemente intermitente como para agotar una recarga completa en menos de 5 minutos, aún podrías ver errores de "sin créditos" incluso con la recarga automática activada. Aumenta tu **Monto de recarga** para que una sola recarga supere cómodamente una ventana de 5 minutos de tu consumo máximo.
</Warning>

***

### Límites de gasto

Establece un monto máximo que puedes gastar por ciclo de facturación para controlar los costos. Cuando se alcanza el límite, las solicitudes a la API serán bloqueadas hasta el siguiente ciclo de facturación.

| Opción              | Descripción                                                                            |
| :------------------ | :------------------------------------------------------------------------------------- |
| **Límite de gasto** | Establece un monto en dólares específico como tu gasto máximo por ciclo de facturación |

<Tip>
  Usa los límites de gasto para prevenir cargos inesperados, especialmente durante el desarrollo y las pruebas.
</Tip>

***

## Créditos gratuitos de la xAI API

Cuando compras créditos de la X API, puedes ganar créditos gratuitos de la [xAI API](https://docs.x.ai) en función de tu gasto acumulado durante un ciclo de facturación.

<Note>
  Para recibir créditos gratuitos de xAI, debes vincular tu equipo de xAI con tu cuenta de developer de X. Puedes hacerlo visitando la configuración de tu cuenta en la [developer console](https://console.x.com).
</Note>

### Cómo funciona

Tu gasto acumulado se rastrea a lo largo de cada ciclo de facturación. A medida que cruzas los umbrales de gasto, desbloqueas tasas de recompensa más altas. Cuando comienza un nuevo ciclo de facturación, tu gasto acumulado se reinicia a \$0.

| Gasto acumulado | Tasa |
| :-------------- | :--- |
| \$0 – \$199     | 0%   |
| \$200 – \$499   | 10%  |
| \$500 – \$999   | 15%  |
| \$1,000+        | 20%  |

<Note>
  La tasa se aplica a tu **saldo acumulado completo**, pero solo recibes el delta: lo que se te debe nuevamente menos lo que ya se te acreditó.
</Note>

### Ejemplo

Supón que realizas varias compras a lo largo de un ciclo de facturación:

| Compra      | Tasa | Total adeudado | Ya acreditado | Recibes     |
| :---------- | :--- | :------------- | :------------ | :---------- |
| \$100       | 0%   | \$0            | \$0           | **\$0**     |
| \$100       | 10%  | \$20           | \$0           | **\$20**    |
| \$150       | 10%  | \$35           | \$20          | **\$15**    |
| \$150       | 15%  | \$75           | \$35          | **\$40**    |
| \$250       | 15%  | \$112.50       | \$75          | **\$37.50** |
| \$250       | 20%  | \$200          | \$112.50      | **\$87.50** |
|             |      |                |               |             |
| **\$1,000** |      |                |               | **\$200**   |

Esta es la misma cantidad que recibirías por una sola compra de \$1,000: el orden y el tamaño de las compras no afectan tus recompensas totales.

<Tip>
  Consulta tu saldo de créditos de xAI y administra tu cuenta en [console.x.ai](https://console.x.ai). Para más detalles sobre la facturación de la xAI API, consulta la [documentación de facturación de xAI](https://docs.x.ai/docs/key-information/billing).
</Tip>

***

## Monitoreo del uso

Rastrea el uso de tu API de forma programática con el [endpoint de Usage](/x-api/usage/introduction):

```bash theme={null}
curl "https://api.x.com/2/usage/tweets" \
  -H "Authorization: Bearer $BEARER_TOKEN"
```

Esto devuelve los conteos diarios de consumo de Posts, ayudándote a:

* Rastrear el consumo en relación con tu presupuesto
* Configurar alertas cuando te acerques a los límites
* Identificar los endpoints con mayor consumo
* Generar informes de uso

***

## Próximos pasos

<CardGroup>
  <Card title="Developer Console" icon="grid-2" href="https://console.x.com">
    Compra créditos y consulta los precios actuales.
  </Card>

  <Card title="Usage API" icon="chart-line" href="/x-api/usage/introduction">
    Monitorea el uso de forma programática.
  </Card>
</CardGroup>
