import pika
import logging
import uuid
import json
import base64
import imghdr
from os import walk
import os

# images = []
# for (dirpath, _, filenames) in walk('images/'):
#     for filename in filenames:
#         if imghdr.what(dirpath + filename) in ['jpeg', 'jpeg', None]:
#             with open(dirpath + filename, 'rb') as f:
#                 image = f.read()
#                 images.append((base64.b64encode(image).decode('utf-8'), filename))
MODE = os.getenv('MODE', 'local')

if MODE == 'production':
    HOST = 'rabbitmq-server'
elif MODE == 'testing':
    HOST = 'rabbitmq-server'
else:
    HOST = '127.0.0.1'

f = open("samoyed.jpg", "rb")
i = f.read()
images = [(base64.b64encode(i).decode('utf-8'), 'samoyed.jpg')]

logging.basicConfig()
connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

for image in images:
    data = {
        'image': image[0],
        'path': image[1],
        'id': str(uuid.uuid4())
    }

    print("===  id: " + data['id'])
    message = json.dumps(data)

    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
print("===  Sent images from images directory")

connection.close()
