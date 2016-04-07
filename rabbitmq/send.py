#!/usr/local/python

import pika
import sys

message = ' '.join(sys.argv[1:]) or "Hello World!"

conn =pika.BlockingConnection(pika.ConnectionParameters('localhost'))
ch = conn.channel()

'''declare queue'''
#ch.queue_declare('hello')
ch.queue_declare('task_queue')

'publish msg to exchange'
#ch.basic_publish('', 'hello', 'Hello world, rabbitMQ!')


ch.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))

print(" [x] Sent %r" % message)

conn.close()