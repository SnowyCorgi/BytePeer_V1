def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_leds("""
            . # . . #
            # . # . .
            # # # . #
            # . # . .
            # . # . #
            """)
        music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        basic.clear_screen()
    else:
        basic.show_leds("""
            # # . . #
            # . # . .
            # # . . #
            # . # . .
            # # . . #
            """)
        music.play(music.tone_playable(392, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        basic.clear_screen()
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global Key1, codeDigit, Key2, Key3, Loaded, Key4
    basic.show_string("A")
    if codeDigit == 0:
        Key1 = 0
        codeDigit += 1
    elif codeDigit == 1:
        Key2 = 0
        codeDigit += 1
    elif codeDigit == 2:
        Key3 = 0
        codeDigit += 1
    elif codeDigit == 3:
        Loaded = 1
        codeDigit += 1
        Key4 = 0
        radio.set_transmit_power(7)
        radio.set_group(parse_float("" + str(Key1) + str(Key2) + str(Key3) + str(Key4)))
    else:
        radio.send_number(0)
    music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def Boot_Sequence():
    global Loaded, bootSequence, Key1, Key2, Key3, Key4, codeDigit
    Loaded = 0
    bootSequence = 0
    Key1 = 0
    Key2 = 0
    Key3 = 0
    Key4 = 1000
    music.set_volume(100)
    led.set_brightness(150)
    codeDigit = 0
    basic.show_leds("""
        . . # . .
        . # # # .
        # # . # #
        . # # # .
        . . # . .
        """)
    music.play(music.string_playable("C E E G C5 G E C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(1000)
    basic.clear_screen()
    bootSequence = 1
def SignalStrengthBar():
    if radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) > 2:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            """)
    elif radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) > 3:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . # . . .
            # # . . .
            """)
    elif radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) > 4:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . # # . .
            # # # . .
            """)
    elif radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) > 5:
        basic.show_leds("""
            . . . . .
            . . . # .
            . . # # .
            . # # # .
            # # # # .
            """)
    elif radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) > 6:
        basic.show_leds("""
            . . . . #
            . . . # #
            . . # # #
            . # # # #
            # # # # #
            """)
    else:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)

def on_button_pressed_ab():
    SignalStrengthBar()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Key1, codeDigit, Key2, Key3, Loaded, Key4
    basic.show_string("B")
    if codeDigit == 0:
        Key1 = 1
        codeDigit += 1
    elif codeDigit == 1:
        Key2 = 1
        codeDigit += 1
    elif codeDigit == 2:
        Key3 = 1
        codeDigit += 1
    elif codeDigit == 3:
        Loaded = 1
        codeDigit += 1
        Key4 = 1
        radio.set_transmit_power(7)
        radio.set_group(parse_float("" + str(Key1) + str(Key2) + str(Key3) + str(Key4)))
    else:
        radio.send_number(1)
    music.play(music.tone_playable(392, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

bootSequence = 0
Key4 = 0
Loaded = 0
Key3 = 0
Key2 = 0
Key1 = 0
codeDigit = 0
Boot_Sequence()

def on_forever():
    if bootSequence == 1:
        if codeDigit == 0:
            basic.show_number(1)
        elif codeDigit == 1:
            basic.show_number(2)
        elif codeDigit == 2:
            basic.show_number(3)
        elif codeDigit == 3:
            basic.show_number(4)
            if Loaded == 1:
                basic.clear_screen()
basic.forever(on_forever)

def on_forever2():
    if Loaded == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(750)
        basic.show_leds("""
            . . . . .
            . . . . .
            # . # . .
            . . . . .
            . . . . .
            """)
        basic.pause(750)
        basic.show_leds("""
            . . . . .
            . . . . .
            # . # . #
            . . . . .
            . . . . .
            """)
        basic.pause(750)
basic.forever(on_forever2)
