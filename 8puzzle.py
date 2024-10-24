import heapq

class PuzzleState:
    def __init__(self, board, empty_tile_pos, moves=0, previous=None):
        self.board = board
        self.empty_tile_pos = empty_tile_pos
        self.moves = moves
        self.previous = previous
        self.goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        self.size = 3

    def is_goal(self):
        return self.board == self.goal_state

    def get_neighbors(self):
        neighbors = []
        x, y = self.empty_tile_pos
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                new_board = list(self.board)
                new_board[x * self.size + y], new_board[new_x * self.size + new_y] = (
                    new_board[new_x * self.size + new_y],
                    new_board[x * self.size + y],
                )
                neighbors.append(PuzzleState(tuple(new_board), (new_x, new_y), self.moves + 1, self))

        return neighbors

    def heuristic(self):
        distance = 0
        for index, value in enumerate(self.board):
            if value != 0:
                target_x, target_y = divmod(value, self.size)
                current_x, current_y = divmod(index, self.size)
                distance += abs(target_x - current_x) + abs(target_y - current_y)
        return distance

    def f(self):
        return self.moves + self.heuristic()

    def __lt__(self, other):
        return self.f() < other.f()

def a_star(start_board):
    empty_tile_pos = start_board.index(0)
    start_state = PuzzleState(tuple(start_board), (empty_tile_pos // 3, empty_tile_pos % 3))

    open_set = []
    heapq.heappush(open_set, start_state)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            return current_state

        closed_set.add(current_state.board)

        for neighbor in current_state.get_neighbors():
            if neighbor.board in closed_set:
                continue
            heapq.heappush(open_set, neighbor)

    return None

def print_solution(solution):
    moves = []
    while solution:
        moves.append(solution.board)
        solution = solution.previous
    for board in reversed(moves):
        print(board)

if __name__ == "__main__":
    start_board = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    solution = a_star(start_board)
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution exists.")
