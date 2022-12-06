#DICE PYTHON PROGRAM
# Python code
#
number2 = 0

def on_gesture_shake():
  global number2
  basic.clear_screen()
  number2 = randint(1, 6)
  if number2 == 1:
    basic.show_leds("""
      . . . . .
      . . . . .
      . . # . .
      . . . . .
      . . . . .
      """)
  else:
    if number2 == 2:
      basic.show_leds("""
        . . . . .
        . # . . .
        . . . . .
        . . . # .
        . . . . .
        """)
    else:
      if number2 == 3:
        basic.show_leds("""
          . . . . .
          . # . . .
          . . # . .
          . . . # .
          . . . . .
          """)
      else:
        if number2 == 4:
          basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """)
        else:
          if number2 == 5:
            basic.show_leds("""
              . . . . .
              . # . # .
              . . # . .
              . # . # .
              . . . . .
              """)
          else:
            basic.show_leds("""
              . . . . .
              . # . # .
              . # . # .
              . # . # .
              . . . . .
              """)
input.on_gesture(Gesture.Shake, on_gesture_shake)
