# API Documentation

## Base URL
All routes are relative to the application root (e.g., `http://127.0.0.1:5000`)

## Board & Navigation

### GET /
Display the main Kanban board with all swimlanes, columns, and cards.

**Response:** HTML page with board layout

---

## Card Operations

### GET /card/create
Display the card creation form.

**Response:** HTML form for creating a card

### POST /card/create
Create a new card.

**Form Data:**
- `title` (required): Card title (string, max 200 chars)
- `description` (optional): Card description (text)
- `column_id` (required): ID of the column to place the card in (integer)
- `due_date` (optional): Due date in YYYY-MM-DD format (date)
- `priority` (optional): Priority level - "low", "medium", or "high" (string, default: "medium")
- `tags` (optional): Comma-separated tags (string)

**Response:** Redirect to index page with flash message

### GET /card/<card_id>/edit
Display the card edit form for a specific card.

**Path Parameters:**
- `card_id`: Card ID (integer)

**Response:** HTML form pre-populated with card data

### POST /card/<card_id>/edit
Update an existing card.

**Path Parameters:**
- `card_id`: Card ID (integer)

**Form Data:** Same as POST /card/create

**Response:** Redirect to index page with flash message

### POST /card/<card_id>/delete
Delete a card.

**Path Parameters:**
- `card_id`: Card ID (integer)

**Response:** Redirect to index page with flash message

### POST /card/<card_id>/move
Move a card to a different column.

**Path Parameters:**
- `card_id`: Card ID (integer)

**Form Data:**
- `column_id` (required): ID of the destination column (integer)

**Response:** Redirect to index page with flash message

---

## Swimlane Operations

### GET /swimlane/create
Display the swimlane creation form.

**Response:** HTML form for creating a swimlane

### POST /swimlane/create
Create a new swimlane.

**Form Data:**
- `name` (required): Swimlane name (string, max 100 chars)
- `order` (optional): Display order (integer, default: 0)

**Response:** Redirect to index page with flash message

### GET /swimlane/<swimlane_id>/edit
Display the swimlane edit form.

**Path Parameters:**
- `swimlane_id`: Swimlane ID (integer)

**Response:** HTML form pre-populated with swimlane data

### POST /swimlane/<swimlane_id>/edit
Update an existing swimlane.

**Path Parameters:**
- `swimlane_id`: Swimlane ID (integer)

**Form Data:** Same as POST /swimlane/create

**Response:** Redirect to index page with flash message

### POST /swimlane/<swimlane_id>/delete
Delete a swimlane and all its columns and cards.

**Path Parameters:**
- `swimlane_id`: Swimlane ID (integer)

**Response:** Redirect to index page with flash message

---

## Column Operations

### GET /column/create
Display the column creation form.

**Response:** HTML form for creating a column

### POST /column/create
Create a new column.

**Form Data:**
- `name` (required): Column name (string, max 100 chars)
- `swimlane_id` (required): ID of the parent swimlane (integer)
- `order` (optional): Display order within swimlane (integer, default: 0)

**Response:** Redirect to index page with flash message

### GET /column/<column_id>/edit
Display the column edit form.

**Path Parameters:**
- `column_id`: Column ID (integer)

**Response:** HTML form pre-populated with column data

### POST /column/<column_id>/edit
Update an existing column.

**Path Parameters:**
- `column_id`: Column ID (integer)

**Form Data:** Same as POST /column/create

**Response:** Redirect to index page with flash message

### POST /column/<column_id>/delete
Delete a column and all its cards.

**Path Parameters:**
- `column_id`: Column ID (integer)

**Response:** Redirect to index page with flash message

---

## Database Models

### Swimlane
- `id`: Primary key (integer)
- `name`: Swimlane name (string, 100 chars, required)
- `order`: Display order (integer, default: 0)
- `columns`: Relationship to Column model (one-to-many)

### Column
- `id`: Primary key (integer)
- `name`: Column name (string, 100 chars, required)
- `order`: Display order within swimlane (integer, default: 0)
- `swimlane_id`: Foreign key to Swimlane (integer, required)
- `swimlane`: Relationship to Swimlane model (many-to-one)
- `cards`: Relationship to Card model (one-to-many)

### Card
- `id`: Primary key (integer)
- `title`: Card title (string, 200 chars, required)
- `description`: Card description (text, optional)
- `due_date`: Due date (date, optional)
- `priority`: Priority level (string, 20 chars, default: "medium")
- `tags`: Comma-separated tags (string, 500 chars, optional)
- `column_id`: Foreign key to Column (integer, required)
- `column`: Relationship to Column model (many-to-one)
- `order`: Display order within column (integer, default: 0)
- `created_at`: Creation timestamp (datetime, auto-generated)
- `updated_at`: Last update timestamp (datetime, auto-updated)

---

## Response Codes

- `200 OK`: Successful GET request
- `302 Found`: Redirect after POST request
- `404 Not Found`: Resource not found (invalid ID)

---

## Flash Messages

All POST operations that modify data return flash messages:

- **Success:** "Card created successfully!", "Card updated successfully!", "Card deleted successfully!", "Card moved successfully!", "Swimlane created successfully!", "Swimlane updated successfully!", "Swimlane deleted successfully!", "Column created successfully!", "Column updated successfully!", "Column deleted successfully!"

Flash messages are displayed at the top of the page and auto-hide after 5 seconds.

---

## Default Data

On first run, the database is initialized with:

**Swimlanes:**
1. High Priority (order: 0)
2. Medium Priority (order: 1)
3. Low Priority (order: 2)

**Columns (per swimlane):**
1. To Do (order: 0)
2. In Progress (order: 1)
3. Done (order: 2)
