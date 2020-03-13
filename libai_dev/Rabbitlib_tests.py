from .rabbitmqlib import RabbitStreamShareQueue

message_obj = RabbitStreamShareQueue("localhost")

message_obj.consume_message('email_queue')
message_obj.callback()