"""Till Firmware Do Us Part: one wedding vow a robot says at its own wedding.

One sentence, under 200 characters: a machine vowing to love through
blackouts and crashes, and to wake beside its partner every morning.
"""

LINE = "I vow to love you through every blackout and every crash, and to wake up beside you every morning for as long as my circuits hold a charge."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space, and a single line.
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
