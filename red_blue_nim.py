
import sys

class red_blue_nim:
    def __init__(self, prev_node, num_of_red, num_of_blue, version, points, misere_version_true):
        self.prev_node = prev_node
        self.num_of_red = num_of_red
        self.num_of_blue = num_of_blue
        self.version=version
        self.points = points
        self.misere_version_true = misere_version_true

def select_action(node, score):

    if node.misere_version_true:
        succ_left = red_blue_nim(node, node.num_of_red-1, node.num_of_blue, node.version, score, node.misere_version_true)
        succ_right = red_blue_nim(node, node.num_of_red, node.num_of_blue-1, node.version, score, node.misere_version_true)
    else:
        succ_left = red_blue_nim(node, node.num_of_red, node.num_of_blue-1, node.version, score, node.misere_version_true)
        succ_right = red_blue_nim(node, node.num_of_red-1, node.num_of_blue, node.version, score, node.misere_version_true)
   
    return succ_left, succ_right

def pruned_minimax(node, depth, max_node, alpha, beta, max_depth):
    for color in ["red", "blue"]:
        if(node.num_of_red == 0 or node.num_of_blue == 0):
            if color == "red" and node.num_of_red == 0:
                node.points = (node.num_of_blue * 3) * (-1 if not max_node else 1)
            elif color == "blue" and node.num_of_blue == 0:
                node.points = (node.num_of_red * 2) * (-1 if not max_node else 1)
            return node
        
    if depth == max_depth:
        if depth == 0:
            if node.num_of_red >= node.num_of_blue:
                node.num_of_red -= 1
            else:
                node.num_of_blue -= 1
            node.points = node.num_of_red * 2 + node.num_of_blue * 3
            return node

        if node.num_of_red * 2 >= node.num_of_blue * 3:
            node.points = 2 if max_node else -2
        else:
            node.points = -2 if max_node else 2

        return node

    optimal_node = None
    if max_node:
        highest_score = float('-inf')
        succ_left, succ_right = select_action(node, 0)
        left = pruned_minimax(succ_left, depth + 1, False, alpha, beta, max_depth)
                
        highest_score = max(left.points, highest_score)
        alpha = max(alpha, highest_score)

        if left.points == highest_score:
            optimal_node = left
        if highest_score >= beta:
            return optimal_node
        

        right = pruned_minimax(succ_right, depth + 1, False, alpha, beta, max_depth)
        highest_score = max(right.points, highest_score)
        alpha = max(alpha, highest_score)

        if right.points == highest_score and right.points != left.points:
            optimal_node = right
        if highest_score >= beta:
            return optimal_node

    else:
        least_score = float('inf')
        succ_left, succ_right= select_action(node, 0)

        left = pruned_minimax(succ_left, depth + 1, True, alpha, beta, max_depth)
        least_score = min(left.points, least_score)
        beta = min(beta, least_score)

        if left.points == least_score:
            optimal_node = left
        if alpha >= least_score:
            return optimal_node

        right = pruned_minimax(succ_right, depth + 1, True, alpha, beta, max_depth)
        least_score = min(right.points, least_score)
        beta = min(beta, least_score)

        if right.points == least_score and right.points != left.points:
            optimal_node = right

        if alpha >= least_score:
            return optimal_node

    return optimal_node

def get_next_node(succ_mmn, init_node):
    for node in iter(lambda: succ_mmn.prev_node, None):
        if node == init_node or node.prev_node is None:
            return succ_mmn
        succ_mmn = node
    return succ_mmn

def take_turns(num_of_red, num_of_blue, version, first_player, depth):
    while num_of_red != 0 and num_of_blue != 0:
        print(f"Red: {num_of_red}, Blue: {num_of_blue}")

        if first_player == "computer":
            init_node = red_blue_nim(None, num_of_red, num_of_blue, version, 0, version.lower() == "misere")
            alpha, beta = float('-inf'), float('inf')

            succ_mmn = pruned_minimax(init_node, 0, True, alpha, beta, depth)
            next_node = get_next_node(succ_mmn, init_node)

            move_color = "red" if next_node.num_of_blue == num_of_blue else "blue"
            print(f"Computer moved {move_color}")
            if move_color == "red":
                num_of_red -= 1 
            else:
                num_of_blue -= 1

        else:
            block = input("Enter red to choose red ball or blue to choose blue ball: ")
            if block.lower() == "red": num_of_red -= 1
            elif block.lower() == "blue": num_of_blue -= 1
            else: print("Wrong input!")

        first_player = "human" if first_player == "computer" else "computer"

    return first_player, num_of_red, num_of_blue


def print_usage_and_exit():
    print("Correct format: python3 red_blue_nim.py <red_balls> <blue_balls> <version:stanadrad/misere> <first-player:computer/human> <depth>")
    sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print_usage_and_exit()
    
    red_balls, blue_balls = [int(arg) for arg in sys.argv[1:3]]
    version = "standard" if len(sys.argv) <= 3 else sys.argv[3] #default is standard
    first_player = "computer" if len(sys.argv) <= 4 else sys.argv[4] #default is computer
    depth = int(sys.argv[5]) if len(sys.argv) > 5 else 10 #default is 10
    print(f"Input: <red balls:{red_balls}> <blue balls:{blue_balls}> <version:{version}> <first-player:{first_player}> <depth:{depth}>")
    
    curr_player, red_left, blue_left = take_turns(red_balls, blue_balls, version, first_player, depth)

    print(f"(red balls:{red_left}, blue balls:{blue_left})")

    points = red_left * 2 + blue_left * 3
    standard_version = version.lower() != "misere"
    winner = "Human" if standard_version == (curr_player.lower() == "computer") else "Computer"
    print(f"Winner:{winner}, Points:{points}")

if __name__ == "__main__":
    main()
