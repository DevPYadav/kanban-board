# Design System

## Color Palette

### Primary Colors
- Background: `#f5f5f5` (light gray)
- White: `#ffffff` (cards, forms)
- Header: `#2c3e50` (dark blue-gray)
- Header hover: `#34495e`

### Accent Colors
- Primary action: `#3498db` (blue)
- Primary hover: `#2980b9`
- Secondary action: `#95a5a6` (gray)
- Secondary hover: `#7f8c8d`

### Priority Colors
- High priority: `#e74c3c` (red) - borders, badges
- Medium priority: `#f39c12` (orange) - borders, badges
- Low priority: `#27ae60` (green) - borders, badges

### Status Colors
- Success: `#d4edda` (background), `#155724` (text)
- Error: `#f8d7da` (background), `#721c24` (text)

### Neutral Colors
- Text primary: `#333333`
- Text secondary: `#7f8c8d`
- Border: `#dddddd`
- Card background: `#f8f9fa`

## Typography

### Font Family
Base font: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif`

### Font Sizes
- Header (h1): 1.5rem
- Section header (h2): 1.25rem
- Subsection header (h3): 1rem
- Card title (h4): 0.95rem
- Body text: 0.875rem
- Small text: 0.75rem

### Font Weights
- Headers: normal (400)
- Form labels: 500
- Priority badges: 500

## Spacing

### Padding
- Header: 1rem 2rem
- Main content: 2rem
- Swimlane: 1.5rem
- Column: 1rem
- Card: 1rem
- Form inputs: 0.75rem

### Margins
- Between swimlanes: 2rem
- Between columns: 1rem
- Between cards: 0.75rem
- Form groups: 1.25rem

### Gaps
- Swimlane gap: 2rem
- Column gap: 1rem
- Card gap: 0.75rem
- Tag gap: 0.25rem

## Components

### Buttons
- Primary button: Blue background, white text, rounded corners (4px)
- Secondary button: Gray background, white text, rounded corners (4px)
- Hover state: Darker shade of base color
- Padding: 0.75rem 1.5rem
- Font weight: 500

### Forms
- Input fields: White background, 1px border (#ddd), rounded corners (4px)
- Input padding: 0.75rem
- Label spacing: 0.5rem below label
- Textarea: resize vertical only

### Cards
- Background: White
- Border radius: 4px
- Box shadow: 0 1px 3px rgba(0,0,0,0.1)
- Left border: 4px (color indicates priority)
- Padding: 1rem

### Swimlanes
- Background: White
- Border radius: 8px
- Box shadow: 0 2px 4px rgba(0,0,0,0.1)
- Padding: 1.5rem
- Bottom border: 2px solid #ecf0f1

### Columns
- Background: #f8f9fa
- Border radius: 6px
- Padding: 1rem
- Min-width: 300px

### Tags
- Background: #ecf0f1
- Text color: #34495e
- Border radius: 4px
- Padding: 0.25rem 0.5rem
- Font size: 0.75rem

### Priority Badges
- Border radius: 12px (pill shape)
- Padding: 0.25rem 0.5rem
- Text transform: uppercase
- Font weight: 500
- Font size: 0.75rem

### Flash Messages
- Success: Green background (#d4edda), dark green text (#155724)
- Padding: 0.75rem
- Border radius: 4px
- Auto-hide after 5 seconds

## Layout

### Board Layout
- Flexbox-based column layout
- Horizontal scrolling for columns within swimlanes
- Responsive design with media queries

### Form Layout
- Max width: 600px
- Centered on page
- White background
- Rounded corners (8px)
- Box shadow: 0 2px 4px rgba(0,0,0,0.1)

### Responsive Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

## Interactions

### Hover States
- Navigation links: Darker background
- Buttons: Darker shade
- Add buttons: Darker background (#bdc3c7)

### Transitions
- Background color: 0.2s ease
- All interactive elements should have transition effects

### Forms
- Validation: HTML5 attributes + server-side validation
- Required fields: Marked with asterisk (*)
- Submit buttons: Cursor pointer

## Accessibility

### Color Contrast
- Ensure text meets WCAG AA standards for contrast
- Priority colors should be distinguishable from background

### Keyboard Navigation
- All interactive elements should be keyboard accessible
- Form fields should have proper labels
- Focus states should be visible

### Semantic HTML
- Use proper heading hierarchy (h1, h2, h3, h4)
- Use semantic elements (header, main, nav, form)
- Forms should have proper label associations

## Icons and Graphics

### Icons
- Use text-based indicators (× for delete, + for add)
- No external icon libraries (keep it lightweight)

### Graphics
- No images or graphics required
- CSS-based styling only
