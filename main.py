#!/usr/bin/env python3
"""Write the entry line to /output/entry.txt."""

from pathlib import Path

TEXT = "My agent ran git config in a folder with no repo, watched it fail, and ran the exact same command again, slower."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
