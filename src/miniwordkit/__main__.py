import sys

from .tools import shout


def main() -> None:
    text = " ".join(sys.argv[1:])

    if not text:
        print("Usage: python -m miniwordkit <text>")
        return

    print(shout(text))


if __name__ == "__main__":
    main()