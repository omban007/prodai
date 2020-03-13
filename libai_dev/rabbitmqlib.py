#!/usr/bin/env python
"""Author:- Datta Ban"""
"""This library for sending and recieving data via rabbitMQ service like kafka"""
import pika


class RabbitStreamShareQueue:

    def __init__(self, host):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host))

    def publish_message(self, queue, message_body):

        channel = self.connection.channel()
        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange='', routing_key=queue, body=message_body)
        self.connection.close()

    def consume_message(self, queue):
        channel = self.connection.channel()

        channel.queue_declare(queue=queue)

        channel.basic_consume(
            queue=queue, on_message_callback=self.callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
            return body
