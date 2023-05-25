from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
def index(request):
    import os
    import google_auth_oauthlib.flow 
    import googleapiclient.discovery 

    CLIENT_SECRET_FILE = r'/Users/deniz/Documents/Python/security detection(Internship)/securitydetection/client_secret_398946460996-s2nncaimr0a0i4fpvmt7l2dkpr2kigfu.apps.googleusercontent.com.json'

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    CLIENT_SECRET_FILE,
    scopes=['https://www.googleapis.com/auth/bigquery'])#['https://www.googleapis.com/auth/drive.metadata.readonly'])

    
    flow.redirect_uri = 'https://127.0.0.1:8000/auth/google'

    authorization_url, state = flow.authorization_url(access_type='offline',include_granted_scopes='true')

    return redirect(authorization_url)