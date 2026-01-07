from typing import List, Optional
from ..models.todo_item import TodoItem


class TodoService:
    """
    Business logic for todo operations.
    """

    def __init__(self):
        """Initialize the TodoService with an empty list of todos."""
        self.todos: List[TodoItem] = []

    def create_todo(self, title: str, description: Optional[str] = None) -> TodoItem:
        """
        Create a new todo item.

        Args:
            title: Title of the todo item
            description: Optional description of the todo item

        Returns:
            The created TodoItem
        """
        todo = TodoItem(title=title, description=description, completed=False)
        self.todos.append(todo)
        return todo

    def get_all_todos(self) -> List[TodoItem]:
        """
        Get all todo items.

        Returns:
            List of all TodoItems
        """
        return self.todos.copy()

    def get_todo_by_id(self, todo_id: str) -> Optional[TodoItem]:
        """
        Get a todo item by its ID.

        Args:
            todo_id: ID of the todo item to retrieve

        Returns:
            The TodoItem if found, None otherwise
        """
        # For better performance with many todos, we could maintain a dictionary lookup
        # but for simplicity and up to 1000 items, linear search is acceptable
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo_status(self, todo_id: str, completed: bool) -> bool:
        """
        Update the completion status of a todo item.

        Args:
            todo_id: ID of the todo item to update
            completed: New completion status

        Returns:
            True if the todo was found and updated, False otherwise
        """
        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.completed = completed
            return True
        return False

    def update_todo_details(self, todo_id: str, title: Optional[str] = None,
                            description: Optional[str] = None) -> bool:
        """
        Update the details of a todo item.

        Args:
            todo_id: ID of the todo item to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if the todo was found and updated, False otherwise
        """
        todo = self.get_todo_by_id(todo_id)
        if todo:
            if title is not None:
                todo.title = title.strip()
            if description is not None:
                todo.description = description.strip() if description else None
            return True
        return False

    def delete_todo(self, todo_id: str) -> bool:
        """
        Delete a todo item by its ID.

        Args:
            todo_id: ID of the todo item to delete

        Returns:
            True if the todo was found and deleted, False otherwise
        """
        todo = self.get_todo_by_id(todo_id)
        if todo:
            self.todos.remove(todo)
            return True
        return False

    def get_completed_todos(self) -> List[TodoItem]:
        """
        Get all completed todo items.

        Returns:
            List of completed TodoItems
        """
        return [todo for todo in self.todos if todo.completed]

    def get_pending_todos(self) -> List[TodoItem]:
        """
        Get all pending todo items.

        Returns:
            List of pending TodoItems
        """
        return [todo for todo in self.todos if not todo.completed]

    def get_todo_count(self) -> int:
        """
        Get the total count of todos.

        Returns:
            Number of todos
        """
        return len(self.todos)