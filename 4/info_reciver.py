import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()
ch.exchange_declare(exchange='direct_logs',exchange_type='direct')

result = ch.queue_declare(queue='',exclusive=True)

queue_name=result.method.queue 
# 3 message
severities = ('info','warning','error')
# becuse we have 3 message,  we shuld have 3 bind
for severity in severities:
    ch.queue_bind(exchange='direct_logs',queue=queue_name,routing_key=severity)
print('waiting for message')

def callback(ch,method,properties,body):
    print(f"{method.routing_key}, {body}")   


ch.basic_consume(queue=queue_name, on_message_callback=callback,auto_ack=True)

ch.start_consuming()