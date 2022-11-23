def srec8():
    if rec8 == 0:
        rec8 = 1
        btn_pressed = 1
        record()
    elif rec8 == 1:
        rec8 = 2
        btn_pressed = 1
        play()
    elif rec8 == 2:
        rec8 = 3
        btn_pressed = 1
        stop()
    print("Button 2 was pressed")

