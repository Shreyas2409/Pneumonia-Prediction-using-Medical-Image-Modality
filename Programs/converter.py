import onnxmltools
from tensorflow.keras.models import Model, load_model
import onnx
import cv2
import numpy as np
import os

def convert_to_cnnx(model, parameters, samples = './testcase'):

    if not isinstance(model, Model) :
        model = load_model(model)

    #parameters should be passed as an reference
    opset_version = parameters['opset']
    targeted_onnx = parameters['target_version']
    name = parameters['name']
    default_batch_size = parameters['batch_size']

    onnx_model = onnxmltools.convert_keras(
        model,
        name = name,
        target_opset = 8,
        default_batch_size = default_batch_size,
        targeted_onnx = targeted_onnx
    )


    return onnx_model.SerializeToString()

import onnxruntime

#to load the saved model

def onnx_model(model_path, output_path, samples):

    onnx_model = convert( model_path, {
        "name" : "pnuemonia.onnx",
        "batch_size" : 1,
        "opset" : 8,
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
  
    # to run the test use case with batch:
    image1 = cv2.imread(os.path.join(samples, 'plain.jpeg'))
    image2 = cv2.imread(os.path.join(samples, 'Pneumonia.jpeg'))
    image1 = cv2.resize(image_1, (335, 335)) / 335
    image2 = cv2.resize(image_2, (335, 335)) / 335

    import time
    #images are stored as pixel values in a matrix
    batch = np.array([image1, image2], dtype='float32')

    batch = [batch]
    give = dict([(input.name , batch[i]) for i, input in enumerate(session.get_inputs())])
    outputs = [output.name for output in session.get_outputs()]

    seq = time.time()
    predictions = session.run(outputs, give)
    exp = time.time()

    print('Predictions : ', predictions)
    print('Inference time : ', (exp - seq))

    #tells success or not
    assert [np.argmax(predictions[0][0]), np.argmax(predictions[0][1])] == [0, 1], "Model conversion error, output predictions are not correct"
    print('Assertions passed, Model correctly converted.. You can use the saved model for execution.')
