# Kanban Board - Task Backlog

## 1. Project Setup with Passing Test
Goal: Set up an empty Flask project with a basic passing test
Description: Initialize a Flask project structure with app.py, requirements.txt, and a simple test file that verifies the Flask app can be imported and instantiated. This establishes the project foundation and testing infrastructure.

## 2. Database Models
Goal: Define and create the database models for swimlanes, columns, and cards
Description: Create SQLAlchemy models for Swimlane, Column, and Card with appropriate fields, relationships, and constraints. Write a test to verify the models can be created and relationships work correctly.

## 3. Database Initialization
Goal: Create a function to initialize the database with default swimlanes and columns
Description: Implement an initialization function that creates the database tables and populates them with default swimlanes (High/Medium/Low Priority) and columns (To Do/In Progress/Done). Write a test to verify default data is created correctly.

## 4. Basic Flask Routes
Goal: Create basic Flask routes for the index page and navigation
Description: Implement the root route that renders a base template and simple navigation menu. Set up the template structure with base.html and a simple index.html. Write a test to verify the index page loads successfully.

## 5. Swimlane CRUD Operations
Goal: Implement create, read, update, and delete operations for swimlanes
Description: Create Flask routes and HTML forms for creating, editing, and deleting swimlanes. Ensure proper validation and database operations. Write tests for each CRUD operation.

## 6. Column CRUD Operations
Goal: Implement create, read, update, and delete operations for columns
Description: Create Flask routes and HTML forms for creating, editing, and deleting columns within swimlanes. Ensure proper validation and database operations. Write tests for each CRUD operation.

## 7. Card CRUD Operations
Goal: Implement create, read, update, and delete operations for cards
Description: Create Flask routes and HTML forms for creating, editing, and deleting cards. Include fields for title, description, due date, priority, and tags. Write tests for each CRUD operation.

## 8. Board View with Swimlanes and Columns
Goal: Render the main Kanban board showing all swimlanes and their columns
Description: Update the index route to query all swimlanes and their associated columns, then render them in a board layout template. Write a test to verify the board displays the correct structure.

## 9. Card Display on Board
Goal: Display cards within their respective columns on the board
Description: Update the board view to query and display cards within each column, showing title, description, priority, due date, and tags. Write a test to verify cards appear in the correct columns.

## 10. Card Movement Between Columns
Goal: Implement the ability to move cards between columns via dropdown selection
Description: Add a dropdown form on each card that allows moving it to any column in any swimlane. Implement the backend route to handle the move operation. Write a test to verify cards can be moved successfully.

## 11. Card Form Enhancements
Goal: Enhance the card form with date picker, priority selector, and tags input
Description: Improve the card creation/edit form with proper input types (date picker for due date, select for priority, text input for tags). Ensure proper validation and data formatting. Write tests for form submission with various inputs.

## 12. Search and Filter Functionality
Goal: Implement client-side search/filter for cards
Description: Add a search input field and JavaScript function to filter cards by title, description, or tags in real-time. Write a test to verify the search functionality works correctly.

## 13. CSS Styling for Board Layout
Goal: Apply CSS styling to create a visually appealing Kanban board layout
Description: Create a CSS file with styles for swimlanes, columns, cards, priority indicators, and responsive layout. Ensure the board is readable and well-organized. Visually verify the styling looks correct.

## 14. Priority Color Coding
Goal: Implement visual color coding for card priority levels
Description: Add CSS classes and styles to visually distinguish high, medium, and low priority cards (e.g., colored borders or badges). Write a test to verify the correct CSS classes are applied based on priority.

## 15. Flash Messages
Goal: Implement flash messages for user feedback on successful operations
Description: Set up Flask flash messaging and create CSS styles for success messages. Display flash messages after create, update, delete, and move operations. Write tests to verify messages appear correctly.

## 16. Swimlane and Column Forms
Goal: Create forms for managing swimlanes and columns
Description: Build HTML forms for creating and editing swimlanes and columns with proper validation. Ensure forms include all necessary fields and provide clear user feedback. Write tests for form submissions.

## 17. Delete Confirmation
Goal: Add confirmation dialogs for destructive operations
Description: Implement JavaScript confirmation dialogs before deleting swimlanes, columns, or cards. Ensure users can cancel the operation. Visually test the confirmation flow.

## 18. Order Management
Goal: Implement ordering fields for swimlanes, columns, and cards
Description: Add order fields to all models and forms to control display order. Update queries to sort by order field. Write tests to verify items display in the correct order.

## 19. Tags Display
Goal: Improve the display of tags on cards
Description: Add CSS styling to display tags as small badges with proper spacing and colors. Ensure tags are parsed correctly from comma-separated strings. Visually verify tag display looks good.

## 20. Responsive Design
Goal: Make the Kanban board responsive for different screen sizes
Description: Add CSS media queries to ensure the board layout works well on mobile, tablet, and desktop screens. Test the board at various screen sizes and orientations.

## 21. Auto-hide Flash Messages
Goal: Automatically hide flash messages after a set time
Description: Add JavaScript to automatically hide flash messages after 5 seconds. Write a test to verify messages disappear automatically.

## 22. Empty State Handling
Goal: Display appropriate messages when boards or columns are empty
Description: Add conditional rendering to show "No cards" or "No columns" messages when appropriate. Write tests to verify empty states display correctly.

## 23. Due Date Formatting
Goal: Ensure due dates are displayed in a consistent, readable format
Description: Format due dates consistently across the application (e.g., YYYY-MM-DD). Handle null due dates gracefully. Write tests to verify date formatting.

## 24. Form Validation
Goal: Add client-side and server-side validation for all forms
Description: Implement HTML5 validation attributes and Flask-WTF validation for required fields, date formats, and data constraints. Write tests to verify validation catches invalid inputs.

## 25. README Documentation
Goal: Create comprehensive README with setup and usage instructions
Description: Write a README.md file with project description, installation steps, how to run the application, and basic usage guide. Ensure a new developer can set up and run the project from the README alone.
