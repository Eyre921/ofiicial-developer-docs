---
title: "認証"
source: https://docs.x.com/ja/fundamentals/authentication/overview
path: ja/fundamentals/authentication/overview
---

X API は膨大な量のデータを扱います。このデータを開発者とユーザーの双方にとって安全に保つ方法が認証です。

X API は膨大な量のデータを扱い、認証によって開発者とユーザー双方のためにそのデータを保護します。以下に示すいくつかの認証方法から選択できます。

ほとんどの開発者は認証の複雑さを直接扱う必要はありません — クライアントライブラリが自動的に処理してくれます。

利用可能なクライアントライブラリのリストは [Tools and libraries](/resources/tools-and-libraries) ページで確認できます。

## 認証方法

<CardGroup>
  <Card title="OAuth 1.0a User Context" href="/resources/fundamentals/authentication/oauth-1-0a/api-key-and-secret">
    OAuth 1.0a により、認可された X デベロッパーアプリが X アカウントに代わって、プライベートなアカウント情報にアクセスしたり、X アクションを実行したりできます。

    <br />

    [**詳細はこちら**](/resources/fundamentals/authentication/oauth-1-0a/api-key-and-secret)
  </Card>

  <Card title="App only" href="/resources/fundamentals/authentication/oauth-2-0/overview">
    App only Access Token により、X デベロッパーアプリが X 上で公開されている情報にアクセスできます。

    <br />

    [**詳細はこちら**](/resources/fundamentals/authentication/oauth-2-0/overview)
  </Card>

  <Card title="ベーシック認証" href="/resources/fundamentals/authentication/basic-auth">
    X のエンタープライズ API の多くは HTTP ベーシック認証の使用を必要とします。

    <br />

    [**詳細はこちら**](/resources/fundamentals/authentication/basic-auth)
  </Card>

  <Card title="OAuth 2.0 Authorization Code Flow with PKCE" href="/resources/fundamentals/authentication/oauth-2-0/authorization-code">
    OAuth 2.0 User Context により、別のアカウントに代わって認証することができ、アプリケーションのスコープと複数のデバイスでの認可フローをよりきめ細かく制御できます。

    <br />

    [**詳細はこちら**](/resources/fundamentals/authentication/oauth-2-0/authorization-code)
  </Card>
</CardGroup>

<Note>
  **注:**
  アプリの API キー、App-only Access Token、個人の Access Token、Access Token Secret は、[Developer Console](/resources/fundamentals/developer-portal) の [X デベロッパーアプリ](/resources/fundamentals/developer-apps) セクションから取得できます。

  **他のユーザーに代わってリクエストを行うには**、[3-legged OAuth フロー](https://developer.x.com/resources/fundamentals/authentication/obtaining-user-access-tokens) を使用してそのユーザー向けに別のアクセストークンセットを生成し、OAuth 1.0a User Context または OAuth 2.0 user context リクエストでそのユーザーのトークンを渡します。
</Note>

## 追加リソース

<CardGroup>
  <Card title="ガイド" href="/resources/fundamentals/authentication/guides">
    統合ガイドを使用して、トークンの生成方法とリクエストの認証方法を学びましょう。
  </Card>

  <Card title="API リファレンス" href="/resources/fundamentals/authentication/api-reference">
    認証エンドポイントのリファレンスガイドを確認しましょう。
  </Card>

  <Card title="ベストプラクティス" href="/resources/fundamentals/authentication/guides/authentication-best-practices">
    キーとトークンを保存するためのベストプラクティスを理解し、自分自身を守ってください。
  </Card>

  <Card title="FAQ" href="/resources/fundamentals/authentication/faq">
    質問がありますか? FAQ をご覧ください。
  </Card>
</CardGroup>
