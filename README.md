# Slackbot Sample

Pythonで簡単にSlack botを作りCloud Foundry上にデプロイしたい人向けのサンプル
ライブラリは↓使います。
https://github.com/lins05/slackbot


# Usage

1. https://api.slack.com/bot-users のcreating a new bot userをクリックして新しくBotを作成する
2. 適当なチャンネルに1.で作成したBotをInviteする
3. imgフォルダにあるpngファイルをすべてファイル名をemoji名としてslackに登録する
4. Botを取得する

```sh
$ git clone https://github.com/kazshinohara/slackbot_sample.git
$ cd slackbot_sample
```

5. 取得したslackbot_sampleディレクトリのmanifest.ymlに環境変数を追加する

```yaml
---
  ...
  - env:
      API_TOKEN: <1.のOAuth & Permissionsに書いてあるBot User OAuth Access Token>

```

6. Cloud FoundryにBotをPushする

```sh
$ cf login -a URL -u USER -p PASS
$ cf push <アプリ名> --health-check-type none
```
