import pika
import sys
from proba import url_extract 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='first', 
                        exchange_type='fanout')


messages = sys.argv[1:]

for message in messages:
    try:
        data = url_extract(message)
        channel.basic_publish(exchange='first', routing_key='', body=data)
        print(" [x] Sent %r" % message)
    except Exception as e:
        print(' [x] %r' % e)

connection.close()
