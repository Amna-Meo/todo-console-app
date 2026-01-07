import argparse
import sys
from typing import Optional
from ..services.todo_service import TodoService
from ..persistence.file_storage import FileStorage
from ..models.todo_item import TodoItem


class TodoAppCLI:
    """
    Command-line interface for the todo application.
    """

    def __init__(self, service: Optional[TodoService] = None, storage: Optional[FileStorage] = None):
        """
        Initialize the CLI with services.

        Args:
            service: TodoService instance (will create new one if None)
            storage: FileStorage instance (will create new one if None)
        """
        self.service = service if service else TodoService()
        self.storage = storage if storage else FileStorage()

        # Load existing todos at startup
        self.service.todos = self.storage.load_todos()

    def run(self, args: Optional[list] = None):
        """
        Run the CLI application with the given arguments.

        Args:
            args: Command-line arguments (sys.argv[1:] if None)
        """
        if args is None:
            args = sys.argv[1:]

        parser = argparse.ArgumentParser(
            description="A command-line todo application",
            prog="todo"
        )
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Add command
        add_parser = subparsers.add_parser("add", help="Add a new todo item")
        add_parser.add_argument("title", help="Title of the todo item")
        add_parser.add_argument("description", nargs="?", default=None,
                                help="Optional description of the todo item")

        # List command
        list_parser = subparsers.add_parser("list", help="List all todo items")
        list_parser.add_argument("--completed", action="store_true",
                                 help="Show only completed todos")
        list_parser.add_argument("--pending", action="store_true",
                                 help="Show only pending todos")

        # Complete command
        complete_parser = subparsers.add_parser("complete", help="Mark a todo as complete")
        complete_parser.add_argument("id", help="ID of the todo item to mark complete")

        # Incomplete command
        incomplete_parser = subparsers.add_parser("incomplete", help="Mark a todo as incomplete")
        incomplete_parser.add_argument("id", help="ID of the todo item to mark incomplete")

        # Update command
        update_parser = subparsers.add_parser("update", help="Update a todo item")
        update_parser.add_argument("id", help="ID of the todo item to update")
        update_parser.add_argument("--title", help="New title for the todo item")
        update_parser.add_argument("--description", help="New description for the todo item")

        # Delete command
        delete_parser = subparsers.add_parser("delete", help="Delete a todo item")
        delete_parser.add_argument("id", help="ID of the todo item to delete")

        # Parse arguments
        parsed_args = parser.parse_args(args)

        # Execute command
        if parsed_args.command == "add":
            self.handle_add(parsed_args.title, parsed_args.description)
        elif parsed_args.command == "list":
            self.handle_list(parsed_args.completed, parsed_args.pending)
        elif parsed_args.command == "complete":
            self.handle_complete(parsed_args.id)
        elif parsed_args.command == "incomplete":
            self.handle_incomplete(parsed_args.id)
        elif parsed_args.command == "update":
            self.handle_update(parsed_args.id, parsed_args.title, parsed_args.description)
        elif parsed_args.command == "delete":
            self.handle_delete(parsed_args.id)
        else:
            parser.print_help()

    def handle_add(self, title: str, description: Optional[str] = None):
        """Handle the add command."""
        try:
            # Validate input
            if not title or not title.strip():
                print("Error: Title cannot be empty")
                return

            # Limit title length to prevent extremely long titles
            if len(title) > 1000:
                print("Error: Title is too long (maximum 1000 characters)")
                return

            todo = self.service.create_todo(title, description)
            print(f"Todo added successfully with ID: {todo.id}")

            # Save to storage
            if self.storage.save_todos(self.service.todos):
                print("Changes saved to storage.")
            else:
                print("Warning: Could not save changes to storage.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def handle_list(self, completed: bool = False, pending: bool = False):
        """Handle the list command."""
        if completed:
            todos = self.service.get_completed_todos()
            print("Completed todos:")
        elif pending:
            todos = self.service.get_pending_todos()
            print("Pending todos:")
        else:
            todos = self.service.get_all_todos()
            print("All todos:")

        if not todos:
            print("No todos found.")
        else:
            for todo in todos:
                status = "✓" if todo.completed else "○"
                print(f"[{status}] ID: {todo.id}")
                print(f"    Title: {todo.title}")
                if todo.description:
                    print(f"    Description: {todo.description}")
                print(f"    Created: {todo.created_at}")
                print()

    def handle_complete(self, todo_id: str):
        """Handle the complete command."""
        if self.service.update_todo_status(todo_id, True):
            print(f"Todo {todo_id} marked as complete")

            # Save to storage
            if self.storage.save_todos(self.service.todos):
                print("Changes saved to storage.")
            else:
                print("Warning: Could not save changes to storage.")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def handle_incomplete(self, todo_id: str):
        """Handle the incomplete command."""
        if self.service.update_todo_status(todo_id, False):
            print(f"Todo {todo_id} marked as incomplete")

            # Save to storage
            if self.storage.save_todos(self.service.todos):
                print("Changes saved to storage.")
            else:
                print("Warning: Could not save changes to storage.")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def handle_update(self, todo_id: str, title: Optional[str] = None, description: Optional[str] = None):
        """Handle the update command."""
        if title is None and description is None:
            print("Error: Please provide at least one field to update (--title or --description)")
            return

        # Validate title if provided
        if title is not None:
            if not title.strip():
                print("Error: Title cannot be empty")
                return
            if len(title) > 1000:
                print("Error: Title is too long (maximum 1000 characters)")
                return

        if self.service.update_todo_details(todo_id, title, description):
            print(f"Todo {todo_id} updated successfully")

            # Save to storage
            if self.storage.save_todos(self.service.todos):
                print("Changes saved to storage.")
            else:
                print("Warning: Could not save changes to storage.")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def handle_delete(self, todo_id: str):
        """Handle the delete command."""
        if self.service.delete_todo(todo_id):
            print(f"Todo {todo_id} deleted successfully")

            # Save to storage
            if self.storage.save_todos(self.service.todos):
                print("Changes saved to storage.")
            else:
                print("Warning: Could not save changes to storage.")
        else:
            print(f"Error: Todo with ID {todo_id} not found")


def main():
    """Main entry point for the CLI application."""
    cli = TodoAppCLI()
    cli.run()


if __name__ == "__main__":
    main()