import torch
import bcolz

def save_array(data, fname):
    c=bcolz.carray(data, rootdir=fname, mode='w')
    c.flush()

def load_array(fname):
    return bcolz.open(fname)[:]

def one_hot_encode(value, value_range=11):
    one_hot = torch.zeros(value_range)
    one_hot[value] = 1
    return one_hot

def time_since(since):
    s = time() - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)