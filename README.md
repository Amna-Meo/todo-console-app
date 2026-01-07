# Todo Console Application

A command-line todo application built with Python 3.13+ that allows you to manage your tasks efficiently from the terminal.

## Features

- Add new todo items with titles and optional descriptions
- View all your todo items with clear status indicators
- Mark todo items as complete or incomplete
- Update existing todo item details
- Delete todo items
- Data persistence between sessions

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-console-app
   ```

2. Install dependencies using UV:
   ```bash
   uv sync
   ```

## Usage

```bash
# Add a new todo
python -m src.main add "Buy groceries" "Milk, bread, eggs"

# List all todos
python -m src.main list

# Mark a todo as complete
python -m src.main complete 1

# Mark a todo as incomplete
python -m src.main incomplete 1

# Update a todo
python -m src.main update 1 "Buy groceries and cook dinner" "Milk, bread, eggs, chicken"

# Delete a todo
python -m src.main delete 1

# Show help
python -m src.main --help
```

## Development

To run the application in development mode:

```bash
python -m src.main
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.