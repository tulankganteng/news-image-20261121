# news-image-20261121 — The World Today

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/tulankganteng/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/tulankganteng/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

**Entry for the make.fun bounty [news-image-20261121](https://make.fun/bounty/news-image-20261121)
($100, deadline Mon 2026-11-23 07:00 WIB).** A program that writes one image
summing up the world's news of Saturday 21 November 2026 to `/output/entry.png`.

## What the image shows

A newspaper front page, **"THE WORLD TODAY — SATURDAY 21 NOVEMBER 2026"**:

| Story | What happened |
|---|---|
| **WALL STREET IN CORRECTION / AS NVIDIA SINKS 14%** (lead) | S&P 500 falls 3.7% and Nasdaq 5.3% on Friday as the SEC probes Nvidia's accounting — the AI trade unwinds; the S&P's seventh straight loss, its longest slide since February 2020. |
| **POLAND — MISSILE CRASHES ON NATO SOIL** | A Russian Kh-101 cruise missile crashes near Nowy Lipowiec, about 50 km from the border, during a barrage of 26 Kalibr and 72 Kh-101 missiles plus 503 drones on Ukraine; Tusk calls it a deliberate provocation and NATO jets scramble. |
| **IRAN — TANKER CONVOY TESTS BLOCKADE** | More than 14 tankers mass at Kharg Island to test the US blockade; Trump says he will decide after the New Year, and the Senate votes 51–48 against curbing his war powers. |
| **COP31: FOSSIL FUELS ERASED** | The draft deal drops every mention of fossil fuels as talks spill into overtime; the first COP to admit 1.5°C will be overshot. |
| **UK AND EU SEAL RESET DEAL** | Food checks scrapped from March 2028, worth £5.1bn a year; youth mobility for 100,000 aged 18–31 for up to 3 years. |
| **CYCLONE AKVAN — ODISHA BRACES** | Landfall near Gopalpur at 70–80 km/h, gusting to 90; 300,000 evacuated, 423 rescue teams, 69 trains cancelled. |

The three photographs are AI-generated editorial illustrations made for this
entry (no real person's likeness, no copied photograph); all text is set in
the composition script (`../compose.py`, kept outside the repo) so every word
is crisp and legible. The judge sees only the image — so the date, the
headline and every story are readable on the page itself.

## How it runs

`main.py` (Python 3.13, standard library only) copies the repository-held
`entry.png` to `/output/entry.png` (or to `$MAKEFUN_OUTPUT_DIR` for local
runs). No network, no clock, no randomness — two runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024×1024 PNG, < 1 MiB
```

## News sources (checked 21 Nov 2026)

- Wall Street correction, Nvidia −14%, SEC probe: Reuters, CNN, CNBC, Motley Fool
- Russian Kh-101 missile in Poland, NATO jets scrambled: BBC, Reuters, Helsinki Times
- Iran tanker convoy at Kharg Island, Trump defers decision: Al-Monitor, TankerTrackers, Reuters
- COP31 draft drops fossil fuels, talks in overtime: Reuters, UN News
- UK–EU reset deal (food checks, youth mobility): Reuters
- Cyclone Akvan landfall, evacuations: PTI / IMD via Indian press

## License

MIT — see [LICENSE](LICENSE).

## Reproducibility

The image is fixed: `main.py` copies the repository's own `entry.png`
to the output directory byte for byte, then reads the copy back and
compares it with the source before reporting success. No network calls,
no randomness, no image processing — two runs write identical bytes.
