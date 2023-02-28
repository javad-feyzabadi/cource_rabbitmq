import pika
import uuid


class Sender:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.ch = self.connection.channel()
        result = self.ch.queue_declare(queue='',exclusive=True)
        self.queue_name = result.method.queue
        self.ch.basic_consume(queue=self.queue_name,on_message_callback=self.on_response,auto_ack=True)

    def on_response(self,ch,method,proper,body):
        if self.coor_id == proper.correlation_id:
            self.response = body

    def call(self,n):
        self.response = None
        self.coor_id = str(uuid.uuid4())
        send.ch.basic_publish(exchange='',routing_key='rpc_queue',
        properties=pika.BasicProperties(reply_to=self.queue_name,correlation_id=self.coor_id),body=str(n))                      
       
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)



send = Sender()

response = send.call(30)
print(response)