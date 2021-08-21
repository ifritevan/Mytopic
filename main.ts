let 課本數量 = 0
basic.forever(function () {
    if (input.acceleration(Dimension.X) == 0 || input.acceleration(Dimension.X) > 0) {
        課本數量 += 1
    }
})
