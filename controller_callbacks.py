from definitions import *

class CallbackType:
    ON_PRESS = 0
    ON_RELEASE = 1
    AXIS = 2

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
                self.callback(ev_value)
                self.skip = True
            elif ev_value == ButtonEvent.RELEASED:
                self.skip = False

        elif self.cb_type == CallbackType.ON_RELEASE and ev_type == EventType.BUTTON and self.code == ev_code and ev_value == ButtonEvent.RELEASED:
            self.callback(ev_value)

        elif self.cb_type == CallbackType.AXIS and ev_type == EventType.AXIS and self.code == ev_code:
            self.callback(ev_value)

controller_callbacks: list[ControllerCallback] = []

def register_axis_callback(code: int, callback: function):
    controller_callbacks.append(ControllerCallback(code, CallbackType.AXIS, EventType.AXIS, callback))

def register_on_press_callback(code: int, callback: function):
    controller_callbacks.append(ControllerCallback(code, CallbackType.ON_PRESS, EventType.BUTTON, callback))

def register_on_release_callback(code: int, callback: function):
    controller_callbacks.append(ControllerCallback(code, CallbackType.ON_RELEASE, EventType.BUTTON, callback))

