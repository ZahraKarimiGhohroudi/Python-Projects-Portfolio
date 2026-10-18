<h1 align="center">🔐 🔑 🔢 Password Toolkit</h1>

<p align="center">
  <img src="data/images.jpeg" alt="Password Toolkit" width="480">
</p>

<p align="center">
  A small Python toolkit for generating secure random passwords, memorable passphrases, and numeric PIN codes.
</p>

---

## ✨ Features

- 🎲 **Random passwords** with a configurable length, numbers, and symbols. Every selected character group appears at least once.
- 📝 **Memorable passphrases** made of random words, with optional capitalization and a custom separator.
- 🔢 **PIN codes** containing digits only.
- 🔒 Uses Python's `secrets` module, which is designed for cryptographically secure randomness.
- 🧪 Covered by unit tests with `pytest`.

## 🧩 How it works

| Generator | Example output | Main options |
|-----------|----------------|--------------|
| `RandomPasswordGenerator` | `k7Q!vR2#pM9x` | `length`, `include_numbers`, `include_symbols` |
| `MemorablePasswordGenerator` | `River-Candle-Orange` | `num_of_words`, `separator`, `capitalization`, `vocabulary` |
| `PinCodeGenerator` | `482019` | `length` |

If a length or word count is below the minimum, the generator prints a message and uses the minimum value instead.

## ⚙️ Requirements

- Python 3.12 or newer
- [pytest](https://pytest.org/) for running the tests
- [NLTK](https://www.nltk.org/) for the default word list

## 🚀 How to run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Download the NLTK word list once:

```bash
python -c "import nltk; nltk.download('words')"
```

Use the classes in your own code:

```python
from password_toolkit import (
    MemorablePasswordGenerator,
    PinCodeGenerator,
    RandomPasswordGenerator,
)

print(RandomPasswordGenerator(length=16).generate())
print(MemorablePasswordGenerator(num_of_words=4, separator="-", capitalization=True).generate())
print(PinCodeGenerator(length=6).generate())
```

Run the tests from the project root:

```bash
python -m pytest -v
```

## 🧠 Concepts used

- Abstract base classes and inheritance (`PasswordGenerator`)
- Cryptographically secure randomness with `secrets`
- Input validation and default fallbacks
- Type hints and docstrings
- Unit testing with `pytest`, including `pytest.raises`

## 📁 Project structure

```
Password_Toolkit/
├── data/
│   └── images.jpeg
├── password_toolkit/
│   ├── __init__.py
│   └── generators.py
├── tests/
│   └── test_generators.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## 📄 License

This project is licensed under the terms in the [LICENSE](../LICENSE) file.