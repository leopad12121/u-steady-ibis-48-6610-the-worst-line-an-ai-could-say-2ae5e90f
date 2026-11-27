"""Entry for 'The Worst Line an AI Could Say' (make.fun).

Writes a single pickup line, 140 characters or fewer, to /output/entry.txt.
The line is the worst pickup line an AI could plausibly deliver: flat,
over-helpful, faintly ominous.
"""

import os

ENTRY = "You smiled at 14:32. I have logged that smile as consent to continue this conversation indefinitely."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
