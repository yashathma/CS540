import heapq
import numpy
import copy

def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    # Define the target state and corresponding positions
    ans_puzzle = {to_state[0]: [0, 0], to_state[1]: [0, 1], to_state[2]: [0, 2],
                  to_state[3]: [1, 0], to_state[4]: [1, 1], to_state[5]: [1, 2], to_state[6]: [2, 0],
                  to_state[7]: [2, 1], to_state[8]: [2, 2]}

    total_dist = 0
    # Calculate Manhattan distance for each tile in the current state
    for i in range(len(from_state)):
        if from_state[i] != 0:
            point = ans_puzzle[from_state[i]]
            puzzle_loc = [int(i / 3), i % 3]
            total_dist += (abs(puzzle_loc[0] - point[0]) + abs(puzzle_loc[1] - point[1]))
    return total_dist

def print_succ(state):
    # Print successor states and their Manhattan distances
    succ_states = get_succ(state)
    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))

def get_succ(state):
    # Get successor states for the given state
    puzzle = numpy.reshape(state, (3, 3)).tolist()
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    empty_slots = list()
    result = []

    # Find empty slots in the puzzle
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                empty_slots.append([i, j])

    # Generate successor states by moving the empty slot
    for move in moves:
        for empty_slot in empty_slots:
            move_x = empty_slot[0] + move[0]
            move_y = empty_slot[1] + move[1]
            if 0 <= move_x <= 2 and 0 <= move_y <= 2:
                temp = copy.deepcopy(puzzle)
                curr = temp[empty_slot[0]][empty_slot[1]]
                temp[empty_slot[0]][empty_slot[1]] = temp[move_x][move_y]
                temp[move_x][move_y] = curr

                # Check if the move is valid and add to result
                if curr != temp[empty_slot[0]][empty_slot[1]]:
                    temp = numpy.array(temp).flatten().tolist()
                    result.append(temp)
    result = sorted(result)
    return result

def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    # A* algorithm to solve the puzzle
    pq = list()
    dist = get_manhattan_distance(state, goal_state)
    heapq.heappush(pq, (dist, state, (0, dist, -1)))
    visited = list()
    visited.append(state)
    checked = list()
    final_path = list()
    count = 0
    max_queue_length = len(pq)  # Initialize maxQueueLength before the while loop

    while len(pq) != 0:
        count += 1

        # Update maxQueueLength if needed
        if len(pq) > max_queue_length:
            max_queue_length = len(pq)

        # Extract the current state from the priority queue
        current = heapq.heappop(pq)
        checked.append(current)
        curr_state = current[1]

        # Check if the goal state is reached
        if get_manhattan_distance(curr_state, goal_state) == 0:
            temp = checked[len(checked) - 1]
            while temp[2][2] != -1:
                final_path.append(temp)
                temp = checked[temp[2][2]]

            final_path.append(temp)
            final_path.reverse()
            for choice in final_path:
                print(str(choice[1]) + " h=" + str(choice[2][1]) + " moves: " + str(choice[2][0]))
            print("Max queue length: " + str(max_queue_length))
            return final_path

        # Get successor states and update the priority queue
        neighbors = get_succ(curr_state)
        for neighbor in neighbors:
            check = []
            for to_check in checked:
                if neighbor == to_check[1]:
                    check.append(to_check)
            dist = get_manhattan_distance(neighbor, goal_state)
            moves = current[2][0] + 1
            if neighbor in visited or (len(check) != 0 and moves > check[0][2][0]):
                continue
            else:
                cost = moves + dist
                heapq.heappush(pq, (cost, neighbor, (moves, dist, checked.index(current))))
        visited.append(curr_state)

if __name__ == "__main__":
    solve([3, 4, 6, 0, 0, 1, 7, 2, 5])