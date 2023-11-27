def checkWin(envi):
    for i in range(3):
        if envi[i][0] == envi[i][1] and envi[i][0] == envi[i][2] and envi[i][0] != 0:
            return f"Player {envi[i][0]} won"
        if envi[0][i] == envi[1][i] and envi[0][i] == envi[2][i] and envi[0][i] != 0:
            return f"Player {envi[0][i]} won"
    if envi[0][0] == envi[1][1] and envi[0][0] == envi[2][2] and envi[0][0] != 0:
        return f"Player {envi[0][0]} won"
    if envi[0][2] == envi[1][1] and envi[0][2] == envi[2][0] and envi[0][2] != 0:
        return f"Player {envi[0][2]} won"
    return False
    