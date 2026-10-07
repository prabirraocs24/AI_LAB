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

        # Swap 0 with adjacent tile
        new_state[zero], new_state[pos] = \
            new_state[pos], new_state[zero]

        states.append(tuple(new_state))

    return states


def dfs(start):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for new_state in next_states(state):
            if new_state not in visited:
                stack.append(
                    (new_state, path + [new_state])
                )

    return None


def print_solution(path):
    if path is None:
        print("No solution")
        return

    print("\nSolution:")
    print("Number of moves:", len(path) - 1)

    for i, state in enumerate(path):
        print("\nStep", i)

        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])


# Input
start = tuple(
    map(int, input("Enter puzzle: ").split())
)

# Validate input
if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input!")
    print("Enter numbers 0 to 8 exactly once.")

else:
    path = dfs(start)
    print_solution(path)
