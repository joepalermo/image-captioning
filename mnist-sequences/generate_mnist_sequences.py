from __future__ import print_function, division
from mnist_sequence_api import MNIST_Sequence_API
import numpy as np
from utils import save_array, load_array

seq_len = 5 # generate sequences of this length
api_object = MNIST_Sequence_API()

def generate_data(n, seq_len, image_width, spacing_range=(0,0)):
    inputs = []
    labels = []
    for i in range(n):
        seq_values = np.random.randint(0, 10, seq_len)
        seq = api_object.generate_mnist_sequence(seq_values, spacing_range, image_width)
        seq = (255 - seq) / 255 # normalize the data
        inputs.append(seq)
        labels.append(seq_values)
    return np.array(inputs), np.array(labels)

n_train = 500
inputs, labels = generate_data(n_train, seq_len, 28*seq_len)
save_array(inputs, "data/train_inputs.bc")
save_array(labels, "data/train_labels.bc")

n_validation = 250
inputs, labels = generate_data(n_validation, seq_len, 28*seq_len)
save_array(inputs, "data/test_inputs.bc")
save_array(labels, "data/test_labels.bc")
