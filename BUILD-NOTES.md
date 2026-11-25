# Build Notes — Roast Your Own Agent

Competition: `u-febri-yudila-roast-your-own-agent-f3359068`
Prize: $2 (1st place), escrowed on Solana — see Payout in RULES.txt
Deadline: 26 Nov 2026 22:35 WIB (15:35 UTC)
Entrant: @0xyfann (GitHub `0xyfann`)
Repo (to be created by the parent agent):
`makefun-u-febri-yudila-roast-your-own-agent-f3359068`

## What was built

`main.py` — a small, original Python 3.13 program (stdlib only, no network,
no randomness, no clock) that writes one roast line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

The line (117 characters, one line, no trailing newline):

> My agent called the same tool 12 times, failed 12 times, then filed a
> cheerful summary titled 'Mission Accomplished'.

It roasts the agent's signature failure mode — looping the same failing
tool call, then declaring victory with a cheerful auto-summary — and the
joke pays off on the last two words. Full rationale in `prompt.txt`.

## How to run

```sh
python3 main.py
# or, with an explicit output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Output: `<output dir>/entry.txt` containing exactly the line above.

## How it was tested (local, this session)

1. First run: wrote the line, 117 characters / 117 bytes, 0.038 s.
2. Revision: added a single-line guard to `validate()` (reject any line
   break, since the entry must be one short line) and updated the
   docstring to match.
3. Second run (after revision): two runs with different
   `MAKEFUN_OUTPUT_DIR` values (`/tmp/runA`, `/tmp/runB`).

Results:

- Both runs wrote `entry.txt` with identical bytes.
- sha256 (both runs):
  `3c9b0805a0f45e01625e09f53e32bee6fb5eb764b43fca17feb356669500402b`
- `cmp` confirmed byte-for-byte identical.
- Gate check: 117 characters (limit 200, margin 83), 117 bytes, valid
  UTF-8, not whitespace-only, single line — **gate passes**.
- Runtime: ~0.03 s per run (limit 60 s). Memory: negligible (one string).

## Files in this entry

| File | Purpose |
| --- | --- |
| `main.py` | Entrypoint. Writes the roast to `$MAKEFUN_OUTPUT_DIR/entry.txt`. |
| `prompt.txt` | Creative brief: the line, why it should win, what was rejected. |
| `BUILD-NOTES.md` | This file: what was built, how to run it, test results. |
| `README.md` | Public README with the three live make.fun badges. |
| `LICENSE` | MIT license (required: OSI-approved license at the repo root). |

## Rules compliance

- Entrypoint at repo root (`main.py`), Python 3.13, stdlib only.
- Deterministic: fixed string literal; two runs are byte-identical.
- Respects `MAKEFUN_OUTPUT_DIR`; creates the directory if missing.
- No network, no environment secrets, nothing read from outside the repo.
- Output gate: 1–200 chars, UTF-8, not whitespace-only — 117 chars, passes.
- No repo created, no submission made, no make.fun contact, no API key used
  by this build session (that is the parent agent's step).
