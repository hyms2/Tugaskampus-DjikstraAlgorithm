from collections import deque

def dijkstra_shortest_path(graph, start, destination):
    if start not in graph or destination not in graph:
        return[]
    queue = deque([(start, 0)])
    visited = set([(start)])
    distance = {start:0}
    parent = {start:None}
    
    while queue:
        vertex, dist = queue.popleft()
        
        if vertex == destination:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            path.reverse()
            return path
            
        for neighbor, value in graph[vertex].items():
            if neighbor not in visited:
                queue.append((neighbor, dist + value))
                visited.add(neighbor)
                distance[neighbor] = dist + value
                parent[neighbor] = vertex
    return[]

map_graph = {
    'Ambon':{'Bandung':80,'Tangerang':30},
    'Bandung':{'Ambon':80,'Cimahi':67,'Surabaya':76},
    'Cimahi':{'Bandung':67,'Depok':87,'Gorontalo':56},
    'Depok':{'Cimahi':87,'Pasuruan':40},
    'Tangerang':{'Ambon':30,'Surabaya':87,'Madiun':32},
    'Surabaya':{'Tangerang':87,'Bandung':76,'Gorontalo':89,'Jakarta':90},
    'Gorontalo':{'Surabaya':89,'Cimahi':56,'Pasuruan':87,'Kupang':99},
    'Pasuruan':{'Gorontalo':87,'Depok':40,'Lubuklinggau':65},
    'Madiun':{'Tangerang':32,'Jakarta':65},
    'Jakarta':{'Madiun':65,'Kupang':87,'Surabaya':90},
    'Kupang':{'jakarta':87,'Gorontalo':99,'Lubuklinggau':45},
    'Lubuklinggau':{'Pasuruan':65,'Kupang':45}
}

destination_city = input("Enter your destination: ")
start_city = input("Enter you start: ")

shortest_path = dijkstra_shortest_path(map_graph, start_city, destination_city)

if shortest_path:
    print("Shortest path: ", ' -> '.join(shortest_path))
else:
    print("No path found.")