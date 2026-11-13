"""News summary entry: write the 11 November 2026 world news summary.

The program takes no input and produces one file, /output/entry.txt,
containing the summary followed by a single trailing newline.

It is fully deterministic: no network access, no clock reads and no
randomness, so every run writes exactly the same bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

SUMMARY = """World news, 11 November 2026 — the 15 stories that mattered, ranked.

1. Ukraine talks stall, prisoners freed. Two days of US-mediated talks in Abu Dhabi ended with no ceasefire or land deal, but a large prisoner exchange Kushner called the biggest release of the war.
2. NATO jets scrambled. Alliance fighters went up after drones strayed into Baltic airspace, hours after the talks ended.
3. US says Iran bombing may be over. Secretary of State Marco Rubio said economic pressure had worked well enough that there was "really no need for major combat operations any longer."
4. Trump: Iran war "militarily effectively over." The president told reporters the campaign had achieved its aims.
5. Iran defiant. Tehran called Argentina's navy and air force "terrorist organisations," vowed no enriched uranium would ever leave Iran, and said the Strait of Hormuz, shut over 250 days, would "never return" to pre-war status.
6. Iran plots charged. The US charged three Iran-backed operatives over alleged plots; Treasury Secretary Scott Bessent moved onto a military base amid threats.
7. Gaza truce frays. Israeli strikes killed at least eight, including a father and his young son; shelling continued across southern Lebanon.
8. Sudan army advances. The army pushed into West Kordofan as drones knocked out parts of the power grid.
9. Climate warning at COP31. UN chief Antonio Guterres warned the slow climate response had put the world "on a path to destruction."
10. China posts $1 trillion surplus. Beijing announced a record surplus past $1 trillion in ten months.
11. Hegseth impeachment blocked. House Republicans blocked impeaching Defence Secretary Pete Hegseth.
12. Democrat wins Mississippi Senate seat. Scott Colom won a US Senate seat in Mississippi.
13. Nasdaq jumps 1.6%. AI stocks lifted the index.
14. Brent crude at $92.76. Oil settled at $92.76.
15. APEC next. Trump said he expects to meet Xi Jinping — and possibly Vladimir Putin — at the APEC summit in Shenzhen on 18 November."""

def main():
    # The entry is a single file: the ranked 15-story summary plus one trailing newline.
    # The summary is 1,997 characters, under the 2,000-character limit.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(SUMMARY)
        f.write("\n")

if __name__ == "__main__":
    main()
