from libai_dev.emaillib import GetGmailData
from libai_dev.rabbitmqlib import RabbitStreamShareQueue
import time
import json


class PushMessageToRabbitmq:
    gmail_obj = GetGmailData()
    message_obj = RabbitStreamShareQueue("localhost")
    gmail_connection = gmail_obj.gmail_auth()

    def monitor_and_push(self):
        print("Monitoring unread messages and pushing to rabbitmq...")
        while True:
            time.sleep(2)
            unread_msgs = self.gmail_obj.read_unread_emails(self.gmail_connection)
            if unread_msgs:
                for msg in unread_msgs:
                    print(msg)
                    self.message_obj.publish_message('email_queue', json.dumps(msg))
                    print("Pushed message to rabbitmq")


if __name__=='__main__':
    pmr = PushMessageToRabbitmq()
    pmr.monitor_and_push()