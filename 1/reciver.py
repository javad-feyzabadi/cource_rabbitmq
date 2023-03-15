import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch2 = connection.channel()
ch2.queue_declare('hello')
def callback(ch,method,properties,body):
    print(f"Recive {body}")
ch2.basic_consume(queue='hello',on_message_callback=callback,auto_ack=True)
print('Waiting for message, To exist press ctl+c')
ch2.start_consuming()