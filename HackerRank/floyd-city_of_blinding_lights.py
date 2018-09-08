#!/bin/python3
# https://www.hackerrank.com/challenges/floyd-city-of-blinding-lights/problem

import math

def floyd_warshall(n, edges):
    dist = [[math.inf] * n for _ in range(n)]
    for (u,v,w) in edges:
        dist[u][v] = w
    for v in range(n):
        dist[v][v] = 0
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(road_edges) ]
    for i in range(road_edges):
        (u,v,w) = edges[i]
        edges[i] = (u-1,v-1,w)
    dist = floyd_warshall(road_nodes, edges)

    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        d = dist[x-1][y-1]
        if math.isinf(d):
            print("-1")
        else:
            print(str(d))
