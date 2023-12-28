import time
import pygame

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            play_alarm()
            break
        time.sleep(1)

def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")  
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    print("Welcome to the Alarm Clock App!")
    alarm_time = input("Set the alarm time (HH:MM:SS): ")

    try:
        time.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
        return

    print(f"Alarm set for {alarm_time}")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
