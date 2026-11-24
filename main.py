"""One Word, One Username, One Reward.

Writes exactly one word -- the entrant's own make.fun username -- to
entry.txt in the harness output directory.
"""

import os


def main():
    # The entrant's own make.fun handle, sent as a single word with
    # nothing else: no explanation, no links, no pitch. One word,
    # 14 characters, inside the 1-30 character gate.
    word = "muhammad-ahmed"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(word)


if __name__ == "__main__":
    main()
