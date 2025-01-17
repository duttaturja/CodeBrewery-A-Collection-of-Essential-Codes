
import math

def alpha_beta_pruning(depth, node_index, is_maximizing, scores, alpha, beta, height):
    if depth == height:
        return scores[node_index]
    if is_maximizing:
        max_eval = -math.inf
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, scores, alpha, beta, height)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, scores, alpha, beta, height)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

if __name__ == "__main__":
    scores = [3, 5, 6, 9, 1, 2, 0, -1]
    height = math.ceil(math.log2(len(scores)))
    print("Optimal value:", alpha_beta_pruning(0, 0, True, scores, -math.inf, math.inf, height))
