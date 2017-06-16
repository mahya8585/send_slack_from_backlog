import tornado.ioloop
import tornado.web
import json
import slackpy

from tornado.options import define, options

define(u"port", default=8888, help=u"run on the given port", type=int)
define(u"debug", default=False, help=u"run in debug mode")


class SendBacklogToSlackHandler(tornado.web.RequestHandler):
    """
        backlogからSlackへのメッセージ通信を行います。
    """
    # カテゴリ・チャネル対応表
    category_channel = {
        "IoT": "iot",
        "BigData/AI": "bigdata-ai",
        "Azure": "azure",
        "AWS": "aws",
        "DevOps": "devops",
        "品質管理": "test-qa",
        "戦略-マーケティング": "marketing",
        "戦略-育成": "college"
    }

    def create_message(self):
        """
        Slack通知用メッセージを作成します。
        :return:成形済みメッセージ
        """
        # 受け取ったjsonを辞書型に変換し、必要な項目を変数化します（辞書のままだと読みにくかったので
        json_dic = json.loads(self.request.body.decode('utf-8'))
        project_key = json_dic["project"]["projectKey"] + "-" + str(json_dic["content"]["key_id"])
        project_name = json_dic["project"]["name"]
        summary = json_dic["content"]["summary"]
        user_name = json_dic["createdUser"]["name"]

        # TODO backlogURL修正ください
        body_message = project_name + "<https://xxxx.backlog.jp/view/" + project_key + " | " + project_key + " " + summary + "> by " + user_name
        print(body_message)

        return body_message

    def send_slack(self, body_message):
        """
        特定のSlackへ文言送付します
        :param body_message:
        :return:
        """
        # TODO for文にしてカテゴリの数だけリクエストできるように作り直す
        # TODO SlackのincominghookのURLを指定してください。
        # incoming_url = "https://hooks.slack.com/services/T02xxxx/xxxx/xxxx/"
        incoming_url = "SlackのincominghookのURL"
        channel = "#std-" + self.get_argument(SendBacklogToSlackHandler.category_channel["カテゴリを抽出して設定"])
        user_name = "BackLogKeeper"
        logging = slackpy.SlackLogger(incoming_url, channel, user_name)

        logging.info(message=body_message)

    def post(self):
        """
        backlogからwebhookされるメソッドです。
        :return:slackへメッセージ送信
        """
        body_message = SendBacklogToSlackHandler.create_message(self)
        print(body_message)

        # ここでslackpyを呼び出すわけですよ。
        SendBacklogToSlackHandler.send_slack(self, body_message)

        # test用(debug用)にreturnページを返却しておきます。
        self.render("template/result.html")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/backlog/slack", SendBacklogToSlackHandler)
        ]

        tornado.web.Application.__init__(self, handlers)


def main():
    app = Application()
    app.listen(options.port)

    print(u"サーバを起動します。")
    # TODO ポートは現在9行目で8888に設定していますが、変更可能です。使いやすいように以下コメントを修正ください
    print(u"http://サーバドメイン:" + str(options.port) + u"/backlog/slack?channel=送付先チャンネル にアクセスしてください")
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
