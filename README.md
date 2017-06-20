# send_slack_from_backlog
send Slack message from backlog that using Tornado web framework 

注意： Python3.4.3 の利用を想定して作っています。2系だと多分エラーになります。

## 1チャネル版

- install Tornado and slackpy
    - pip install Tornado
    - pip install slackpy

- backlogtoslack.py 内の設定部分を修正します
    - Backlogドメイン
    - SlackのincommingHookのURL(Slackの設定から取得してください)
  
- srcディレクトリ配下をサーバに配置！
- backlogtoslack.py を起動します
- 以下urlをBacklogのwebhook機能に登録！
    - http://サーバドメイン:8888/backlog/slack?channel=表示させたいチャンネル名
        - ex) http://hogehoge.jp:8888/backlog/slack?channel=project-x

自分用ツールなのでエラー処理とかまだ作ってません。。。


## カテゴリによるチャネル切り替え

Azure Functions Appで動くPythonコードです。   
TODOと書かれている部分を修正してください。
**現在チケットの新規登録にのみ対応しています**

**LibディレクトリをKuduから配置してください(Function名ディレクトリ直下)**

