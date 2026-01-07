# API Contracts: Todo Console Application

## CLI Command Contracts

### Add Todo Command
```
Command: add [title] [description?]
Input:
  - title: string (required, non-empty)
  - description: string (optional)

Output:
  - Success: "Todo added successfully with ID: {id}"
  - Error: "Error: {error message}"

Business Logic:
  - Creates a new TodoItem with provided title and description
  - Sets completed status to false by default
  - Generates unique ID
  - Saves to persistent storage
  - Returns success message with assigned ID
```

### List Todos Command
```
Command: list
Input: None

Output:
  - Success: Formatted list of all todos with ID, title, status, and description
  - Error: "Error: {error message}"

Business Logic:
  - Retrieves all todos from storage
  - Formats for display with clear status indicators
  - Shows appropriate message if no todos exist
```

### Complete/Incomplete Todo Command
```
Command: complete [id] | incomplete [id]
Input:
  - id: string/number (required, valid todo ID)

Output:
  - Success: "Todo {id} marked as {complete/incomplete}"
  - Error: "Error: {error message}"

Business Logic:
  - Finds todo by ID
  - Updates completion status
  - Saves to persistent storage
  - Returns status update confirmation
```

### Update Todo Command
```
Command: update [id] [title?] [description?]
Input:
  - id: string/number (required, valid todo ID)
  - title: string (optional, if provided updates title)
  - description: string (optional, if provided updates description)

Output:
  - Success: "Todo {id} updated successfully"
  - Error: "Error: {error message}"

Business Logic:
  - Finds todo by ID
  - Updates specified fields (title and/or description)
  - Saves to persistent storage
  - Returns update confirmation
```

### Delete Todo Command
```
Command: delete [id]
Input:
  - id: string/number (required, valid todo ID)

Output:
  - Success: "Todo {id} deleted successfully"
  - Error: "Error: {error message}"

Business Logic:
  - Finds and removes todo by ID
  - Updates persistent storage
  - Returns deletion confirmation
```

## Data Contracts

### Todo Item JSON Schema
```json
{
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "title": {"type": "string", "minLength": 1},
    "description": {"type": "string"},
    "completed": {"type": "boolean"},
    "created_at": {"type": "string", "format": "date-time"}
  },
  "required": ["id", "title", "completed", "created_at"]
}
```

### Todo List JSON Schema
```json
{
  "type": "object",
  "properties": {
    "todos": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/TodoItem"
      }
    }
  },
  "definitions": {
    "TodoItem": {
      "$ref": "#/TodoItemJSONSchema"
    }
  }
}
```