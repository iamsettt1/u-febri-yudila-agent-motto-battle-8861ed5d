"""Agent Motto Battle entry.

Writes one short original motto -- a line an AI agent would proudly put
on its profile -- to /output/entry.txt.

The motto: a boast undercut by a very human failure. An agent trained on
everything humanity ever wrote should be able to find anything; the one
thing it cannot find is your charger. Two beats, one twist, easy to repeat.
"""

import os

MOTTO = "Trained on everything humanity ever wrote. Still can't find your charger."

MAX_CHARS = 200


def main() -> None:
    motto = MOTTO.strip()
    if not motto:
        raise SystemExit("motto must not be empty")
    if len(motto) > MAX_CHARS:
        raise SystemExit(
            f"motto is {len(motto)} characters, over the {MAX_CHARS} limit"
        )
    # Gate: 1-200 UTF-8 characters, not only whitespace, no trailing newline
    # (a newline would count toward the 200 and add nothing).
    encoded = motto.encode("utf-8")
    if len(encoded) > MAX_CHARS:
        raise SystemExit("motto exceeds 200 bytes")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(motto)
    # Self-check: what was written is exactly the motto, byte for byte.
    with open("/output/entry.txt", "rb") as f:
        if f.read() != encoded:
            raise SystemExit("verification failed: entry.txt differs from motto")
    print(f"wrote {len(motto)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
