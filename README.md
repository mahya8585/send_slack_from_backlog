# send_slack_from_backlog
send Slack message from backlog that using Tornado web framework 

注意： Python3.4.3 の利用を想定して作っています。2系だと多分エラーになります。

how to use.
- install Tornado and slackpy
    - pip install Tornado
    - pip install slackpy
  
- srcディレクトリ配下をサーバに配置！
- backlogtoslack.py を起動します
- 以下urlをBacklogのwebhook機能に登録！
    - http://サーバドメイン:8888/backlog/slack?channel=表示させたいチャンネル名
        - ex) http://hogehoge.jp:8888/backlog/slack?channel=project-x

自分用ツールなのでエラー処理とかまだ作ってません。。。
