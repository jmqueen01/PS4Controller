import pygame

TRIGGER_THRESHOLD = 0.5


def main():
    pygame.init()

    # Initialize the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Print the name of the joystick
    print("Joystick Name:", joystick.get_name())

    button_pressed = [False] * joystick.get_numbuttons()
    axis_moved = [False] * joystick.get_numaxes()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                button_pressed[event.button] = True
                button_name = get_ps4_button_name(event.button)
                if button_name == "D-Up":
                    print("Button", button_name, "Moving Forwards")
                if button_name == "D-Left":
                    print("Button", button_name, "Moving Left")
                if button_name == "D-Down":
                    print("Button", button_name, "Moving Backwards")
                if button_name == "D-Right":
                    print("Button", button_name, "Moving Right")
                if button_name == "L1":
                    print("Button", button_name, "Spinning Up")
                if button_name == "R1":
                    print("Button", button_name, "Canon Firing!!")
                if button_name == "Cross":
                    print("Button", button_name, "Canon Pitch Down")
                if button_name == "Triangle":
                    print("Button", button_name, "Canon Pitch Up")
                if button_name == "Circle":
                    print("Button", button_name, "Canon Yaw Right ")
                if button_name == "Square":
                    print("Button", button_name, "Canon Yaw Left")
            elif event.type == pygame.JOYBUTTONUP:
                button_pressed[event.button] = False
                button_name = get_ps4_button_name(event.button)
                if button_name:
                    print("Button", button_name, "released")
            elif event.type == pygame.JOYAXISMOTION:
                if not axis_moved[event.axis]:
                    axis_moved[event.axis] = True
                    axis_name, direction = get_ps4_axis_info(event.axis, event.value)
                    if axis_name and direction:
                        print("Axis", axis_name, "moved", direction)
            elif event.type == pygame.JOYAXISMOTION:
                if axis_moved[event.axis]:
                    axis_moved[event.axis] = False
                    gamepad.read_event()
        # Check for quit event
        if pygame.event.peek(pygame.QUIT):
            running = False


pygame.quit()


def get_ps4_button_name(button_index):
    ps4_button_map = {
        0: "Cross",
        1: "Circle",
        2: "Square",
        3: "Triangle",
        4: "Share",
        5: "PS",
        6: "Options",
        7: "L3",
        8: "R3",
        9: "L1",
        10: "R1",
        11: "D-Up",
        12: "D-Down",
        13: "D-Left",
        14: "D-Right",
        15: "Touchpad",
    }
    return ps4_button_map.get(button_index)


def get_ps4_axis_info(axis_index, axis_value):
    ps4_axis_map = {
        0: ("Left Stick X", "left"),
        1: ("Left Stick Y", "up"),
        2: ("Right Stick X", "left"),
        3: ("Right Stick Y", "up"),
        4: ("L2", "pressed" if axis_value > 0.5 else "released"),
        5: ("R2", "pressed" if axis_value > 0.5 else "released"),
    }

    axis_name, direction = ps4_axis_map.get(axis_index, (None, None))

    return axis_name, direction


if __name__ == "__main__":
    main()
