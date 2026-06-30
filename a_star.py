import heapq
import math

   
graph = {
    'A': [('B', 2.82), ('C', 3.16)],
    'B': [('A', 2.82)],
    'C': [('A', 3.16), ('D', 2.23), ('F', 5.0)],
    'D': [('C', 2.23), ('E', 2.24), ('H', 4.47), ('G', 3.6)],
    'E': [('D', 2.24)],
    'F': [('C', 5.0)],
    'G': [('D', 3.6), ('H', 1.0), ('I', 2.0)],
    'H': [('D', 4.47), ('G', 1.0), ('I', 1.0)],
    'I': [('G', 2.0), ('H', 1.0)]
}

 
   
coordinates = {
    'A': (0, 6),
    'B': (2, 8),
    'C': (1, 3),
    'D': (3, 4),
    'E': (2, 1),
    'F': (4, 7),
    'G': (6, 2),
    'H': (7, 1),
    'I': (8, 2)
}

def euclidean_distance(node1, node2):
    x1, y1 = coordinates[node1]
    x2, y2 = coordinates[node2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start, 0, [start]))
    closed_set = set()
    
    step = 1
    
    while open_set:
        f_value, current_node, g_value, path = heapq.heappop(open_set)
        
        print(f"Step {step}:")
        print(f"  Node: {current_node}")
        print(f"  g({current_node}) = {g_value:.2f}")
        print(f"  h({current_node}) = {euclidean_distance(current_node, goal):.2f}")
        print(f"  f({current_node}) = {f_value:.2f}")
        
        if current_node == goal:
            print(f"\nPath: {' -> '.join(path)}")
            print(f"Total Cost: {f_value:.2f}")
            return path, f_value
        
        closed_set.add(current_node)
        
        if current_node in graph:
            for neighbor, cost in graph[current_node]:
                if neighbor not in closed_set:
                    new_g = g_value + cost
                    h = euclidean_distance(neighbor, goal)
                    new_f = new_g + h
                    new_path = path + [neighbor]
                    heapq.heappush(open_set, (new_f, neighbor, new_g, new_path))
        
        step += 1
        print()
    
    return None, float('inf')

path, cost = a_star('A', 'I')
