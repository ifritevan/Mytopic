課本數量 = 0

def on_forever():
    global 課本數量
    if input.acceleration(Dimension.X) == 0 or input.acceleration(Dimension.X) > 0:
        課本數量 += 1
basic.forever(on_forever)
