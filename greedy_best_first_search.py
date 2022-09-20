from data import roadmap_as_graph, heuristic_values

def GreedyBestFirstSearch(graph, heuristics, start, target):

    # retruns path followed as a list
    
    path = [start] 
    next_child = start
    while next_child != target:
        child_heuristics = []
        sorted_children = []
        for city in graph[next_child]:
            h_val = heuristic_values[city]
            child_heuristics.append(h_val)
        sorted_child_heuristics = sorted(child_heuristics)
        lowest_h_val = sorted_child_heuristics[0]
        next_child = list(heuristics.keys())[list(heuristics.values()).index(lowest_h_val)]
        path.append(next_child)
    return path
  
  # using Arad to Bucharest as an example
  print(GreedyBestFirstSearch(roadmap_as_graph, heuristic_values, "Arad", "Bucharest"))
