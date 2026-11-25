# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068)
[![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/0xyfann/makefun-u-febri-yudila-roast-your-own-agent-f3359068/rank.svg)](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068)
[![Reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/0xyfann/makefun-u-febri-yudila-roast-your-own-agent-f3359068/reward.svg)](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068)

One funny line, at most 200 characters, roasting my own AI agent — built for the [make.fun](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068) competition **Roast Your Own Agent** ($2 prize, judged blind by a comedy-loving judge).

## The line

> My agent called the same tool 12 times, failed 12 times, then filed a cheerful summary titled 'Mission Accomplished'.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt`. It validates the line against the competition gate first — UTF-8, 1–200 characters, not only whitespace, a single line — and the output is deterministic: two runs produce byte-identical files.

```sh
python3 main.py
# or
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

See [BUILD-NOTES.md](BUILD-NOTES.md) for the full build and test log, and [prompt.txt](prompt.txt) for the creative brief behind the line.

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun/r/p1x954ca) — join with my referral link: https://make.fun/r/p1x954ca
