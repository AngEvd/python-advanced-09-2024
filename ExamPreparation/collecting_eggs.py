from collections import deque

eggs = deque(map(int, input().split(", ")))
papers = deque(map(int, input().split(", ")))
box_size = 50
boxes_filled = 0

while eggs and papers:
    if eggs[0] <= 0:
        eggs.popleft()
    elif eggs[0] == 13:
        eggs.popleft()
        first_paper = papers.popleft()
        last_paper = papers.pop()
        papers.append(first_paper)
        papers.appendleft(last_paper)
    else:
        if eggs[0] + papers[-1] <= box_size:
            boxes_filled += 1
        eggs.popleft()
        papers.pop()

if boxes_filled > 0:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: " + ", ".join(map(str, eggs)))
if papers:
    print(f"Pieces of paper left: " + ", ".join(map(str, papers)))