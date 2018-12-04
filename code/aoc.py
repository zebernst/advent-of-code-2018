from pathlib import Path


def data(*, day: int):
    aoc_dir = Path(__file__).resolve().parent.parent

    if not isinstance(day, int):
        print(f"{day} is not a number!")
        exit(1)

    try:
        with open(aoc_dir / "input" / f"{day:02d}.txt") as f:
            return f.read().strip()
    except Exception as e:
        print(f"Couldn't load data for day {day}.")
        print(e)
        exit(1)
