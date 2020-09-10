# Display water break notification
# Alert for battery status
# birthday reminders for close people

import time
from win10toast import ToastNotifier

# toaster = ToastNotifier()
# toaster.show_toast("Hello Buddy!!!",
#                    "Lets have some 🥤 break",
#                    r"C:\Users\admin\Desktop\VS_python\noti_e_fy\glass1.ico",
#                    10)


def send_notify(title, msg, icon, interval):
    toaster = ToastNotifier()
    toaster.show_toast(title, msg, icon, interval)


while True:
    # send_notify()
    toaster = ToastNotifier()
    toaster.show_toast("Hello Buddy!!!",
                       "Lets have some 🥤 break",
                       r"C:\Users\admin\Desktop\VS_python\noti_e_fy\glass1.ico",
                       10)
    time.sleep(3600)
