class Node:
    def __init__(self, state, g, h):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def h(state):
    return sum(1 for i in range(len(state)) for j in range(i + 1, len(state))
               if state[i] == state[j] or abs(state[i] - state[j]) == j - i)

def a_star_8_queens():
    initial_state = [-1] * 8
    open_set = [Node(initial_state, 0, h(initial_state))]
    closed_set = set()

    while open_set:
        current = open_set.pop(0)
        if len(current.state) == 8 and all(s != -1 for s in current.state):
            return current.state

        closed_set.add(tuple(current.state))

        for col in range(8):
            for row in range(8):
                if current.state[row] == -1:
                    new_state = current.state[:]
                    new_state[row] = col
                    if tuple(new_state) not in closed_set:
                        new_g = current.g + 1
                        new_h = h(new_state)
                        open_set.append(Node(new_state, new_g, new_h))
                        open_set.sort()

result = a_star_8_queens()
print(result)
