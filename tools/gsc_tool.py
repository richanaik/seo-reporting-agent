from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

def get_gsc_credentials():
    creds = None
    if os.path.exists('token_gsc.pickle'):
        with open('token_gsc.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token_gsc.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def fetch_gsc_data(site_url: str, days: int = 28):
    """Fetch GSC performance data — queries, clicks, impressions, CTR, position."""
    creds = get_gsc_credentials()
    service = build('searchconsole', 'v1', credentials=creds)

    end_date = datetime.today() - timedelta(days=3)  # GSC has 3-day delay
    start_date = end_date - timedelta(days=days)

    response = service.searchanalytics().query(
        siteUrl=site_url,
        body={
            'startDate': start_date.strftime('%Y-%m-%d'),
            'endDate': end_date.strftime('%Y-%m-%d'),
            'dimensions': ['query'],
            'rowLimit': 25,
            'orderBy': [{'fieldName': 'clicks', 'sortOrder': 'DESCENDING'}]
        }
    ).execute()

    results = []
    for row in response.get('rows', []):
        results.append({
            'query': row['keys'][0],
            'clicks': row['clicks'],
            'impressions': row['impressions'],
            'ctr': round(row['ctr'] * 100, 2),
            'position': round(row['position'], 1),
        })

    return results