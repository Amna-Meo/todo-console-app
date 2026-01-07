import json
import os
from pathlib import Path
from typing import List, Optional
from ..models.todo_item import TodoItem


class FileStorage:
    """
    JSON file persistence for todo items.
    """

    def __init__(self, storage_path: Optional[str] = None):
        """
        Initialize FileStorage with a storage path.

        Args:
            storage_path: Path to the JSON file for storage (default: ~/.todos.json)
        """
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            # Use home directory for default storage
            home = Path.home()
            self.storage_path = home / ".todos.json"

    def save_todos(self, todos: List[TodoItem]) -> bool:
        """
        Save a list of todo items to the storage file.

        Args:
            todos: List of TodoItems to save

        Returns:
            True if save was successful, False otherwise
        """
        try:
            # Convert todos to dictionary format
            todos_data = [todo.to_dict() for todo in todos]

            # Ensure directory exists
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)

            # Write to file
            with open(self.storage_path, 'w', encoding='utf-8') as file:
                json.dump({"todos": todos_data}, file, indent=2, ensure_ascii=False)

            return True
        except Exception as e:
            print(f"Error saving todos: {e}")
            return False

    def load_todos(self) -> List[TodoItem]:
        """
        Load todo items from the storage file.

        Returns:
            List of loaded TodoItems, or empty list if file doesn't exist or is corrupted
        """
        if not self.storage_path.exists():
            return []

        try:
            with open(self.storage_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            if not isinstance(data, dict) or "todos" not in data:
                print(f"Warning: Invalid data format in {self.storage_path}")
                return []

            todos_data = data["todos"]
            if not isinstance(todos_data, list):
                print(f"Warning: Invalid todos format in {self.storage_path}")
                return []

            todos = []
            for todo_data in todos_data:
                try:
                    todo = TodoItem.from_dict(todo_data)
                    todos.append(todo)
                except Exception as e:
                    print(f"Warning: Could not load todo item: {e}")
                    continue

            return todos
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {self.storage_path}: {e}")
            return []
        except FileNotFoundError:
            # This is expected if no todos exist yet
            return []
        except PermissionError:
            print(f"Error: Permission denied when accessing {self.storage_path}")
            return []
        except Exception as e:
            print(f"Error loading todos: {e}")
            return []

    def clear_storage(self) -> bool:
        """
        Clear the storage file.

        Returns:
            True if successful, False otherwise
        """
        try:
            if self.storage_path.exists():
                self.storage_path.unlink()
            return True
        except Exception as e:
            print(f"Error clearing storage: {e}")
            return False