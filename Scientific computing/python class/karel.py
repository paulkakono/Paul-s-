from stanfordkarel import *
print('Karel library imported successfully!')

def main():
    move()
    put_beeper()
    move()
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    move()
    put_beeper()
    turn_right()
    run()
    turn_right()
    finish()
    turn_around()
    run()
    turn_left()
    run()
    


    

def turn_right():
    for i in range(3):
        turn_left()

def run():
    move()
    move()
    move()

def finish():
    move()
    move()
    move()
    pick_beeper()

def turn_around():
    for i in range(2):
        turn_left



    


        
    

if __name__ == '__main__':
    run_karel_program()