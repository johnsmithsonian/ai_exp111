import heapq

class PuzzleState:
    def __init__(self, board, g=0):
        self.board = board
        self.g = g
        self.h = self.heuristic()
    
    def heuristic(self):
        return sum(abs((val - 1) // 3 - i) + abs((val - 1) % 3 - j)
                   for i in range(3) for j in range(3)
                   if (val := self.board[i * 3 + j]) != 0)

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def get_neighbors(state):
    neighbors = []
    zero_pos = state.board.index(0)
    x, y = divmod(zero_pos, 3)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_zero_pos = new_x * 3 + new_y
            new_board = state.board[:]
            new_board[zero_pos], new_board[new_zero_pos] = new_board[new_zero_pos], new_board[zero_pos]
            neighbors.append(PuzzleState(new_board, state.g + 1))

    return neighbors

def a_star(initial_board):
    initial_state = PuzzleState(initial_board)
    open_set = [initial_state]
    visited = {tuple(initial_board)}
    paths = {tuple(initial_board): None}  # To track the path

    while open_set:
        current_state = heapq.heappop(open_set)
        if current_state.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            return current_state, paths  # Return the solution and the path dictionary

        for neighbor in get_neighbors(current_state):
            board_tuple = tuple(neighbor.board)
            if board_tuple not in visited:
                visited.add(board_tuple)
                heapq.heappush(open_set, neighbor)
                paths[board_tuple] = current_state  # Store the parent state

    return None, paths  # Return None if no solution found

def print_board(board):
    for i in range(3):
        print(board[i * 3:(i + 1) * 3])
    print()

# Example usage
initial_board = [1, 2, 3, 8, 5, 0, 4, 7, 6]
solution, paths = a_star(initial_board)

if solution:
    # Reconstruct the path from the solution
    path = []
    current = solution
    while current:
        path.append(current.board)
        current = paths.get(tuple(current.board))

    for step in reversed(path):
        print_board(step)
else:
    print("No solution found.")
