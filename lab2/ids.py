goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def next_states(state):
    zero = state.index(0)
    states = []

    for pos in moves[zero]:
        new_state = list(state)
        new_state[zero], new_state[pos] = new_state[pos], new_state[zero]
        states.append(tuple(new_state))

    return states


def depth_limited(state, depth, path, visited):
    if state == goal:
        return path

    if depth == 0:
        return None

    visited.add(state)

    for new_state in next_states(state):
        if new_state not in visited:
            result = depth_limited(
                new_state,
                depth - 1,
                path + [new_state],
                visited
            )

            if result is not None:
                return result

    visited.remove(state)
    return None


def is_solvable(state):
    arr = [x for x in state if x != 0]
    inversions = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1

    return inversions % 2 == 0


def ids(start):
    if not is_solvable(start):
        return None

    depth = 0

    while True:
        result = depth_limited(start, depth, [start], set())

        if result is not None:
            return result

        depth += 1


def print_solution(path):
    if path is None:
        print("No solution exists")
        return

    print("\nSolution:")
    print("Total moves:", len(path) - 1)

    for step, state in enumerate(path):
        print("\nStep", step)
        print(*state[0:3])
        print(*state[3:6])
        print(*state[6:9])


start = tuple(map(int, input("Enter puzzle: ").split()))

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input! Enter numbers 0 to 8 exactly once.")
else:
    path = ids(start)
    print_solution(path)
