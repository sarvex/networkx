#!/usr/bin/env python
"""
Compute some network properties for the lollipop graph.
"""

#    Copyright (C) 2004 by 
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

from networkx import *

G = lollipop_graph(4,6)

pathlengths=[]

print("source vertex {target:length, }")
for v in G.nodes():
    spl=single_source_shortest_path_length(G,v)
    print(f'{v} {spl}')
    pathlengths.extend(iter(spl.values()))
print('')
print(f"average shortest path length {sum(pathlengths) / len(pathlengths)}")

# histogram of path lengths 
dist={}
for p in pathlengths:
    if p in dist:
        dist[p]+=1
    else:
        dist[p]=1

print('')
print("length #paths")
verts=dist.keys()
for d in sorted(verts):
    print('%s %d' % (d,dist[d]))

print("radius: %d" % radius(G))
print("diameter: %d" % diameter(G))
print(f"eccentricity: {eccentricity(G)}")
print(f"center: {center(G)}")
print(f"periphery: {periphery(G)}")
print(f"density: {density(G)}")

