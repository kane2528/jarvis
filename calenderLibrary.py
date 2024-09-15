from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import datetime
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google():
    """Authenticate the user and return a Google Calendar service instance."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service

def get_today_schedule():
    """Fetch today's events from Google Calendar"""
    service = authenticate_google()
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    end_of_day = (datetime.datetime.utcnow() + datetime.timedelta(hours=23, minutes=59)).isoformat() + 'Z'
    
    events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=end_of_day,
                                          singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return "You have no events today."
    
    schedule = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        schedule.append(f"{event['summary']} at {start}")

    return ', '.join(schedule)

def add_event(summary, start_time, end_time):
    """Add an event to the Google Calendar"""
    service = authenticate_google()
    
    event = {
      'summary': summary,
      'start': {
        'dateTime': start_time,
        'timeZone': 'UTC',
      },
      'end': {
        'dateTime': end_time,
        'timeZone': 'UTC',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return f"Event created: {event.get('htmlLink')}"
