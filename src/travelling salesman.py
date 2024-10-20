from itertools import permutations
from time import time

from graphs import graph_12_points

# Функция для вычисления расстояния пути
def calculate_path_distance(path, graph):
    distance = 0
    for i in range(len(path) - 1):
        start, end = path[i], path[i + 1]
        distance += graph[start].get(end, float("inf"))
    # Добавляем расстояние для возвращения в начальный пункт
    distance += graph[path[-1]].get(path[0], float("inf"))
    return distance


# Функция решения задачи коммивояжёра
def solve_tsp(graph, start_node):
    # Получаем список всех городов, кроме начального
    cities = list(graph.keys())
    cities.remove(start_node)

    shortest_path = None
    min_distance = float("inf")

    # Проходим по всем перестановкам городов
    for perm in permutations(cities):
        path = [start_node] + list(perm)
        distance = calculate_path_distance(path, graph)
        if distance < min_distance:
            min_distance = distance
            shortest_path = path

    return shortest_path, min_distance


# Решение задачи коммивояжёра для заданного графа с началом в "Гудермес"
start_time = time()
solution_path, solution_distance = solve_tsp(graph_12_points, "Гудермес")
end_time = time()

print(f"Оптимальный маршрут: {solution_path}")
print(f"Общая длина пути: {solution_distance} км")
print(f"Время затраченное на поиск: {end_time - start_time}")
