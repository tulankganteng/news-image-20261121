"""THE WORLD TODAY -- Saturday 21 November 2026.

Entrypoint for the news-image-20261121 bounty. The repository holds
the finished picture, entry.png, drawn from the day's verified world
news. This program only puts an exact copy of that picture where the
harness reads it, after checking the copy's fingerprint, so a
damaged file can never pass as the entry.

Standard library only. No network. Deterministic: two runs write
the same bytes.
"""

import hashlib
import os
import sys
from pathlib import Path

PICTURE_NAME = "entry.png"
EXPECTED_DIGEST = "23f40ed1c04bd6ccde393725f9a6bd9bb5eb6c4173723ca1dfc7c9b3b502bbc2"


def digest_of(data):
    """SHA-256 hex digest of a byte string."""
    return hashlib.sha256(data).hexdigest()


def destination_folder():
    """Folder the harness reads the finished image from."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if wanted:
        return Path(wanted)
    return Path("/output")


def place_picture():
    """Copy entry.png to the destination, fingerprint-checked."""
    here = Path(__file__).resolve().parent
    source = here / PICTURE_NAME
    picture = source.read_bytes()
    if digest_of(picture) != EXPECTED_DIGEST:
        print("entry.png failed its fingerprint check", file=sys.stderr)
        return 1
    folder = destination_folder()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / PICTURE_NAME
    target.write_bytes(picture)
    print("wrote %s (%d bytes)" % (target, len(picture)))
    return 0


if __name__ == "__main__":
    raise SystemExit(place_picture())
