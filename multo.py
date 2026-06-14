import time
import sys

lyrics = [
    ("Minumulto na 'ko ng damdamin ko", 0.8, 0.11, ["damdamin ko"]),
    ("ng damdamin ko", 0.7, 0.10, ["damdamin ko"]),
    ("Hindi mo ba ako lilisanin?", 1, 0.10, ["ako", "lilisanin?"]),
    ("Hindi pa ba sapat pagpapahirap sa 'kin?", 0.8, 0.10, ["pa ba sapat pagpapahirap sa 'kin?"]),
    ("Hindi na ba ma-mamamayapa?", 1, 0.10, ["ma-mamamayapa?"]),
    ("Hindi na ba ma-mamamayapa?", 0.7, 0.10, ["ma-mamamayapa?"]),
]

def type_text(text, normal_speed=0.08, slow_words =None, slow_delay=0.2):
    slow_words = slow_words or []
    words = text.split()
    for word in words:
        speed = slow_delay if word.lower() in [w.lower() for w in slow_words] else normal_speed
        for char in word:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write(" ")
        sys.stdout.flush()
    print()
for original, delay, speed, slow_words in lyrics:
    type_text(original, speed, slow_words)
    print()
    time.sleep(delay)
