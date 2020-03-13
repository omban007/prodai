from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from bs4 import BeautifulSoup
import time
import dateutil.parser as parser
import os

SCOPES = 'https://www.googleapis.com/auth/gmail.modify'

user_id = 'me'
label_id_one = 'INBOX'
label_id_two = 'UNREAD'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class GetGmailData:

    def gmail_auth(self):
        store = file.Storage(DIR_PATH+'/config_files/storage.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(DIR_PATH+'/config_files/credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

        return GMAIL

    def get_mssg_list(self, GMAIL, mssg_list, read_len, mark_unread=False):
        final_list = []

        for mssg in mssg_list[:read_len]:
            temp_dict = {}
            m_id = mssg['id']
            message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute()
            payld = message['payload']
            headr = payld['headers']

            for one in headr:
                if one['name'] == 'Subject':
                    msg_subject = one['value']
                    temp_dict['Subject'] = msg_subject
                else:
                    pass

            for two in headr:
                if two['name'] == 'Date':
                    msg_date = two['value']
                    date_parse = (parser.parse(msg_date))
                    m_date = (date_parse.date())
                    temp_dict['Date'] = str(m_date)
                else:
                    pass

            for three in headr:
                if three['name'] == 'From':
                    msg_from = three['value']
                    temp_dict['Sender'] = msg_from
                else:
                    pass

            temp_dict['Snippet'] = message['snippet']

            try:
                mssg_parts = payld['parts']
                part_one = mssg_parts[0]
                part_body = part_one['body']
                part_data = part_body['data']
                clean_one = part_data.replace("-", "+")
                clean_one = clean_one.replace("_", "/")
                clean_two = base64.b64decode(bytes(clean_one, 'UTF-8'))
                soup = BeautifulSoup(clean_two, "lxml")
                mssg_body = soup.body()

                temp_dict['Message_body'] = mssg_body
            except:
                pass

            # print(temp_dict)
            final_list.append(temp_dict)
            if mark_unread:
                GMAIL.users().messages().modify(userId=user_id, id=m_id, body={'removeLabelIds': ['UNREAD']}).execute()
        return final_list

    def read_inbox_emails(self, GMAIL, count):

        mssg_list = None
        time.sleep(2)

        read_msgs = GMAIL.users().messages().list(userId='me', labelIds=[label_id_one]).execute()

        if read_msgs['resultSizeEstimate']:
            mssg_list = read_msgs['messages']

        if mssg_list:
            mssg_len = len(mssg_list)
            if mssg_len <= count:
                inbox_messages = self.get_mssg_list(GMAIL, mssg_list, mssg_len)
            elif mssg_len >= count:
                inbox_messages = self.get_mssg_list(GMAIL, mssg_list, count)

        return inbox_messages

    def read_unread_emails(self, GMAIL):
        mssg_list = None
        time.sleep(2)
        mark_unread = True
        inbox_messages = None
        read_msgs = GMAIL.users().messages().list(userId='me', labelIds=[label_id_one, label_id_two]).execute()

        if read_msgs['resultSizeEstimate']:
            mssg_list = read_msgs['messages']

        if mssg_list:
            mssg_len = len(mssg_list)
            inbox_messages = self.get_mssg_list(GMAIL, mssg_list, mssg_len, mark_unread=mark_unread)

        return inbox_messages
