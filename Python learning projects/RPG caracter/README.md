# RPG Character Creator

A Python function that validates inputs and generates an RPG-style character sheet, built while practicing for the freeCodeCamp Python Certification.

## What it does

`create_character(name, strength, intelligence, charisma)` checks that the name and stats are valid, then returns a character sheet showing each stat as a bar of filled/empty dots.

## Validation rules

- Name: must be a non-empty string, 10 characters or fewer, no spaces
- Stats: must be integers between 1 and 4, and must sum to exactly 7

If a rule is broken, the function returns an error message instead of the sheet.

## Example

```python
create_character('ren', 4, 2, 1)
```

```
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

## Notes

- Pure Python, no external libraries
- No loops — validation uses direct boolean logic
