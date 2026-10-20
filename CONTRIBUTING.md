# Contributing to Scritchy Scratchy Trainer

Thanks for wanting to help out. This is a hobbyist Windows desktop trainer
built around the *Scritchy Scratchy* rhythm game client.

## Ground rules
- Keep PRs focused. One feature per PR.
- Match the existing layered layout: `bootstrap/` → `core/` → `handlers/` → `helpers/`.
- Don't hardcode offsets; put them in `core/offsets.py` with a comment on which
  game build they target.
- Any new handler must register itself in `handlers/__init__.py`.

## Dev setup
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m scritchy_trainer
```

## Reporting bugs
Open an issue with:
- Windows version
- Game build / patch
- Trainer version (from `scritchy_trainer/__init__.py`)
- Relevant `logs/` snippet

## Educational use only
This repository exists for reverse-engineering practice and modding education.
Do not use it to grief other players in ranked lobbies.