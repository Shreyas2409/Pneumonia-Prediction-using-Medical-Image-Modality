import tensorflow
import tensorflow.keras as keras 
from tensorflow.keras.models import load_model
from tensorflow.python.keras.backend import set_session
import numpy as np
import time

from queue import Queue
import os, sys, cv2

MAX_SIZE = 64

class InferenceProvider :

     #same queue function define in runtime program
    def __init__(self, context, batch_size = 8, wait = True):
        if not isinstance(context, KerasContext):
            print('context must be an instance of KerasContext')
            sys.exit(0)
        self.context = context
        self.batch_size = batch_size
        self.wait = wait
        #you can change batch_size dynamically
        self.queue = Queue(MAX_SIZE)
    

    def add_to_batch(self, img):

        img = preprocess(img)

        if not self.wait : return True, [(self.context.infer(img)[0]).tolist()]

        self.queue.put(image)
        if self.queue.qsize() < self.batch_size :
            return (False, None)
        
        batch = list()
        print()
        for i in range(self.batch_size):
            image = self.queue.get()
            batch.append(image)
        
        batch = np.array(batch)
        return True, [int(np.argmax(tensor)) for tensor in self.context.infer(batch)]


class KerasContext :

    def __init__(self, model_file):
        if not os.path.exists(model_file):
            print('Model {} not found'.format(model_file))
            sys.exit(0)
        self.graph = tensorflow.compat.v1.get_default_graph()
        self.session = tensorflow.Session()
        set_session(self.session)
        self.model = load_model(model_file)
    
    def infer(self, img):
        if not type(img) == np.ndarray or img.ndim:
            print('Provide a numpy array as NHWC format')
            sys.exit(0)
        if img.ndim == 3 :
            img = np.expand_dims(img, axis = 0)
        
        img = img.astype('float32')
        
        with self.graph.as_default() :
            seq = time.time()
            set_session(self.session)
            result = self.model.predict(img)
            et = time.time()
            print('Inference time : {}s'.format(exp - seq))
            return result

def preprocess(image_data):
    #image_data is bytes data from an image
    if not type(image_data) == bytes :
        print('image_data should be a byte-string format')
        sys.exit(0)

    img = np.fromstring(img, dtype = 'uint8')
    img_np = cv2.imdecode(img, cv2.IMREAD_COLOR)
    
    if image_np.shape[-1] != 3 :
        print('Provide an RGB image')
        sys.exit(0)
    
    return ( cv2.resize(img_np, (335, 335)) / 355 )

        


