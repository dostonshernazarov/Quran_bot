
import pika
import json
import sys
import signal

def handle_sigint(sig, frame):
    print("Stopping producer...")
    sys.exit(0)

def Send_message(chapter, verse, text, user_name):
    signal.signal(signal.SIGINT, handle_sigint)

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='messages')

    try:

        # message = f"Text: {text}"
        channel.basic_publish(exchange='', routing_key='messages', body=json.dumps({'message': text, 'chapter': chapter, 'verse': verse, 'user': user_name}))
        # print("Message sent:", text)
    except KeyboardInterrupt:
        print("Stopping producer...")
        connection.close()



