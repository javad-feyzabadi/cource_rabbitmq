import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()
ch.exchange_declare(exchange='direct_logs',exchange_type='fanout')

result = ch.queue_declare(queue='',exclusive=True)

queue_name=result.method.queue



severities = 'error'


ch.queue_bind(exchange='direct_logs',queue=queue_name,routing_key=severities)
print('waiting for message')

def callback(ch,method,properties,body):
    with open('error_logs.log','a') as el:
        el.write(str (f'{body}')+'\n')
    ch.basic_ack(delivery_tag = method.delivery_tag)


ch.basic_consume(queue=queue_name, on_message_callback=callback)

ch.start_consuming()