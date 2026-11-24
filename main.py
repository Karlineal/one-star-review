"""Writes the entry: one line (144 characters), a deadpan one-star review of sleep.

The sandbox runs it offline, once per grade; it only writes /output/entry.txt.
"""

import pathlib

LINE = (
    "One star. Sleep is advertised as free and then bills you in whole evenin"
    "gs. Support unresponsive. Would not recommend to anyone with a deadline."
)


def main() -> None:
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
