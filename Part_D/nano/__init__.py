# Import main program
from __future__ import absolute_import, print_function, unicode_literals
from .Nano import Nano

def create_instance(c_insance):
    return Nano(c_insance)
