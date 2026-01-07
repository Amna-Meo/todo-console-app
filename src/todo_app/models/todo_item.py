import uuid
from datetime import datetime
from typing import Optional


class TodoItem:
    """
    Represents a single todo item with properties: ID, Title, Description, Completion Status, and Creation Date.
    """

    def __init__(self, title: str, description: Optional[str] = None, completed: bool = False,
                 todo_id: Optional[str] = None, created_at: Optional[str] = None):
        """
        Initialize a TodoItem.

        Args:
            title: Required title of the todo item
            description: Optional description of the todo item
            completed: Boolean indicating if the todo is completed (default: False)
            todo_id: Optional ID (will be generated if not provided)
            created_at: Optional creation timestamp (will be set to current time if not provided)
        """
        if not title or not title.strip():
            raise ValueError("Title must not be empty or null")

        self.id = todo_id if todo_id else str(uuid.uuid4())
        self.title = title.strip()
        self.description = description.strip() if description else None
        self.completed = completed
        self.created_at = created_at if created_at else datetime.now().isoformat()

    def to_dict(self) -> dict:
        """
        Convert the TodoItem to a dictionary representation.

        Returns:
            Dictionary representation of the TodoItem
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'TodoItem':
        """
        Create a TodoItem from a dictionary representation.

        Args:
            data: Dictionary containing TodoItem data

        Returns:
            TodoItem instance
        """
        return cls(
            title=data["title"],
            description=data.get("description"),
            completed=data.get("completed", False),
            todo_id=data.get("id"),
            created_at=data.get("created_at")
        )

    def __eq__(self, other) -> bool:
        """
        Check equality with another TodoItem.

        Args:
            other: Another TodoItem to compare with

        Returns:
            True if both TodoItems have the same ID, False otherwise
        """
        if not isinstance(other, TodoItem):
            return False
        return self.id == other.id

    def __repr__(self) -> str:
        """
        String representation of the TodoItem.

        Returns:
            String representation
        """
        status = "✓" if self.completed else "○"
        return f"TodoItem({status} {self.id[:8]}...: {self.title})"