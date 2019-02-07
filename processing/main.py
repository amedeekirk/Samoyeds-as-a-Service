import pika
import os
import json
import numpy as np
from keras import backend as K

from nets import ImageNetNetwork
from determiner import combine_dictionaries, average
from image import convert


K.set_session(K.tf.Session(config=K.tf.ConfigProto(intra_op_parallelism_threads=1,
                                                   inter_op_parallelism_threads=1)))
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
IMAGE_SIZE = 224
MODE = os.getenv('MODE', 'local')

if MODE == 'production':
    print('===  Production')
    NETWORKS = [('seresnet50', IMAGE_SIZE),
                ('resnet101', IMAGE_SIZE),
                ('densenet169', IMAGE_SIZE),
                ('mobilenet', IMAGE_SIZE),
                ('resnet34', IMAGE_SIZE)]
    HOST = 'rabbitmq-server'
elif MODE == 'testing':
    import scripts.pika_test
    print('===  Testing')
    NETWORKS = [('mobilenet', IMAGE_SIZE)]
    HOST = 'rabbitmq-server'
else:
    HOST = '127.0.0.1'


print('===  Initializing/Downloading Networks')
image_networks = [ImageNetNetwork(*network) for network in NETWORKS]

connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_declare(queue='return_queue', durable=True)


def process(ch, method, properties, body):
    data = json.loads(body)
    image = convert(data['image'], IMAGE_SIZE)
    predictions = []

    if image:
        error = False
        image = np.array(image)
        list_predictions = []
        for network in image_networks:
            list_predictions.append(network.classify(image.copy()))
        predictions = average(combine_dictionaries(list_predictions))
    else:
        error = True

    data = {
        'idx': data['idx'],
        'path': data['path'],
        'predictions': predictions,
        'error': error
    }

    message = json.dumps(data)
    channel.basic_publish(exchange='',
                          routing_key='return_queue',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(process, queue='task_queue')

print('===  Listening')
channel.start_consuming()
