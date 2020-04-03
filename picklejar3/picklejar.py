# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2020 Kevin Walchko
# see LICENSE for full details
##############################################
import pickle

class PickleJar(object):
    def __init__(self):
        self.fd = None
        self.buffer = {}

    def __del__(self):
        self.close()

    def init(self, fname, buffer_size=500):
        self.fd = open(fname, 'wb')
        self.buffer = {}
        self.buffer_size = buffer_size
        self.counter = 0

    def push(self, topic, data):
        if not self.fd: raise Exception("PickleJar.init() not set")
        # self.buffer.append(data)
        if topic not in self.buffer:
            self.buffer[topic] = []
        self.buffer[topic].append(data)
        self.counter += 1
        if self.counter > self.buffer_size:
            self.write()
            self.counter = 0

    def read(self, fname):
        with open(fname, 'rb') as f:
            d = f.read()
            print(len(d))
            d = pickle.loads(d)
            print(d)

    def write(self):
        if not self.fd: raise Exception("PickleJar.init() not set")
        # for d in self.buffer:
        #     pickle.dump(d, self.fd)
        self.fd.write(pickle.dumps(self.buffer))
        print("w")
        print(self.fd)
        self.buffer = {}

    def close(self):
        if self.fd:
            if len(self.buffer) > 0:
                self.write()
            self.fd.close()
