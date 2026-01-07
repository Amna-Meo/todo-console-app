# Data Model: Todo Console Application

## Todo Item Entity

### Attributes
- **id**: string (unique identifier, auto-generated)
- **title**: string (required, non-empty)
- **description**: string (optional, can be null/empty)
- **completed**: boolean (default: false)
- **created_at**: string (ISO 8601 timestamp, auto-generated)

### Validation Rules
- Title must not be empty or null
- ID must be unique within the todo list
- Completed status must be boolean
- Created_at must be valid ISO 8601 timestamp

### State Transitions
- New Todo Item: `completed = false` (default)
- Mark Complete: `completed = true`
- Mark Incomplete: `completed = false`

## Todo List Collection

### Attributes
- **items**: array of TodoItem objects
- **count**: integer (number of items in the list)

### Operations
- Add item to collection
- Remove item by ID
- Update item by ID
- Find item by ID
- List all items
- Filter by completion status

## Data Persistence Model

### File Structure (JSON)
```json
{
  "todos": [
    {
      "id": "unique-identifier",
      "title": "Todo title",
      "description": "Optional description",
      "completed": false,
      "created_at": "2026-01-07T10:30:00Z"
    }
  ]
}
```

### Validation for Persistence
- File must contain valid JSON
- Todos array must exist
- Each todo item must conform to Todo Item schema
- No duplicate IDs allowed