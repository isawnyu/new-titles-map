# Based on quickstart.py from Google API documentation

from __future__ import print_function

import pickle
import os.path
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

#### ISAW Customization ####
# The ID and range of the BSN Add-on sheet
SPREADSHEET_ID = '1-ZLk7nfUcFH6jc8CNngikN5NvT5o-yooKLXygCYu8ms'
RANGE_NAME = 'nt_map_data_columns'
############################

def get_sheet_data(spreadsheet_id, range_name):
    """ WRITE DOCSTRING
    """
    ### DO NOT CHANGE - START
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('../token.pickle'):
        with open('../token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('../token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                range=range_name).execute()
    values = result.get('values', [])
    ### DO NOT CHANGE - END

    data = []

    if not values:
        print('No data found.')
    else:
        for row in values[1:]:
            data.append(row)

    return data

def convert_nt_map_data_columns(data):
    ## record google-sheet-column-number
    # date 0
    # precision_code 7
    # region 9
    # location 10
    # pleiades_id 2
    # latitute 12
    # longitude 12
    # bsn 17

    conv_data = []
    for i, row in enumerate(data):
        print(i)
        print(row)
        latlong = row[12]
        lat, long = None, None
        if latlong:
            if len(latlong.split(',')) == 2:
                lat = float(row[12].split(',')[0])
                long = float(row[12].split(',')[1])
        conv_data.append([row[0], int(row[7]), row[9], row[10], row[2], lat, long , row[17]])
    return conv_data

if __name__ == '__main__':
    data = get_sheet_data(SPREADSHEET_ID, RANGE_NAME)
    data = convert_nt_map_data_columns(data)
    print(data)
