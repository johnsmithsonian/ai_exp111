def minimax(node, depth, is_maximizing_player):
    if depth == 2:
        return node
    
    if is_maximizing_player:
        best_value = float('-inf')
        for child in node:
            value = minimax(child, depth + 1, False)
            best_value = max(best_value, value)
        return best_value
    
    else:
        best_value = float('inf')
        for child in node:
            value = minimax(child, depth + 1, True)
            best_value = min(best_value, value)
        return best_value

game_tree = [
    [3, 5], 
    [2, 9]
]

optimal_value = minimax(game_tree, 0, True)
print(f"The optimal move value for the maximizing player is: {optimal_value}")