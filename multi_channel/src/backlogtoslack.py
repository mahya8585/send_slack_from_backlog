# -*- coding: UTF-8 -*-
import os
import json
import platform
import sys
sys.path.append('Lib')
import requests


print(platform.python_version())
category_channel = {
    'IoT': 'iot',
    'BigData/AI': 'bigdata-ai',
    'Azure': 'azure',
    'AWS': 'aws',
    'DevOps': 'devops'
}

# TODO incomminghook のurlを設定してください
incoming_url = 'https://hooks.slack.com/services/xxxxxxxxxxM'
backlog_data = json.loads(open(os.environ['req']).read())
print(backlog_data)

project = backlog_data['project']
project_key = project['projectKey']

content = backlog_data['content']
summary = str(content['summary'].encode('utf-8'))
categories = content['category']
key_id = str(content['key_id'])

ticket_id = str(project_key + '-' + key_id)

if content['assignee'] is None:
    assignee = '未設定'
else:
    assignee = content['assignee']['name'].encode('utf-8')

for category in categories:
    category_name = category['name'].encode('utf-8')
    
    # TODO 各自のチャネル振り分け制御を行ってください
    channel = '#backlog'
    if category_name in category_channel:
        channel = channel + '-' + category_channel[category_name]

    # TODO 利用しているbacklogのドメインを指定してください
    message = '<https://xxxxx.backlog.jp/view/' + ticket_id + ' | ' + ticket_id + ' ' + summary + '> -> assignee : ' + str(assignee)
    post_body = {
        'text': message,
        'username': 'BackLogKeeper',
        'icon_emoji': ':heart:',
        'channel': channel
    }
    header = {
        'Content-Type': 'application/json'
    }
    requests.post(incoming_url, headers=header, data=json.dumps(post_body))
    print('send to ' + channel + ' from category:' + category_name)

print('finish to send slack.')
