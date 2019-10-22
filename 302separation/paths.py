#!/usr/bin/env python3

import sys

def pre_compute(w, n):
    for i in range(n):
        for j in range(n):
            if w[i][j] == 0:
                w[i][j] = 2*n + 1
    return w

def post_compute(w, n, max):
    for i in range(n):
        for j in range(n):
            if w[i][j] == 2*n + 1 or (w[i][j] > max):
                w[i][j] = 0
    return w

def compute_shortest_path_matrix(adjacency_matrix, max):
    w = adjacency_matrix
    n = len(w)
    w = pre_compute(w, n)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (i != j):
                    w[i][j] = min(w[i][j], w[i][k] + w[k][j])
    w = post_compute(w, n, max)
    return w