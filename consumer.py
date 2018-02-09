import sys
import pika
from func import html_parser


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='first', 
                        exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='first',
                   queue=queue_name)

def callback(ch, method, properties, body):
    print('Next')
    ch.basic_ack(delivery_tag = method.delivery_tag)
    output = html_parser(body)
    print(output)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue=queue_name)

channel.start_consuming()
