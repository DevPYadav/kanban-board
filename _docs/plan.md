# Kanban Board - Project Scope & Requirements

## Project Overview
A local web-based Kanban board tool for tracking TO DO items with swimlanes, columns, and card management.

## Technology Stack
- **Backend**: Python/Flask web application
- **Database**: SQLite (lightweight, built into Python)
- **Frontend**: HTML templates with CSS and vanilla JavaScript
- **Storage**: Local SQLite database file (`kanban.db`)

## Core Features

### 1. Board Structure
- **Swimlanes**: Horizontal groupings for organizing work by priority or category
  - Default swimlanes: High Priority, Medium Priority, Low Priority
  - Fully customizable: create, edit, delete swimlanes
  - Orderable swimlanes
- **Columns**: Vertical status columns within each swimlane
  - Default columns per swimlane: To Do, In Progress, Done
  - Fully customizable: create, edit, delete columns
  - Orderable columns within swimlanes

### 2. Card Management
Each card/task includes:
- **Title** (required)
- **Description** (optional)
- **Status** (determined by column assignment)
- **Due Date** (optional)
- **Priority Level** (low, medium, high)
- **Tags/Labels** (comma-separated, optional)
- **Creation and update timestamps**

**Card Operations:**
- Create new cards
- Edit existing cards
- Delete cards
- Move cards between columns (including across swimlanes)

### 3. User Interface
- Clean, responsive web interface
- Color-coded priority indicators (red for high, orange for medium, green for low)
- Visual distinction between swimlanes and columns
- Search/filter functionality for cards
- Flash notifications for user feedback

### 4. Data Persistence
- All data stored in SQLite database
- Automatic database initialization with default structure
- Data persists across application restarts

## Implementation Details

### Database Schema

**Swimlane Table:**
- `id` (primary key)
- `name` (string, required)
- `order` (integer, for sorting)

**Column Table:**
- `id` (primary key)
- `name` (string, required)
- `order` (integer, for sorting)
- `swimlane_id` (foreign key to Swimlane)

**Card Table:**
- `id` (primary key)
- `title` (string, required)
- `description` (text, optional)
- `due_date` (date, optional)
- `priority` (string: low/medium/high)
- `tags` (string, comma-separated)
- `column_id` (foreign key to Column)
- `order` (integer, for sorting)
- `created_at` (datetime)
- `updated_at` (datetime)

### File Structure
```
kanban-board/
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
├── kanban.db                       # SQLite database (auto-generated)
├── plan.md                         # This file
├── templates/                      # HTML templates
│   ├── base.html                  # Base layout template
│   ├── index.html                 # Main board view
│   ├── card_form.html             # Card create/edit form
│   ├── swimlane_form.html         # Swimlane create/edit form
│   └── column_form.html           # Column create/edit form
└── static/
    ├── css/
    │   └── style.css              # Application styling
    └── js/
        └── script.js              # Client-side JavaScript
```

### API Routes

**Board & Navigation:**
- `GET /` - Main board view

**Card Operations:**
- `GET /card/create` - Display card creation form
- `POST /card/create` - Create new card
- `GET /card/<id>/edit` - Display card edit form
- `POST /card/<id>/edit` - Update card
- `POST /card/<id>/delete` - Delete card
- `POST /card/<id>/move` - Move card to different column

**Swimlane Operations:**
- `GET /swimlane/create` - Display swimlane creation form
- `POST /swimlane/create` - Create new swimlane
- `GET /swimlane/<id>/edit` - Display swimlane edit form
- `POST /swimlane/<id>/edit` - Update swimlane
- `POST /swimlane/<id>/delete` - Delete swimlane

**Column Operations:**
- `GET /column/create` - Display column creation form
- `POST /column/create` - Create new column
- `GET /column/<id>/edit` - Display column edit form
- `POST /column/<id>/edit` - Update column
- `POST /column/<id>/delete` - Delete column

## Future Enhancements (Not Implemented)

### Phase 2 - Drag and Drop
- Implement drag-and-drop functionality for moving cards between columns
- Visual feedback during drag operations
- Smooth animations

### Phase 3 - Advanced Features
- Card attachments (file uploads)
- Comments/discussion threads on cards
- Card history/audit log
- Export board to PDF/JSON
- Import cards from CSV/JSON
- Keyboard shortcuts
- Dark mode theme

### Phase 4 - Collaboration
- Multiple user support
- User authentication
- Permission system
- Real-time updates via WebSockets

## How to Run

### Prerequisites
- Python 3.x installed
- pip package manager

### Installation
```bash
cd kanban-board
pip install -r requirements.txt
```

### Running the Application
```bash
python3 app.py
```

The application will be available at: http://127.0.0.1:5000

### Stopping the Application
Press `CTRL+C` in the terminal where the server is running.

## Notes
- This is a development server using Flask's built-in server
- For production use, consider using a WSGI server like Gunicorn
- The SECRET_KEY in `app.py` should be changed for production deployments
- Database file (`kanban.db`) is created automatically on first run
- Default swimlanes and columns are created if the database is empty
