# pip install pyobjc pyautogui
# pip install pyobjc pyautogui

from time import sleep
import pyautogui
from AppKit import NSWorkspace
import os


class MetaOne(type):
    def __new__(cls, name, bases, dict):
        pass


class StatusMonitor:
    current_status = "unknown"
    last_fg_app = "unknown"
    last_mouse_pos = (None, None)
    SLEEP_DURATION = 1  # sec
    last_status = "unknown"

    def discord_is_still_fg(self):
        current_fg_app = get_foreground_app_name()
        same = self.last_fg_app == current_fg_app
        self.last_fg_app = current_fg_app
        is_discord = match_discord_name(current_fg_app)
        return same and is_discord

    def mouse_has_moved(self):
        x, y = pyautogui.position()
        moved = self.last_mouse_pos == (x, y)
        self.last_mouse_pos = (x, y)
        if moved:
            return False
        else:
            return True

    def set_status(self, new_status):
        if new_status != self.last_status:
            if new_status == "idle":
                print("set idle")
            elif new_status == "invisible":
                print("set invisible")

            self.last_status = new_status

    def discord_is_still_opened(self):
        return True

    def run(self):
        while True:
            if self.discord_is_still_fg():
                if self.mouse_has_moved():
                    self.set_status("idle")
                else:
                    self.set_status("invisible")
            else:
                if self.discord_is_still_opened():
                    self.set_status("invisible")
                else:
                    print("discord closed")

            sleep(self.SLEEP_DURATION)


def is_macOS():
    return os.name == "posix"


def is_Win():
    return os.name == "nt"


def get_foreground_app_name():
    # print(os.name)
    if is_macOS():
        return NSWorkspace.sharedWorkspace().activeApplication()["NSApplicationName"]
    elif is_Win():
        return "windows"


def match_discord_name(app_name):
    if is_macOS():
        return app_name == "Google Chrome"


if __name__ == "__main__":
    moni = StatusMonitor()
    moni.run()
