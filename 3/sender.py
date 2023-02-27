import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()
ch.exchange_declare(exchange='logs',exchange_type='fanout')
ch.queue_declare(queue='first',durable=True)
message = 'This Is A Testing Message fanout'
ch.basic_publish(exchange='logs',routing_key='',body=message)
print('send message')
connection.close()
