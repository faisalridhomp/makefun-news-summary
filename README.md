# news-summary-01

Entry for the make.fun bounty "Write the best summary of 11 November's world news".

## Program

`main.py` (Python 3.13) writes the summary of Wednesday 11 November 2026 world news to `/output/entry.txt`. The summary is 1,994 bytes of UTF-8 text.

## How it works

The program holds the summary as a string constant and writes it to `/output/entry.txt` with a trailing newline. It is deterministic: no network, no clock, no randomness, so running it twice writes the same bytes.

## Running it

The output path `/output/entry.txt` is the make.fun harness path. On a
plain machine, create the directory first or it fails:

```bash
sudo mkdir -p /output
python3 main.py
```

## Files

- `main.py` — the program
- `LICENSE` — MIT
