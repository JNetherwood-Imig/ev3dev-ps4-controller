from definitions import *

class CallbackType:
    ON_PRESS = 0
    ON_RELEASE = 1

class ControllerCallback:
    code: int
    cb_type: int
    ev_type: int
    skip: bool
    callback: function

    def __init__(self, code: int, cb_type: int, ev_type: int, callback: function) -> None:
        self.code = code
        self.cb_type = cb_type
        self.ev_type = ev_type
        self.skip = False
        self.callback = callback

    def try_run(self, ev_type: int, ev_code: int, ev_value: int) -> None:
        if self.cb_type == CallbackType.ON_PRESS and ev_type == EventType.BUTTON and self.code == ev_code:
            if ev_value == ButtonEvent.PRESSED and not self.skip:
                self.callback()
                self.skip = True
            elif ev_value == ButtonEvent.RELEASED:
                self.skip = False

        elif self.cb_type == CallbackType.ON_RELEASE and ev_type == EventType.BUTTON and self.code == ev_code and ev_value == ButtonEvent.RELEASED:
            self.callback()

controller_callbacks: list[ControllerCallback] = []

def register_on_press_callback(code: int, callback: function):
    controller_callbacks.append(ControllerCallback(code, CallbackType.ON_PRESS, EventType.BUTTON, callback))

def register_on_release_callback(code: int, callback: function):
    controller_callbacks.append(ControllerCallback(code, CallbackType.ON_RELEASE, EventType.BUTTON, callback))

