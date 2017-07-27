# -*- coding: UTF-8 -*-
import os
import json
import platform
import sys
sys.path.append('Lib')
import requests


print(platform.python_version())

incoming_url = 'https://hooks.slack.com/services/xxxx/xxx/xxxx'
backlog_data = json.loads(open(os.environ['req']).read())
print(backlog_data)

project = backlog_data['project']
project_key = project['projectKey']

content = backlog_data['content']
summary = str(content['summary'].encode('utf-8'))
key_id = str(content['key_id'])

ticket_id = str(project_key + '-' + key_id)

if 'assignee' in content:
    assignee = '-> assignee : ' + content['assignee']['name'].encode('utf-8')
else:
    assignee = ''

message = '<https://xxx.backlog.jp/view/' + ticket_id + ' | ' + ticket_id + ' ' + summary + '> ' + str(assignee)
post_body = {
    'text': message,
    'username': 'BackLogKeeper',
    'icon_emoji': ':cop:',
    'channel': 'channel name'
}
header = {
    'Content-Type': 'application/json'
}
requests.post(incoming_url, headers=header, data=json.dumps(post_body))
print('send')

print('finish to send slack.')

