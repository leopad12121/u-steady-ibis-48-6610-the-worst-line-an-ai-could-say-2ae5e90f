"""The Worst Line an AI Could Say entry: writes a single line to entry.txt.

Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = "Are you a captcha? Because I keep failing the 'I am not a robot' checkbox around you — and honestly, neither can you."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
