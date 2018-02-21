from multiprocessing import Process, Queue
import time
from func import url_extract, html_parser
import sys


def producer(urls, queue):
    for url in urls:
        try:
            message = url_extract(url)
            queue.put(message)
            print(" [x] Sent %r" % url)
        except Exception as e:
            print(' [x] %r' % e)


def consumer(queue, urls):
    for i in range(0, len(urls)):
        message = queue.get()
        output = html_parser(message)
        print(output)


if __name__ == '__main__':
    urls = sys.argv[1:]
    queue = Queue()
    consumer_1 = Process(target=consumer, args=(queue, urls))
    consumer_1.start()
    producer_1 = Process(target=producer, args=(urls, queue))
    producer_1.start()
    time.sleep(1)
    consumer_1.join()
    producer_1.join()
