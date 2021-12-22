import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch2 = connection.channel()

ch2.queue_declare(queue='hello')
print('Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch2.basic_qos(prefetch_count=1)
ch2.basic_consume(queue='hello', on_message_callback=callback)

ch2.start_consuming()