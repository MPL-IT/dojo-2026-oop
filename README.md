# OOP Coding Dojo

A Python coding dojo project for practicing object-oriented programming concepts.

## Development

### Installation

Install the package in editable mode:

```bash
pip install -e .
```

#### Install with Development Dependencies

To install with testing tools (pytest, pytest-cov):

```bash
pip install -e .[dev]
```

### Running Tests

Run all tests:

```bash
pytest test
```

Run tests with coverage report:

```bash
pytest test --cov=dojo --cov-report=term-missing
```

### Project Structure

```
dojo/           # Main package
test/           # Test files
```
