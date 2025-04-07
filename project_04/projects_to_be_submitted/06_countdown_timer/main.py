import time
import sys

def countdown(t):
    print("\n🚀 Get Ready! The Countdown Begins! 🚀\n")
    
    while t:
        mins, secs = divmod(t, 60)
        timer = f"⏳ Time Remaining: {mins:02d}:{secs:02d}"
        sys.stdout.write(f"\r{timer}")
        sys.stdout.flush()
        time.sleep(1)
        t -= 1
    
    print("\n🎊 BOOM! Time's Up! 🎊\n")
    print("💡 Did you complete your task on time? Keep challenging yourself! 💡")

try:
    t = int(input("⏱️ Enter countdown time in seconds: "))
    if t > 0:
        countdown(t)
    else:
        print("⚠️ Please enter a positive number!")
except ValueError:
    print("❌ Invalid input! Please enter a valid number.")

