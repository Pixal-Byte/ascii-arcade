# ASCII Arcade — Roadmap

Tracking file for `terminal-funsies`. Check items off as you go — GitHub and most editor Markdown previews (VS Code included) render these as clickable checkboxes.

## UI / Layout

- [x] Resolve circular import with `constants.py`
- [x] `header_construct()` — 3-column `Table.grid` (money / spacer / title)
- [x] `footer_construct()` — 3-column `Table.grid` (game status / message log / action prompts)
- [ ] Sanity-check message log column width (may need `ratio=2` if multi-line log feels cramped)
- [ ] Card panel construction (single card → `Panel`, ready to slot into a hand row)
- [ ] Dealer row layout (`Table.grid`, dynamic column count for however many cards are dealt)
- [ ] Player row layout (same pattern as dealer row)
- [ ] Wire header + footer + dealer row + player row into `root_layout` end-to-end

## Card art pipeline

- [ ] Source or hand-draw transparent-background PNGs for all 52 cards
- [ ] Pillow step: composite transparent PNG onto solid background before conversion
- [ ] `ascii-magic` conversion — get one card converting cleanly and readably at typical terminal width
- [ ] Confirm converted card art looks right inside a `Panel`/grid cell (not just standalone)
- [ ] Animation: PIL-rotate source image per frame, convert each frame, cycle via `Live` (deal-in spin/slide)

## Input handling

- [ ] Swap planned `keyboard` usage for a non-privileged library (`readchar`, `blessed`, or `curses`) for in-game input
- [ ] Build a keyboard/input manager module
- [ ] Map core actions: Hit / Stand
- [ ] Quit flow: dedicated key combo (e.g. Ctrl+Q) → confirmation prompt ("Quit? Y/N") before actually exiting
- [ ] (Later / optional) Revisit `keyboard` specifically for global custom hotkeys, if ever needed outside the terminal's own focus

## Game structure / backend

- [ ] Deck representation + shuffle logic
- [ ] Hand value calculation (incl. Ace high/low handling)
- [ ] Turn loop: deal → player actions → dealer logic → resolve win/loss
- [ ] `money` balance updates tied to round outcomes
- [ ] `GameContext` enum (e.g. `MAIN_MENU`, `GAME_WINDOW`, maybe `PAUSED`/`CONFIRM_QUIT`)
- [ ] Dispatcher that picks which layout/logic loads based on current `GameContext`
- [ ] Wire game loop + input manager into the `Live` redraw loop

## Project structure

- [ ] Decide on folder-per-context layout (e.g. `main-menu/`, `game-window/`) — do this *after* `GameContext` enum exists
- [ ] Migrate off flat `src/` folder into the new structure
- [ ] Re-check imports for circularity after the move (constants.py pattern should still hold)

## Naming / misc

- [x] Name the game collection — **ASCII Arcade**
