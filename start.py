import main as bot
from datetime import datetime as time
import pyautogui as cb

def main():
    while True:
        print("Waiting For Class....")

        today = time.now()
        current_time = today.strftime("%H:%M")

        if not current_time == "07:32":
            print("Starting Class At ", current_time)
            bot.start_class()



# NO EDIT __NAME__

if __name__ == '__main__':
    main()

# NO CODE PAST THIS POINT <-- -->