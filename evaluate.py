from config import Config
from os import listdir
from os.path import join
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from model import get_model


def get_single_test(dir):
    sz = 200
    test = np.zeros(shape=(sz, 160, 160, 1))
    cnt = 0
    for f in sorted(listdir(dir)):
        if str(join(dir, f))[-3:] == "tif":
            img = Image.open(join(dir, f)).resize((160, 160))
            img = np.array(img, dtype=np.float32) / 160.0

            test[cnt, :, :, 0] = img
            cnt = cnt + 1
    return test


def evaluate(dir):

    model = get_model(True)
    print("got model")
    test = get_single_test(dir)
    print("got test")
    sz = test.shape[0] - 10
    sequences = np.zeros((sz, 10, 160, 160, 1))
    # apply the sliding window technique to get the sequences
    for i in range(0, sz):
        clip = np.zeros((10, 160, 160, 1))
        for j in range(0, 10):
            clip[j] = test[i + j, :, :, :]
        sequences[i] = clip

    # get the reconstruction cost of all the sequences
    reconstructed_sequences = model.predict(sequences,batch_size=4)
    sequences_reconstruction_cost = np.array([np.linalg.norm(np.subtract(sequences[i],reconstructed_sequences[i])) for i in range(0,sz)])
    sa = (sequences_reconstruction_cost - np.min(sequences_reconstruction_cost)) / np.max(sequences_reconstruction_cost)
    sr = 1.0 - sa

    return sr