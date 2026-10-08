from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, RunReportRequest
)
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']

def get_ga4_credentials():
    creds = None
    if os.path.exists('token_ga4.pickle'):
        with open('token_ga4.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token_ga4.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def fetch_ga4_data(property_id: str, days: int = 28):
    """Fetch key GA4 metrics for the last N days vs previous period."""
    creds = get_ga4_credentials()
    client = BetaAnalyticsDataClient(credentials=creds)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="date")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="activeUsers"),
            Metric(name="bounceRate"),
            Metric(name="averageSessionDuration"),
            Metric(name="conversions"),
        ],
        date_ranges=[
            DateRange(start_date=f"{days}daysAgo", end_date="today"),
        ],
    )

    response = client.run_report(request)

    results = []
    for row in response.rows:
        results.append({
            "date": row.dimension_values[0].value,
            "sessions": float(row.metric_values[0].value),
            "active_users": float(row.metric_values[1].value),
            "bounce_rate": float(row.metric_values[2].value),
            "avg_session_duration": float(row.metric_values[3].value),
            "conversions": float(row.metric_values[4].value),
        })

    return results