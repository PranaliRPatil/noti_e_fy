# Display water break notification
# Break Notifications

import time
from win10toast import ToastNotifier

def send_notify(title: str, msg: str, interval: int, sleep_interval: float, icon=None) -> None:
    """Popups Notifications for you"""
    time.sleep(60 * sleep_interval)
    toaster = ToastNotifier()
    toaster.show_toast(title, msg, icon, interval)


while True:
    notify
    send_notify("Hey hii!!!",
                "Lets have some break", 10, 20)
    send_notify("Hello Buddy!!!",
                "Lets have some 🥤 break", 10, 30, r"C:\Users\admin\Desktop\VS_python\noti_e_fy\glass1.ico")
    time.sleep(3600)
