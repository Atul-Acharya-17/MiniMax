
class MiniMax:

    pos_inf = float('inf')
    neg_inf = float('-inf')

    def solve(self, state, max_depth, is_maximizing, heuristic, is_terminal, get_next_states):

        if max_depth == 0 or is_terminal(state):
            return state, heuristic(state)

        else:
            next_states = get_next_states(state, is_maximizing)
    
            if is_maximizing:

                best_value = self.neg_inf
                best_state = None

                for child in next_states:
                    _, value = self.solve(child, max_depth-1, False, heuristic, is_terminal, get_next_states)

                    if value > best_value:
                        best_value = value
                        best_state = child
                
                return best_state, best_value
            
            else:

                best_value = self.pos_inf
                best_state = None

                for child in next_states:
                    _, value = self.solve(child, max_depth-1, True, heuristic, is_terminal, get_next_states)

                    if value < best_value:
                        best_value = value
                        best_state = child
                
                return best_state, best_value            
                