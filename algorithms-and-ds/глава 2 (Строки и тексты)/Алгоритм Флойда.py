# coding: utf-8

inf = float("inf")

# Матрица вершин
V = [0, 1, 2, 3, 4]

# Матрица весов
weights = [
    [0, 1, inf, inf, 4],
    [1, 0, 5, 1, inf],
    [inf, 5, 0, 2, inf],
    [inf, 1, 2, 0, 1],
    [4, inf, inf, 1, 0]
]

# Матрица последователей
followers = [
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
]


def print_matrix(mx):
    for row in mx:
        print(" ".join((f"{col:>3}" for col in map(str, row))))
    print()


def floyd(w, f):
    """
    Алгоритм Флойда-Уоршелла
    :param w: матрица весов
    :param f: матрица последователей
    :return: матрицу
    """
    for j in V:
        print(f"Промежуточная вершина: {j + 1}")

        for u in V:
            for v in V:
                distance = w[u][j] + w[j][v]
                if distance < w[u][v]:
                    print(
                        f"Путь из вершины {u + 1} в {v + 1} "
                        f"через промежуточную вершину {j + 1} "
                        f"короче = {distance} (старое значение = {w[u][v]})"
                    )
                    w[u][v] = distance
                    w[v][u] = distance

                    f[u][v] = f[u][j]
                    f[v][u] = f[v][j]  # !!!

        print("Матрицы: ")
        print_matrix(w)
        print_matrix(f)
    return w, f


def get_lower_path(w, f, u, v):
    """
    Выводит кратчайший путь из вершины u в вершину v
    :param w: матрица весов
    :param f: матрица последователей
    :param u: начало
    :param v: конец
    :return:
    """

    if w[u][v] == inf:
        return []

    path = []
    while u != v:
        path.append(u)
        u = f[u][v]
    path.append(u)

    return path


# ----
# Считаем новые матрицы
# new_w - матрица весов
# new_f - матрица последователей
new_w, new_f = floyd(weights, followers)

print("Результат: ")
print_matrix(new_f)

# start - новая вершина
start = 1
for i in V:
    if i == start:
        continue

    lower_path = get_lower_path(weights, new_f, start, i)
    p = ' -> '.join(map(lambda s: f"{s + 1}", lower_path))
    print(f"Из {start + 1} в {i + 1} = {new_w[start][i]} ({p})")