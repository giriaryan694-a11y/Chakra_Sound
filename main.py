import numpy as np
import sounddevice as sd
import os
from scipy.io.wavfile import write
from pyfiglet import Figlet
from termcolor import colored
from colorama import init, Fore, Style

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Chakra frequencies (Hz)
CHAKRAS = {
    1: ("Root", 194.18, "red"),
    2: ("Sacral", 210.42, "yellow"),
    3: ("Solar Plexus", 126.22, "green"),
    4: ("Heart", 136.10, "cyan"),
    5: ("Throat", 141.27, "blue"),
    6: ("Third Eye", 221.23, "magenta"),
    7: ("Crown", 172.06, "white")
}

SAMPLE_RATE = 44100
os.makedirs("chakra_tones", exist_ok=True)

# ========== Utility Functions ==========

def banner():
    fig = Figlet(font="slant")
    print(colored(fig.renderText("Chakra Sound"), "cyan"))
    print(colored("Developed by Aryan Giri 🧘‍♂️ — Vibrate Higher ⚡", "yellow"))
    print(colored("=" * 60, "cyan"))

def generate_tone(frequency, duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    tone = np.sin(2 * np.pi * frequency * t)
    return (tone * 0.3).astype(np.float32)  # lower volume

def play_tone(frequency, duration):
    audio = generate_tone(frequency, duration)
    sd.play(audio, SAMPLE_RATE)
    sd.wait()

def save_tone(name, frequency, duration):
    audio = generate_tone(frequency, duration)
    path = f"chakra_tones/{name}_{frequency:.2f}Hz_{duration}s.wav"
    write(path, SAMPLE_RATE, (audio * 32767).astype(np.int16))
    print(colored(f"✅ Saved: {path}", "green"))

def chakra_menu():
    print(colored("\nSelect a Chakra to Generate:", "yellow", attrs=["bold"]))
    for k, (name, freq, color) in CHAKRAS.items():
        chakra_label = colored(f"{k}. {name} Chakra", color, attrs=["bold"])
        print(f"{chakra_label} — {freq} Hz")
    print(colored("8. Generate & Play ALL Chakras", "cyan", attrs=["bold"]))
    print(colored("0. Exit", "red", attrs=["bold"]))
    print(colored("=" * 60, "cyan"))

# ========== Main Logic ==========

def main():
    banner()
    while True:
        chakra_menu()
        try:
            choice = int(input(colored("Enter choice (1–8): ", "yellow")))
        except ValueError:
            print(colored("❌ Invalid input! Please enter a number.", "red"))
            continue

        if choice == 0:
            print(colored("Goodbye — Stay in Harmony 🙏", "cyan"))
            break

        elif choice in CHAKRAS:
            name, freq, color = CHAKRAS[choice]
            try:
                duration = float(input(colored(f"Enter duration for {name} Chakra (seconds): ", color)))
            except ValueError:
                print(colored("❌ Invalid duration!", "red"))
                continue

            action = input(colored("[P]lay or [S]ave? ", "magenta")).strip().lower()
            if action == "p":
                print(colored(f"🎵 Playing {name} Chakra ({freq} Hz)...", color))
                play_tone(freq, duration)
            elif action == "s":
                save_tone(name, freq, duration)
            else:
                print(colored("❌ Invalid option!", "red"))

        elif choice == 8:
            duration = float(input(colored("Enter duration per chakra (seconds): ", "yellow")))
            print(colored("\n🌀 Starting Chakra Alignment Sequence 🌀\n", "magenta", attrs=["bold"]))
            for name, freq, color in CHAKRAS.values():
                print(colored(f"🎶 {name} Chakra ({freq} Hz)...", color))
                play_tone(freq, duration)
            print(colored("\n🌈 All Chakras Activated — Namaste 🙏", "green", attrs=["bold"]))

        else:
            print(colored("❌ Invalid selection!", "red"))

# ========== Entry Point ==========
if __name__ == "__main__":
    main()
