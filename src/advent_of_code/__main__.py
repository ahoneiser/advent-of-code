import pathlib

from advent_of_code.twentytwentythree import dayfive, dayfour, dayone, daythree, daytwo

p = dayone.PuzzleOne(pathlib.Path("data/2023/1/input.txt"))

print(f"puzzle one: {p.run()}")

p = dayone.PuzzleTwo(pathlib.Path("data/2023/1/input.txt"))

print(f"puzzle two: {p.run()}")


p = daytwo.PuzzleOne(pathlib.Path("data/2023/2/input.txt"))

result = p.run()

print(f"puzzle one: {result}")

p = daytwo.PuzzleTwo(pathlib.Path("data/2023/2/input.txt"))

result = p.run()

print(f"puzzle two: {result}")


p = daythree.PuzzleOne(pathlib.Path("data/2023/3/input.txt"))

result = p.run()

print(f"puzzle one: {result}")

p = daythree.PuzzleTwo(pathlib.Path("data/2023/3/input.txt"))

result = p.run()

print(f"puzzle two: {result}")

p = dayfour.PuzzleOne(pathlib.Path("data/2023/4/input.txt"))

result = p.run()

print(f"puzzle one: {result}")

p = dayfour.PuzzleTwo(pathlib.Path("data/2023/4/input.txt"))

result = p.run()

print(f"puzzle two: {result}")

p = dayfive.PuzzleOne(pathlib.Path("data/2023/5/input.txt"))

result = p.run()

print(f"puzzle one: {result}")

p = dayfive.PuzzleTwo(pathlib.Path("data/2023/5/input.txt"))

result = p.run()

print(f"puzzle two: {result}")
