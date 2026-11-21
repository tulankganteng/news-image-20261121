#!/usr/bin/env python3
"""Place the front page image where the harness expects it.

The newspaper front page for Saturday 21 November 2026 is stored in this
repository as entry.png. This program reads those bytes and writes them,
unchanged, to ``entry.png`` inside the output directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (``/output`` when the
variable is absent). It does no image processing and no network access,
so running it twice always produces identical bytes. The copy is
verified byte-for-byte after writing, so a partial or failed write
is reported instead of passing silently.
"""

import hashlib
import os
import sys
from pathlib import Path


def locate_source() -> Path:
    """Return the path of the image held in this repository."""
    return Path(__file__).resolve().parent / "entry.png"


def output_path() -> Path:
    """Return where the image must be written."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(directory) / "entry.png"


def main() -> int:
    source = locate_source()
    target = output_path()
    data = source.read_bytes()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    written = target.read_bytes()
    if written != data:
        print(f"mismatch: {target} differs from {source}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {target} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
