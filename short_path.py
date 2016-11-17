#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-07 18:46:17
# @Author  : Liu Jian (461698053@qq.com)
# @Link    : ${link}
# @Version : $Id$
from heapq import heappop, heappush
from copy import deepcopy

inf = float('inf')
'''
    参数说明:
        G:
        D:
        u:
        v:
        k:
'''


def relax(W, u, v, D, P):
    """
        松弛技术
    """
    d = D.get(u, inf) + W[u][v]
    if d < D.get(v, inf):
        D[v], P[v] = d, u
        return True


def bellman_ford(G, s):
    """
        最短路径:Bellman-Ford算法
    """
    D, P = {s: 0}, {}
    for rnd in G:
        changed = False
        for u in G:
            for v in G[u]:
                if relax(G, u, v, D, P):
                    changed = True
        if changed:
            raise ValueError('negative cycle!')
    return D, P


def dijkstra(G, s):
    """
        最短路径:Dijkstra算法
    """
    D, P, Q, S = {s: 0}, {}, [(0, s)], set()
    while Q:
        _, u = heappop(Q)
        if u in S:
            continue
        S.add(u)
        for v in G[u]:
            relax(G, u, v, D, P)
            heappush(Q, (D[v], v))
    return D, P


def johnson(G):
    """
        最短路径算法:Johnson,基于多对多的稀疏图
    """
    G = deepcopy(G)
    s = object()
    G[s] = {v: 0 for v in G}
    h, _ = bellman_ford(G, s)
    del G[s]
    for u in G:
        for v in G:
            G[u][v] += h[u] - h[v]
    D, P = {}, {}
    for u in G:
        D[u], P[u] = dijkstra(G, u)
        for v in G:
            D[u][v] += h[v] - h[u]
    return D, P


def floyd_warshall(G):
    """
        最短路径算法：Floyd Warshall，仅考虑距离
    """
    D = deepcopy(G)
    for k in G:
        for u in G:
            for v in G:
                D[u][v] = min(D[u][v], D[u][k], +D[k][v])
    return D


if __name__ == '__main__':
    main()
