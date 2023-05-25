from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    import os
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    CLIENT_SECRET_FILE = r'/Users/deniz/Documents/Python/security detection(Internship)/securitydetection/client_secret_398946460996-s2nncaimr0a0i4fpvmt7l2dkpr2kigfu.apps.googleusercontent.com.json'
    # Scopes define the level of access you need
    SCOPES = ['https://www.googleapis.com/auth/account']

    credentials_path = CLIENT_SECRET_FILE#'''path/to/credentials.json'''
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)

    credentials = flow.run_local_server(port=0)

    service = build('account', 'v1', credentials=credentials)
    accounts = service.accounts().list().execute()
    accounts2=[]
    for account in accounts2['accounts']:
        accounts2.append(f"Account ID: {account['accountId']}")

    return HttpResponse(accounts2)