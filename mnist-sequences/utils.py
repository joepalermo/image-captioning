import bcolz

def save_array(data, fname):
    c=bcolz.carray(data, rootdir=fname, mode='w')
    c.flush()

def load_array(fname):
    return bcolz.open(fname)[:]
