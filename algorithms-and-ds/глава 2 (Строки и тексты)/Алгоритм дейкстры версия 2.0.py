import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph} # Словарь, для хранения расстояний
    distances[start] = 0 #расстояние до начальной вершины
    queue = [(0, start)]#Очередь для хранения расстояний и вершин

    while queue:
        current_distance, current_node = heapq.heappop(queue)#Извлекаем самый маленький элемент из кучи
# Если текущее расстояние до вершины уже больше, чем сохранённое расстояние, игнорируем её.
        if current_distance > distances[current_node]:
            continue
#Рассмотр соседних вершин
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            #Если найден более короткий путь, обновим расстояние
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1},
    'C': {'B': 1, 'A': 5}
}

dijkstra_result = dijkstra(graph, 'A')#Начальная вершина A
print(dijkstra_result)
