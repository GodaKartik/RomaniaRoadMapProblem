roadmap_as_graph = {
    "Arad": ["Zerind", "Timisoara", "Sibiu"], #
    "Zerind": ["Oradea", "Arad"], #
    "Timisoara": ["Arad", "Lugoj"], #
    "Sibiu": ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"], #
    "Oradea": ["Sibiu", "Zerind"], #
    "Lugoj": ["Timisoara", "Mehadia"], #
    "Fagaras": ["Sibiu", "Bucharest"], # 
    "Rimnicu Vilcea": ["Sibiu", "Pitesti", "Craiova"], #
    "Mehadia": ["Lugoj", "Dobreta"], #
    "Dobreta": ["Mehadia", "Craiova"], #
    "Craiova": ["Dobreta", "Rimnicu Vilcea", "Pitesti"], #
    "Pitesti": ["Rimnicu Vilcea", "Craiova", "Bucharest"], #
    "Bucharest": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"], 
    "Giurgiu": ["Bucharest"],
    "Urziceni" : ["Bucharest", "Hirsova", "Vaslui"],
    "Hirsova" : ["Urziceni","Eforie"],
    "Vaslui" : ["Iasi", "Urziceni"],
    "Iasi" : ["Vaslui", "Neamt"],
    "Neamt" : ["Iasi"]

}

heuristic_values = {
    "Arad": 366, 
    "Zerind": 374, 
    "Timisoara": 329, 
    "Sibiu": 253,
    "Oradea": 380,
    "Lugoj": 244, 
    "Fagaras": 176, 
    "Rimnicu Vilcea": 193, 
    "Mehadia": 241,
    "Dobreta": 242,
    "Craiova": 160, 
    "Pitesti": 98, 
    "Bucharest": 0, 
    "Giurgiu": 77,
    "Eforie" : 161,
    "Hirsova" : 151,
    "Iasi" : 226,
    "Neamt" : 234,
    "Urziceni" : 80,
    "Vaslui" : 199
}
