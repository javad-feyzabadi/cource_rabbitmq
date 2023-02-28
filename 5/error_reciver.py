import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()
ch.exchange_declare(exchange='topic_logs',exchange_type='topic')

result = ch.queue_declare(queue='',exclusive=True)
queue_name=result.method.queue 

binding_key = '*.*.important'
ch.queue_bind(exchange='topic_logs',queue=queue_name,routing_key=binding_key)
print('waiting for message')

def callback(ch,method,properties,body):
    with open('error_logs.log','a') as el:
        el.write(f'{str(body)})+\n')




ch.basic_consume(queue=queue_name, on_message_callback=callback,auto_ack=True)

ch.start_consuming()