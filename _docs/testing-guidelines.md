# Testing Guidelines

## Test Structure

Tests should be organized in the `tests/` directory, mirroring the application structure:
- `tests/test_models.py` - Database model tests
- `tests/test_routes.py` - Flask route tests
- `tests/test_ui.py` - UI/component tests

## Writing Tests

### Test Naming
- Use descriptive test names that explain what is being tested
- Follow the pattern: `test_<feature>_<scenario>_<expected_result>`
- Example: `test_card_creation_with_valid_data_succeeds`

### Test Structure
Each test should follow the Arrange-Act-Assert pattern:
```python
def test_example():
    # Arrange - Set up the test data and conditions
    card = Card(title="Test Card", priority="high")
    
    # Act - Perform the action being tested
    db.session.add(card)
    db.session.commit()
    
    # Assert - Verify the expected outcome
    assert Card.query.count() == 1
    assert Card.query.first().title == "Test Card"
```

### Database Tests
- Use fixtures for database setup/teardown
- Each test should start with a clean database state
- Test both positive and negative cases
- Test edge cases and boundary conditions

### Route Tests
- Test both successful and error responses
- Verify status codes
- Check response content/redirects
- Test form validation

### UI Tests
- Test client-side JavaScript behavior where applicable
- Verify correct CSS classes are applied
- Test search/filter functionality
- Check form rendering

## Test Coverage

- Aim for high coverage on core business logic
- Critical paths (CRUD operations) should have comprehensive tests
- UI rendering should have basic coverage
- Don't test trivial one-liners

## Running Tests

- Run all tests: `uv run pytest`
- Run specific file: `uv run pytest tests/test_models.py`
- Run with verbose output: `uv run pytest -v`
- Run with coverage: `uv run pytest --cov=app`

## Common Patterns

### Testing with Fixtures
```python
@pytest.fixture
def app():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
```

### Testing Routes
```python
def test_index_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Kanban Board' in response.data
```

### Testing Forms
```python
def test_create_card_with_valid_data(client):
    response = client.post('/card/create', data={
        'title': 'Test Card',
        'priority': 'high',
        'column_id': 1
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Card created successfully' in response.data
```

## When to Write Tests

- Write tests before implementing features (TDD) when possible
- At minimum, write tests alongside implementation
- Ensure tests pass before marking a task complete
- Update tests when changing behavior
