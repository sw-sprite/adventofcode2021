from collections import defaultdict, Counter
from functools import lru_cache
import itertools
import math
import string
import sys
import unittest

DICT = {"A": 1, "B": 10, "C": 100, "D": 1000}

def parse_input(i):
	out = [[], [], [], []]
	for idx, line in enumerate(i):
		if idx == 2 or idx == 3:
			row = [DICT[c] for c in line.split("#") if c != "" and c != "  " and c != "\n"]
			for idx in range(4):
				out[idx].append(row[idx])
	return out

class Node:

    def __init__(self, label, current_store=None, match=None):
        self.label = label
        self.current_store = current_store
        self.match = match

    def in_position(self):
        return self.code == self.match

class Graph:
    
    def __init__(self, num_nodes = 25):
        self.nodes = []
        for i in range(num_nodes):
            self.nodes.append(Node(i))
        
        self.edges = [(0,4), (1,5), (6,2), (7,3),
            (4,9), (4,10), (5,10), (5,11), (6,11), (6,12), (7,12),
            (8,9), (9,10), (10,11), (11,12), (12,13), (13,14)]
        self.edges = set(self.edges)

    def get_state(self):
        l = []
        for n in self.nodes:
            l.append((n.label, n.current_store))
        
        print(tuple(l))
        return tuple(l)

def pt1(i):
    position = [[0] * 11, [i[0][0], i[1][0], i[2][0], i[3][0]], [i[0][1], i[1][1], i[2][1], i[3][1]]]
    position = [tuple(p) for p in position]
    return 0

def solve():
    with open("input_1.txt") as f:    
        ipt = parse_input(f.readlines())
    
    print(pt1(ipt))
    # g = Graph()
    # g.nodes[0].current_store = 'D'
    # g.nodes[1].current_store = 'D'
    # g.nodes[2].current_store = 'B'
    # g.nodes[3].current_store = 'C'
    # g.nodes[4].current_store = 'A'
    # g.nodes[5].current_store = 'C'
    # g.nodes[6].current_store = 'B'
    # g.nodes[7].current_store = 'A'

    # states = {}
    # g.get_state()

solve()