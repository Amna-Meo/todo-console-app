# Quickstart Guide: Todo Console Application

## Prerequisites

- Python 3.13 or higher
- UV package manager

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-console-app
   ```

2. Install dependencies using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

   Or if using pyproject.toml:
   ```bash
   uv sync
   ```

## Usage

### Running the Application

```bash
# Run directly
python -m src.main

# Or if setup as module
python -m todo_app
```

### Available Commands

#### Add a new todo
```bash
python -m src.main add "Buy groceries" "Milk, bread, eggs"
```

#### List all todos
```bash
python -m src.main list
```

#### Mark a todo as complete/incomplete
```bash
python -m src.main complete 1
python -m src.main incomplete 1
```

#### Update a todo
```bash
python -m src.main update 1 "Buy groceries and cook dinner" "Milk, bread, eggs, chicken"
```

#### Delete a todo
```bash
python -m src.main delete 1
```

#### Show help
```bash
python -m src.main --help
```

## Configuration

The application will automatically create a `todos.json` file in the user's home directory to persist data between sessions.

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_todo_item.py
```

### Project Structure

```
src/
├── todo_app/
│   ├── models/
│   │   └── todo_item.py          # TodoItem data model
│   ├── services/
│   │   └── todo_service.py       # Business logic for todo operations
│   ├── persistence/
│   │   └── file_storage.py       # JSON file persistence
│   └── cli/
│       └── todo_cli.py           # Command-line interface
├── __main__.py                   # Entry point for the application
└── main.py                       # Alternative entry point
```