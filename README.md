# CC2j will convert CSV to JSON

Python 3 program that converts a CSV to a JSON array, and stores that array in output.json

## Installation Instructions:

1. Install Python 3 (Python 3.7.2)
2. Install pipenv (pip install pipenv)
3. Run the command: `pipenv shell`
4. Run the command: `pipenv install --dev`

## Example Usage

1. Create input.csv

```
"First Name","Last Name"
"Willie","Sosa"
"Samantha","Estrada"
"Joseph","Hines"
"Kathryn","Hodge"
"Philip","Long"
```

2. Run the command: `python cc2j.py` 

3. You should now see output.json

```
[
    {
        "First Name": "Willie",
        "Last Name": "Sosa"
    },
    {
        "First Name": "Samantha",
        "Last Name": "Estrada"
    },
    {
        "First Name": "Joseph",
        "Last Name": "Hines"
    },
    {
        "First Name": "Kathryn",
        "Last Name": "Hodge"
    },
    {
        "First Name": "Philip",
        "Last Name": "Long"
    }
]
```

4. Finished! Use your output.json

## Dependencies

Dependency | Reason for Using
--- |---
 Pylint | Linter
 tqdm | Creates a Progress Bar
