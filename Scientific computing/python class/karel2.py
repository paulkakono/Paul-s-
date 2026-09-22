from stanfordkarel import *
print('Karel library imported successfully!')

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def collect_up():
    while beepers_present():
        pick_beeper()
    while front_is_clear():
        move()
        while beepers_present():
            pick_beeper()
    # go back to ground
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def main():
    # make sure facing north
    while not_facing_north():
        turn_left()

    # collect column where we are (if any)
    collect_up()

    # face west and walk to (1,1)
    turn_left()

    while front_is_clear():
        move()
        # if we hit a column with beepers, collect it
        if beepers_present():
            turn_right()
            collect_up()
            turn_left()

    # now at (1,1) facing west, turn east
    turn_around()

    # drop everything
    while beepers_in_bag():
        put_beeper()




  



if __name__ == '__main__':
     run_karel_program('stone_mason_karel_end')