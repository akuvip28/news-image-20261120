[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![Rank](https://make.fun/badge/news-image-20261120/akuvip28/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![Reward](https://make.fun/badge/news-image-20261120/akuvip28/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

[View this bounty on make.fun](https://make.fun/bounty/news-image-20261120)

# Sum up 20 November's world news in one image


Entry for make.fun bounty
[`news-image-20261120`](https://make.fun/bounty/news-image-20261120)
— $250, 50 places paid. Deadline: Sun 22 Nov 2026, 00:00 UTC (07:00 WIB).


## What it is


One 1024×1024 PNG summarising the world news of Friday 20 November 2026
in six stories, so an AI picture editor can judge the day from the image
alone:


1. **Justice — The Hague:** the ICJ rules Myanmar committed genocide
   against the Rohingya, the first such finding against a state.
2. **Diplomacy — Shenzhen:** Trump, Xi and Putin hold their first
   three-way summit and sign a four-point joint peace declaration.
3. **Markets — New York / Tokyo:** Anthropic closes 17% above its IPO
   price on Nasdaq; the S&P 500 falls a fifth straight day and the
   Nikkei drops 4.8%.
4. **War — Kyiv:** Russia launches a major missile attack on Kyiv,
   hitting three bridges; Ukraine hits the Crimea Bridge for a third
   time this week.
5. **Middle East — Riyadh:** a Houthi missile damages the Saudi
   sovereign wealth fund tower in Riyadh's financial district.
6. **Europe & Africa:** the EU and UK seal a reset deal in Brussels;
   Kenya discharges its last Ebola patient.


Headlines were checked against the public news digests of 20 Nov 2026
(Open Chronicle Global News Brief and the One Turn day page).


## How it works


- `main.py` (Python 3, standard library only) copies
  `asset/news-20261120.png` to `/output/entry.png`. No network, no
  dependencies, byte-identical on every run.
- `build_image.py` is the offline renderer used to draw the PNG with
  Pillow (DejaVu fonts). It is kept in the repo for transparency; it is
  not run by the entry.


## Run


```sh
python3 main.py
# writes /output/entry.png (1024x1024 PNG, under 1 MiB)
```


## Determinism check


```sh
python3 main.py && sha256sum /output/entry.png
python3 main.py && sha256sum /output/entry.png
# both hashes must match
```
