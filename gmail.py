import os

import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import file
from oauth2client import tools


class Mail(object):
    _scopes = 'https://www.googleapis.com/auth/gmail.readonly'
    _client_secret_file = 'client_secret.json'
    _application_name = 'USB Notifier'

    def __init__(self):
        credentials = self.get_credentials()
        self._http = credentials.authorize(httplib2.Http())

    def get_credentials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')

        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)

        credential_path = os.path.join(credential_dir, 'redspace-gmail.json')

        store = file.Storage(credential_path)
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self._client_secret_file, self._scopes)
            flow.user_agent = self._application_name
            credentials = tools.run_flow(flow, store)
            print('Storing credentials to ' + credential_path)

        return credentials

    def unread_messages(self):
        service = discovery.build('gmail', 'v1', http=self._http)
        results = service.users().labels().get(userId='me', id='INBOX').execute()

        return results.get('messagesUnread')
