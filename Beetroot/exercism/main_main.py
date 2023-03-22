def eat_ghost(power_pellet_active, touching_ghost):
    if (power_pellet_active is True) and (touching_ghost is True):
        return True
    else:
        return False

def score(touching_power_pellet, touching_dot):
    if (touching_power_pellet is True) or (touching_dot is True):
        return True
    else:
        return False
def lose(power_pellet_active, touching_ghost):
    if (power_pellet_active is False) and (touching_ghost is True):
        return True
    else:
        return False
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):

    if (has_eaten_all_dots is True) and (power_pellet_active is True) and (touching_ghost is True):
        return True
    elif (has_eaten_all_dots is True) and (power_pellet_active is False) and (touching_ghost is True):
        return False
    elif (has_eaten_all_dots is True) and (touching_ghost is False):
        return True
    else:
        return False