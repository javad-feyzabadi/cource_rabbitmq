import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()
# create exchange => type = fanout
ch.exchange_declare(exchange='logs',exchange_type='fanout')
# create q => exclusive is default false  
result = ch.queue_declare(queue='',exclusive=True)
#queue name
queue=result.method.queue
# binding , queue = queue name
ch.queue_bind(exchange='logs',queue=queue)
print('waiting for logs')

def callback(ch,method,properties,body):
    print(f"Recived {body}")
    ch.basic_ack(delivery_tag = method.delivery_tag)


ch.basic_consume(queue=queue, on_message_callback=callback)

ch.start_consuming()