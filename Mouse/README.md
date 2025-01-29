# Python Functions - [simulate_mouse.py](simulate_mouse.py)

Standardized functions to save up repetitive work and keep code clean within Python scripting.
These all have basic formats and uses, but they can be customized relatively easily to achieve tailored functionalities.

> [!NOTE]
> These functions uses the module [pyautogui](https://pyautogui.readthedocs.io/).
> This module is not build-in with Python.

> [!TIP]
> The top-left corner of the screen represents the (0, 0) coordinates.

## Content

-   [get_mouse_position()](#get_mouse_position)
-   [set_mouse()](#set_mouse)
-   [move_mouse()](#move_mouse)
-   [afk_movement()](#afk_movement)
-   [example_function()](#example_function)

## Functions

### get_mouse_position()

Get the current mouse position coordinates.

-   Args:

    -   user_confirm (bool, optional): A boolean representing wether or not the user should confirm to return the current mouse position coordinates. Defaults to False.

-   Returns:

    -   tuple[float, float]: A tuple containing the current mouse position x- and y-coordinate.

```python
def get_mouse_position(user_confirm: bool = False) -> tuple[float, float]:
    if user_confirm:
        # Print screen resolution
        SCREEN_WIDTH: int = 0
        SCREEN_HEIGHT: int = 0
        SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
        print(
            f"Screen resolution:\n\tWidth :{SCREEN_WIDTH:>5}\n\tHeight:{SCREEN_HEIGHT:>5}"
        )
        # Wait for user input (Enter)
        input("Press enter to register the current mouse position (coordinates):")
    # Print the current mouse location coordinates
    current_mouse_x: float = 0
    current_mouse_y: float = 0
    current_mouse_x, current_mouse_y = pyautogui.position()
    if user_confirm:
        print(f"\tX:{current_mouse_x:>5}\n\tY:{current_mouse_y:>5}")
    return (current_mouse_x, current_mouse_y)
```

### set_mouse()

Set the mouse position to a given position.

-   Args:

    -   x (int): An integer representing the x-coordinate on the screen.
    -   y (int): An integer representing the y-coordinate on the screen.
    -   click (bool, optional): A boolean representing wether or not the mouse should be clicked on the given position. Defaults to False.


```python
def set_mouse(x: int, y: int, click: bool = False) -> None:
    # Set mouse position
    if click:
        pyautogui.click(x, y)
    else:
        pyautogui.moveTo(x, y)
```

### move_mouse()

Move the mouse position relative to the current mouse position.

-   Args:

    -   x (int): An integer representing the x-coordinate to be moved on the screen.
    -   y (int): An integer representing the y-coordinate to be moved on the screen.
    -   duration (float, optional): A float representing the duration of the mouse movement in seconds. Defaults to 0.
    -   click (bool, optional): A boolean representing wether or not the mouse should be clicked on the given position. Defaults to False.

-   Returns:

    -   tuple[float, float]: A tuple containing the current mouse position x- and y-coordinate.

```python
def move_mouse(
    # Move mouse relatively to the current position
    pyautogui.move(x, y, duration, pyautogui.easeInOutQuad)
    return get_mouse_position()
```

### afk_movement()

Move the mouse position from a starting point for the given duration.

-   Args:

    -   x (int): An integer representing the x-coordinate on the screen.
    -   y (int): An integer representing the y-coordinate on the screen.
    -   duration (int): A float representing the duration of the mouse movement in seconds.


```python
def afk_movement(x: int, y: int, duration: int) -> None:
    print("AFK script running...")
    # Set the starting mouse position
    set_mouse(x, y)
    mouse_pos: tuple[float, float] = get_mouse_position()
    # For the given duration:
    for i in range(duration):
        if get_mouse_position() != mouse_pos:
            break
        # Move the mouse by one pixel over one second
        mouse_pos = move_mouse(1, 0)
        print(f"{i + 1} / {duration} seconds")
        time.sleep(1)
    else:
        print("AFK script finished!")
        return
    print("AFK script stopped!")
```

### example_function()

Example of use: Get, set and move mouse position.

```python
def example_function() -> None:
    get_mouse_position(True)
    set_mouse(650, 400)
    move_mouse(300, 300, 1)
    afk_movement(100, 100, (15 * 60))
```
