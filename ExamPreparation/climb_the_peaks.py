from collections import deque

food_portions = list(map(int, input().split(", ")))
daily_stamina = deque(map(int, input().split(", ")))

mountain_peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

conquered_peaks = []

while food_portions and daily_stamina and mountain_peaks:
    daily_effort = food_portions.pop() + daily_stamina.popleft()
    if daily_effort >= mountain_peaks[0][1]:
        conquered_peaks.append(mountain_peaks.popleft()[0])

if not mountain_peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print("Conquered peaks:\n" + "\n".join(conquered_peaks))
