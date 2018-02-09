import pika
import sys
from func import url_extract 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='first', 
                        exchange_type='fanout')


urls = sys.argv[1:]

for url in urls:
    try:
        message = url_extract(url)
        channel.basic_publish(exchange='first', routing_key='', body=message)
        print(" [x] Sent %r" % url)
    except Exception as e:
        print(' [x] %r' % e)

connection.close()
