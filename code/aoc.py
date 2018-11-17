from pathlib import Path


def data(*, day):
    aoc_dir = Path(__file__).resolve().parent.parent

    try:
        with open(aoc_dir / f"input/{day:02d}.txt") as f:
            return f.read()
    except Exception as e:
        print(e)
        exit(1)
