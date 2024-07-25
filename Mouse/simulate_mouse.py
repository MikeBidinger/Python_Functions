import pyautogui  # https://pyautogui.readthedocs.io/ - This module is not build-in with Python


def main():
    get_mouse_position()
    set_mouse(650, 400)
    move_mouse(300, 300, 1)
    afk_movement(100, 100, 5)


def get_mouse_position() -> tuple[int, int]:
    """Get the current mouse position coordinates.
    - Returns:
        - A tuple containing the current mouse position x- and y-coordinate.
    """
    # Print screen resolution
    SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
    print(
        f"Screen resolution:\n\tWidth :{SCREEN_WIDTH:>5}\n\tHeight:{SCREEN_HEIGHT:>5}"
    )
    # Wait for user input (Enter)
    input("Press enter to register the current mouse position (coordinates):")
    # Print the current mouse location coordinates
    current_mouse_x, current_mouse_y = pyautogui.position()
    print(f"\tX:{current_mouse_x:>5}\n\tY:{current_mouse_y:>5}")
    return (current_mouse_x, current_mouse_y)


def set_mouse(x: int, y: int, click: bool = False):
    """Set the mouse position to a given position.
    NOTE: The top-left corner of the screen represents the (0, 0) coordinates.
    - Args:
        - x: An integer representing the x-coordinate on the screen.
        - y: An integer representing the y-coordinate on the screen.
        - click: An optional boolean representing wether or not the mouse should be clicked on the given position.
    """
    # Set mouse position
    if click:
        pyautogui.click(x, y)
    else:
        pyautogui.moveTo(x, y)


def move_mouse(x: int, y: int, duration: float = 0, click: bool = False):
    """Move the mouse position relative to the current mouse position.
    NOTE: The top-left corner of the screen represents the (0, 0) coordinates.
    - Args:
        - x: An integer representing the x-coordinate on the screen.
        - y: An integer representing the y-coordinate on the screen.
        - duration: An optional float representing the duration of the mouse movement in seconds.
        - click: An optional boolean representing wether or not the mouse should be clicked on the given position.
    """
    # Move mouse relatively to the current position
    pyautogui.move(x, y, duration, pyautogui.easeInOutQuad)


def afk_movement(x: int, y: int, duration: int):
    """Move the mouse position from a starting point for the given duration.
    NOTE: The top-left corner of the screen represents the (0, 0) coordinates.
    - Args:
        - x: An integer representing the x-coordinate on the screen.
        - y: An integer representing the y-coordinate on the screen.
        - duration: An  float representing the duration of the mouse movement in seconds.
    """
    print("AFK script running...")
    # Set the starting mouse position
    set_mouse(x, y)
    # For the given duration:
    for i in range(duration):
        # Move the mouse by one pixel over one second
        move_mouse(1, 0, 1)
        print(f"{i + 1} / {duration} seconds")
    print("AFK script finished!")


if __name__ == "__main__":
    main()
