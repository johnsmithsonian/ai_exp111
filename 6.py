leaf_values = [3, 5, 2, 9]

def minimax(is_maximizing):
    if is_maximizing:
        return max(leaf_values)
    else:
        return min(leaf_values)

def best_move():
    return minimax(True)

best_value = best_move()
print(f"Best move value for maximizing player: {best_value}")
