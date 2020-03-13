# from .rabbitmqlib import RabbitStreamShareQueue
from libai_dev.rabbitmqlib import RabbitStreamShareQueue

message_obj = RabbitStreamShareQueue("localhost")

message_obj.consume_message('email_queue')
print(message_obj.callback())