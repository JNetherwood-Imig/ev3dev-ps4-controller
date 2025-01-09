import utils

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
        if self.cb_type == CallbackType.ON_PRESS and \
                ev_type == utils.EventType.BUTTON and \
                self.code == ev_code:
            if ev_value == utils.ButtonEvent.PRESSED and not self.skip:
                self.callback()
                self.skip = True
            elif ev_value == utils.ButtonEvent.RELEASED:
                self.skip = False

        elif self.cb_type == CallbackType.ON_RELEASE and \
                ev_type == utils.EventType.BUTTON and \
                self.code == ev_code and \
                ev_value == utils.ButtonEvent.RELEASED:
            self.callback()

cb_list: list[ControllerCallback] = []

def register_on_press_callback(code: int, callback: function):
    cb_list.append(
            ControllerCallback(code, CallbackType.ON_PRESS, utils.EventType.BUTTON, callback))

def register_on_release_callback(code: int, callback: function):
    cb_list.append(
            ControllerCallback(code, CallbackType.ON_RELEASE, utils.EventType.BUTTON, callback))

