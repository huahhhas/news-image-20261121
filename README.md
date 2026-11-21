[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/huahhhas/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/huahhhas/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# World news, 21 November 2026, in one image

A newspaper front page — **THE WORLD TODAY, Saturday, 21 November 2026** —
summing up the day's world news in a single 1024×1024 image.

## The stories

- **Russian missiles hit Poland** — Two Russian missiles and a suspected drone
  crashed in south-east Poland during a huge overnight barrage on Ukraine.
  Prime Minister Donald Tusk called it a deliberate provocation; NATO chief
  Mark Rutte called it a grave violation of Polish airspace and flew to
  Warsaw. No one was hurt; allied jets scrambled and Patriot batteries were
  put on alert.
- **Wall Street in free fall** — The S&P 500 fell 3.7% and the Dow 950 points,
  both entering correction territory. The Nasdaq lost 5.3%, wiping out its
  2026 gains, as Nvidia slid 14% after its chief executive resigned and the
  Anthropic IPO fizzled.
- **Cyclone Akvan hits India** — The storm crossed the Odisha coast near
  Gopalpur with fierce winds and rain. About 300,000 people were moved to
  safety.
- **Court: Myanmar committed genocide** — Rights groups demanded action after
  the world court ruled Myanmar committed genocide against the Rohingya.
- Also: Rutte in Warsaw, NSE now the world's 5th-largest exchange, India
  fight back in the Wellington Test, COP31 in its final stage, and the
  Trump–Xi–Putin summit ending with few results.

## How it is made

`draw_poster_21.py` (kept with the build notes) draws the front page with
PIL: masthead, headlines, a drawn night scene over a Polish village, a
falling-markets chart, and a news band. The drawing is deterministic — two
runs produce byte-identical PNGs. `main.py` (Python 3.13, standard library
only) copies `entry.png` to the output directory.

## Entry

- Competition: [news-image-20261121 on make.fun](https://make.fun/bounty/news-image-20261121)
- Program: `main.py` writes `entry.png` to `/output/entry.png`
- Image: 1024×1024 PNG, under 1 MiB
