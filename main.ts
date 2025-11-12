radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        basic.showLeds(`
            . # . . #
            # . # . .
            # # # . #
            # . # . .
            # . # . #
            `)
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        basic.clearScreen()
    } else {
        basic.showLeds(`
            # # . . #
            # . # . .
            # # . . #
            # . # . .
            # # . . #
            `)
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.A, function () {
    basic.showString("A")
    if (codeDigit == 0) {
        Key1 = 0
        codeDigit += 1
    } else if (codeDigit == 1) {
        Key2 = 0
        codeDigit += 1
    } else if (codeDigit == 2) {
        Key3 = 0
        codeDigit += 1
    } else if (codeDigit == 3) {
        Loaded = 1
        codeDigit += 1
        Key4 = 0
        radio.setTransmitPower(7)
        radio.setGroup(parseFloat("" + Key1 + Key2 + Key3 + Key4))
    } else {
        radio.sendNumber(0)
    }
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    basic.clearScreen()
})
function Boot_Sequence () {
    Loaded = 0
    bootSequence = 0
    Key1 = 0
    Key2 = 0
    Key3 = 0
    Key4 = 1000
    music.setVolume(100)
    led.setBrightness(150)
    codeDigit = 0
    basic.showLeds(`
        . . # . .
        . # # # .
        # # . # #
        . # # # .
        . . # . .
        `)
    music.play(music.stringPlayable("C E E G C5 G E C ", 120), music.PlaybackMode.UntilDone)
    basic.pause(1000)
    basic.clearScreen()
    bootSequence = 1
}
function SignalStrengthBar () {
    if (radio.receivedPacket(RadioPacketProperty.SignalStrength) > 2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            `)
    } else if (radio.receivedPacket(RadioPacketProperty.SignalStrength) > 3) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # . . .
            # # . . .
            `)
    } else if (radio.receivedPacket(RadioPacketProperty.SignalStrength) > 4) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . # # . .
            # # # . .
            `)
    } else if (radio.receivedPacket(RadioPacketProperty.SignalStrength) > 5) {
        basic.showLeds(`
            . . . . .
            . . . # .
            . . # # .
            . # # # .
            # # # # .
            `)
    } else if (radio.receivedPacket(RadioPacketProperty.SignalStrength) > 6) {
        basic.showLeds(`
            . . . . #
            . . . # #
            . . # # #
            . # # # #
            # # # # #
            `)
    } else {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
}
input.onButtonPressed(Button.AB, function () {
    SignalStrengthBar()
})
input.onButtonPressed(Button.B, function () {
    basic.showString("B")
    if (codeDigit == 0) {
        Key1 = 1
        codeDigit += 1
    } else if (codeDigit == 1) {
        Key2 = 1
        codeDigit += 1
    } else if (codeDigit == 2) {
        Key3 = 1
        codeDigit += 1
    } else if (codeDigit == 3) {
        Loaded = 1
        codeDigit += 1
        Key4 = 1
        radio.setTransmitPower(7)
        radio.setGroup(parseFloat("" + Key1 + Key2 + Key3 + Key4))
    } else {
        radio.sendNumber(1)
    }
    music.play(music.tonePlayable(392, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    basic.clearScreen()
})
let bootSequence = 0
let Key4 = 0
let Loaded = 0
let Key3 = 0
let Key2 = 0
let Key1 = 0
let codeDigit = 0
Boot_Sequence()
basic.forever(function () {
    if (bootSequence == 1) {
        if (codeDigit == 0) {
            basic.showNumber(1)
        } else if (codeDigit == 1) {
            basic.showNumber(2)
        } else if (codeDigit == 2) {
            basic.showNumber(3)
        } else if (codeDigit == 3) {
            basic.showNumber(4)
            if (Loaded == 1) {
                basic.clearScreen()
            }
        }
    }
})
basic.forever(function () {
    if (Loaded == 1) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(750)
        basic.showLeds(`
            . . . . .
            . . . . .
            # . # . .
            . . . . .
            . . . . .
            `)
        basic.pause(750)
        basic.showLeds(`
            . . . . .
            . . . . .
            # . # . #
            . . . . .
            . . . . .
            `)
        basic.pause(750)
    }
})
