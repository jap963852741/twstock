from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from pprint import pprint


global SiteNum
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
# SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'
class Googleinformation:
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = '123!A:Z'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName
    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        # home_dir = os.path.expanduser('~')
        home_dir = os.getcwd()
        credential_dir = os.path.join(home_dir, '.credentials')
        # print('112312313232123'+credential_dir)
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'sheets.googleapis.com-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE,SCOPES)
            flow.user_agent =APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials
    def main(self):
        """Shows basic usage of the Sheets API.
        Creates a Sheets API service object and prints the names and majors of
        students in a sample spreadsheet:
        https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
        """
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)

        spreadsheetId = self.spreadsheetId
        rangeName = self.rangeName
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=rangeName).execute()
        values = result.get('values', [])


        if not values:
            print('No data found.')
        else:
            # print('Name, Major:')
            # for row in values:
            #     # Print columns A and E, which correspond to indices 0 and 4.
            #     print('%s, ' % row)
            return values

    def write(self,List):
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)
        spreadsheet_id = self.spreadsheetId  # TODO: Update placeholder value.
        rangeName = self.rangeName
        value_input_option = 'USER_ENTERED'

        value_range_body = {
            "majorDimension": "COLUMNS",
            "values": [
                List,
            ]
        }

        request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                                               range=rangeName,
                                                               valueInputOption=value_input_option,
                                                               # insertDataOption=insert_data_option,
                                                               body=value_range_body)
        request.execute()
class The_Net_Asset_Valueinformation(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = '每股淨值(yahoo)!A:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName
class The_EPSinformation(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = 'EPS(hi_stock)!A:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName

class The_Debt_Asset_ratio_information(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = '負債資產比!A:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName


class The_Dividend_Payout_Ratio_information(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = '現金股利發放率!A:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName


class The_ROE_information(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = 'ROE!A:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName

class The_Tradin_volume_information(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = '交易量!A2:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName


class The_Establishment_time_information(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = '成立時間!A2:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName


class The_Buy_Sell_Point_information(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = '四大買點判斷!A2:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName

class The_Now_Tradin_volume_information(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = '即時交易量!A2:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName

class Regression_Price_information(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = '回歸預測!A2:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName
class Ex_Dividends_information(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = '除權息日期股利!A2:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName
class Buy_Sell_exceed_information(Googleinformation):
    def __init__(self,spreadsheetId = '1l156Q4E_HxpebTuzVFQk0MI1vayKFCwW_tTJSWxFjXg',rangeName = '買賣超!A2:E'):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName
if __name__=='__main__':
    A = Buy_Sell_exceed_information()
    List = [1,2,3]
    # print(A.get_SOP_Noteinformation())
    note = A.write(List)














