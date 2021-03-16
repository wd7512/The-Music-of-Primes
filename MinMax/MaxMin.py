#define a function score which rates a state

def MaxMin(state,ismax):


    possible_moves = []
    scores = []

    game_is_over = False

    if game_is_over:
        return winner

    for move in possible_moves:
        new_state = 'state + move'
        scores.append(MaxMin(new_state,not ismax))

    if ismax == True:
        score = max(scores)
    else:
        score = min(scores)

    return score

