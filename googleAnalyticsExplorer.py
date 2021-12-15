#!/usr/bin/env python

import os
from googleapiclient.discovery import build
from google.oauth2 import service_account

keyPath = os.getenv('SA_KEY_PATH', 'features.json')
tableID = os.getenv('TABLE_ID','123456789')
credentials = service_account.Credentials.from_service_account_file(keyPath)

scopedCredentials = credentials.with_scopes('https://www.googleapis.com/aut/analytics.readonly')

with build('analytics', 'v3', credentials=credentials) as service:
    realtimeData = service.data().realtime().get(
        ids = f'ga:{TABLE_ID}', metrics = 'rt: pageviews', dimensions = 'rt: pagePath'
    ).execute()

    print(realtimeData)