from networkx.algorithms import shortest_path
import networkx as nx

def getLeavesFromGraphImposingDistanceFromOrigin(G, path_lenght_from_main = 5, origin_name = 'culture'):
  leaves = []
  for n in G.nodes:
    #print(f'verify - ({G.in_degree(n)}, {len(nx.algorithms.shortest_paths.generic.shortest_path(G, n, "culture"))}) ({n})')
    if G.in_degree(n) == 0 and len(shortest_path(G, n, origin_name)) == path_lenght_from_main:
      leaves.append(n)
  return leaves

def getNodesFromOriginDistance(G: nx.DiGraph, origin_name='culture', distance=4):
  return [ n for n in G.nodes if len(shortest_path(G, n, origin_name)) == distance ]

def calculateAllSimilaritiesFromListWithGraph(G: nx.DiGraph, origin_name='culture'):
  nodes = getNodesFromOriginDistance(G, origin_name, 3)

  return nodes