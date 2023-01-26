import sys

def get_line(): 
    return sys.stdin.readline().rstrip()

def get_ints():
    return map(int,get_line().split())

def print_array(array):
    for i in range(len(array)):
            print(array[i])