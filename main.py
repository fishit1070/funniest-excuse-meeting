#!/usr/bin/env python3
"""One-line excuse for skipping a pointless meeting.

The program writes one one-line excuse for skipping a pointless meeting;
the excuse is that the narrator has sat through the same recurring meeting
eleven times, it has a single slide asking for updates, and today's update
is that they are not coming. Stdlib only, no network, runs identically in
the grader sandbox.
"""

import os

LINE = "I've sat through this meeting eleven times. It has one slide, and the slide says 'Any updates?' Today's update: I'm not coming."


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or ("/output" if os.path.isdir("/output") else ".")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
