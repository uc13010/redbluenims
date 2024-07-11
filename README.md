-red_blue_nim.py is a program to play both standard and misere versions of Red-Blue Nim where players take turns removing marbles from two piles. If either pile is empty on a player's turn, they lose (standard) or win (misére) with the total points depending on the remaining marbles (2 points per red, 3 points per blue).
-Action to be taken by computer at each step is calculated using min-max algorithm with alpha beta pruning that include move ordering to first pick a blue marble for the standard version and to first pick a red marble for the misere version. 
-The program receives human input at each step, which consists of either 'red' or 'blue' to indicate the chosen marble pile during the human's turn.

Depth limited search explanation:
Depth limited search has been implemented in the program. The eval function calculates points at maximum depth which implies-
At the maximum depth:
1. The code first checks if the current depth equals the maximum depth specified for the minimax search. If it does, it means the algorithm has reached a leaf node in the game tree and needs to evaluate this node.
2. At a depth of 0, which is the root node of the search, the program determines which color pile (red or blue) has more marbles. It then removes one marble from the larger pile. After adjusting the piles, it calculates the total points by multiplying the number of red marbles by 2 and the number of blue marbles by 3. This represents the score that would be obtained if the game ends at this point.
3. For non-root nodes at the maximum depth, the code checks whether red marbles (multiplied by 2) dominate blue marbles (multiplied by 3) in terms of points. If red dominates, it assigns 2 points if it's a max_node (maximizing player's turn) and -2 points if it's a min_node (minimizing player's turn). If blue dominates, it assigns -2 points for a max_node and 2 points for a min_node. This reflects the advantage or disadvantage of the current position.
4. In both cases (root and non-root), the function returns the node with its points updated based on the evaluation at the maximum depth. The points represent the potential outcome of the game from that node, which will be used by the minimax algorithm to make decisions during the search.

Instructions to execute:
1. Install python in the system
2. Open Terminal/command line prompt 
3. Navigate to the folder that contains the code file and execute the following code 
    - Command: python3 (or python) red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>
    - Example: python3 red_blue_nim.py 3 5 standard computer 2
    - <num-red> <num-blue>: Integer input, default version: standard, default first player: computer, default depth: 10
