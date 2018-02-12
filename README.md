# Extractor
A Simple Web Link Extractor - 
Requires Rabbitmq server installed


Complete proccess flow:

1. Run consumer.py in a terminal. The Consumer is running continuously and waiting for producer's messages,
   and it can be stopped manualy with CTRL+C.
   

2. In a new terminal run producer.py with "python producer.py firs_url second_url...". The Producer needs 
   inputs(URLs in command line e.g http://www.txodds.com) that will be processed and sent as a message to the Consumer. 
   
   
3. After running producer.py, in that terminal will be printed urls which producer got and processed, and producer.py will
   stop running. In consumer.py terminal output will be printed on screen. Output can be saved in log file,
   by running the command "python consumer.py > any_name.log
   


The Producer extracts the markup from each URL it gets, and sends HTML to the Consumer. The Consumer parses HTML by 'a' tag and displays only http links as output.
