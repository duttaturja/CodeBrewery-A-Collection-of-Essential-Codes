
import math

def minmax(depth, node_index, is_maximizing, scores, height):
    if depth == height:
        return scores[node_index]
    if is_maximizing:
        return max(minmax(depth + 1, node_index * 2, False, scores, height),
                   minmax(depth + 1, node_index * 2 + 1, False, scores, height))
    else:
        return min(minmax(depth + 1, node_index * 2, True, scores, height),
                   minmax(depth + 1, node_index * 2 + 1, True, scores, height))

if __name__ == "__main__":
    scores = [3, 5, 6, 9, 1, 2, 0, -1]
    height = math.ceil(math.log2(len(scores)))
    print("Optimal value:", minmax(0, 0, True, scores, height))
