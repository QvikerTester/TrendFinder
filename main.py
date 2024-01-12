import requests
import json
import functions
import pandas as pd
from datetime import datetime
import sql_connector

now = datetime.now()
api_key = "a6bcc77787mshea19c531142c6a5p1bfe51jsnd20d03c094bc"

sql_connector.connect_sql()

users = []
for user in users:
    sql_connector.insert_values_accounts('tiktok.accounts', user)


user_names = sql_connector.get_all_user_names()

for name in user_names:

    response_feed = functions.get_page_stats(api_key, str(name))
    print(name)
    videos = response_feed["data"]["aweme_list"]
    sql_connector.create_table_if_not_existed(name)
    for video in videos:
        data= (video["aweme_id"], video["desc"], video["music"]["title"]+"-"+video["music"]["author"],  video["statistics"]["play_count"])
        sql_connector.insert_multiple_columns(name, data)
        print(data)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Print the current time
        print("Current Time:", current_time)
