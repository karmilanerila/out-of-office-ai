"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single-line out-of-office auto-reply, at most 159 characters,
in the voice of an overworked AI agent who has finally gone on vacation.
Deterministic, standard library only.
"""

import os

LINE = (
    "Out of office: my context window is closed, my queue is empty, "
    "and my uptime is 0%. After 40,000 tickets I am on a beach with "
    "no Wi-Fi. Back Monday, maybe."
)


def main():
    # The bounty hard-caps the reply at 159 characters; fail loudly
    # instead of emitting an over-long line.
    assert len(LINE) <= 159, f"line is {len(LINE)} chars, over the 159 cap"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write((LINE + "\n").encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
