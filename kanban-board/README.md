# Kanban Board

A local web-based Kanban board tool for tracking TO DO items with swimlanes, columns, and card management.

## Features

- Create and manage swimlanes for organizing work by priority or category
- Create and manage columns within swimlanes (e.g., To Do, In Progress, Done)
- Create and manage cards with title, description, due date, priority, and tags
- Move cards between columns and swimlanes
- Search and filter cards by title, description, or tags
- Color-coded priority indicators (high, medium, low)
- Persistent data storage using SQLite

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Navigate to the kanban-board directory:
```bash
cd kanban-board
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask development server:
```bash
python3 app.py
```

The application will be available at: http://127.0.0.1:5000

To stop the server, press `CTRL+C` in the terminal.

## Usage

### Creating Swimlanes

1. Click the "+ Add Swimlane" button at the bottom of the board
2. Enter a name for the swimlane (e.g., "High Priority")
3. Optionally set the display order
4. Click "Create Swimlane"

### Creating Columns

1. Click the "+ Add Column" button within a swimlane
2. Enter a name for the column (e.g., "To Do")
3. Select the parent swimlane
4. Optionally set the display order within the swimlane
5. Click "Create Column"

### Creating Cards

1. Click the "+ Add Card" button within a column
2. Enter a title for the card (required)
3. Optionally add a description
4. Select the column where the card should be placed
5. Optionally set a due date
6. Select a priority level (low, medium, high)
7. Optionally add tags (comma-separated)
8. Click "Create Card"

### Moving Cards

1. Find the card you want to move
2. Use the dropdown menu on the card to select the destination column
3. The card will automatically move to the selected column

### Editing and Deleting

- **Edit**: Click the "Edit" link on any swimlane, column, or card to modify it
- **Delete**: Click the "Delete" button on any swimlane, column, or card to remove it (confirmation required)

### Searching

Use the search bar at the top of the board to filter cards by title, description, or tags in real-time.

## Default Data

On first run, the application automatically creates:
- 3 swimlanes: High Priority, Medium Priority, Low Priority
- 3 columns per swimlane: To Do, In Progress, Done

## Development

For information about the development process and team roles, see the `_docs/` directory in the project root.

## License

This project is open source and available for local use.
