import onnxmltools
from tensorflow.keras.models import Model, load_model
import onnx
import cv2
import numpy as np
import os

#convert the model  from keras into onnx 
def convert(model, parameters, samples = './samples'):

    if not isinstance(model, Model) :
        model = load_model(model)

    #REFERENCE PARAMETERS
    opset_version = parameters['opset']
    targeted_onnx = parameters['target_version']
    name = parameters['name']
    default_batch_size = parameters['batch_size']
#using onnxmlmodel tool to convert the model from keras to onnx 
    onnx_model = onnxmltools.convert_keras(
        model,
        name = name,
        target_opset = 7,
        default_batch_size = default_batch_size,
        targeted_onnx = targeted_onnx
    )

   

    return onnx_model.SerializeToString()

# test case  run on the model 
import onnxruntime

#

def create_onnx(model_path, output_path, samples):

    onnx_model = convert( model_path, {
        "name" : "pnuemonia.onnx",
        "batch_size" : 1,
        "opset" : 7,
        "target_version" : onnx.__version__
    })

    options = onnxruntime.SessionOptions()
    options.enable_cpu_mem_arena = True
    options.enable_mem_pattern = True
    options.graph_optimization_level = onnxruntime.GraphOptimizationLevel.ORT_ENABLE_ALL
    options.optimized_model_filepath = output_path

    session = onnxruntime.InferenceSession(onnx_model, options)
    print('Inputs : ',  [ip.shape for ip in session.get_inputs()])
    print('Outputs : ', [op.shape for op in session.get_outputs()])
    #
    #Run test use case with batch:
    image_1 = cv2.imread(os.path.join(samples, 'no.jpeg'))#read the image
    image_2 = cv2.imread(os.path.join(samples, 'yes.jpeg'))
    image_1 = cv2.resize(image_1, (224, 224)) / 255. #we are dividing this by 255 because we in training we used this ratio 
    image_2 = cv2.resize(image_2, (224, 224)) / 255. #risizing the image

    import time
    batch = np.array([image_1, image_2], dtype='float32')

    batch = [batch]
    feed = dict([(input.name , batch[i]) for i, input in enumerate(session.get_inputs())])
    outputs = [output.name for output in session.get_outputs()]

    st = time.time()
    predictions = session.run(outputs, feed)
    et = time.time()

    print('Predictions : ', predictions)
    print('Inference time : ', (et - st))

    assert [np.argmax(predictions[0][0]), np.argmax(predictions[0][1])] == [0, 1], "Model conversion error, output predictions are not correct"
    print('Assertions passed, Model correctly converted.. You can use the saved model for execution.')
