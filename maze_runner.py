from my_queue import Queue


def make_adjacency_list(grid: list) -> dict:
    adjacency_list = {}
    length = len(grid)
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            adjacency_list[(row, column)] = []

            for neighbor1 in range(-1, 2, 2):
                for neighbor2 in range(-1, 2, 2):
                    if 0 <= column + neighbor1 < length and 0 <= row + neighbor2 <= length\
                            and grid[row][column + neighbor1] != 1:
                        adjacency_list[(row, column)].append((row + neighbor2, column + neighbor1))

                    # if 0 <= row + neighbor < length and grid[row + neighbor][column] != 1:
                    #     adjacency_list[(row, column)].append((row + neighbor, column))


    return adjacency_list


def path_finder(grid: dict, start: tuple, stop: tuple):
    visited = set()
    queue = Queue()
    previous = {}

    queue.push((start, 0))
    visited.add(start)

    while len(queue) > 0:
        node, distance = queue.pop()

        if node == stop:
            return distance, previous

        try:
            for neighbor in grid.get(node):
                if neighbor not in visited:
                    queue.push((neighbor, distance + 1))
                    visited.add(neighbor)
                    previous[neighbor] = node
        except:
            pass

    return -2, previous

