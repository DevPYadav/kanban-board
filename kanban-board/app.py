from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Swimlane(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    order = db.Column(db.Integer, default=0)
    columns = db.relationship('Column', backref='swimlane', lazy=True, cascade='all, delete-orphan')

class Column(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    order = db.Column(db.Integer, default=0)
    swimlane_id = db.Column(db.Integer, db.ForeignKey('swimlane.id'), nullable=False)
    cards = db.relationship('Card', backref='column', lazy=True, cascade='all, delete-orphan')

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.Date, nullable=True)
    priority = db.Column(db.String(20), default='medium')  # low, medium, high
    tags = db.Column(db.String(500), nullable=True)  # comma-separated tags
    column_id = db.Column(db.Integer, db.ForeignKey('column.id'), nullable=False)
    order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Routes
@app.route('/')
def index():
    swimlanes = Swimlane.query.order_by(Swimlane.order).all()
    return render_template('index.html', swimlanes=swimlanes)

@app.route('/card/create', methods=['GET', 'POST'])
def create_card():
    if request.method == 'POST':
        card = Card(
            title=request.form['title'],
            description=request.form.get('description', ''),
            due_date=datetime.strptime(request.form['due_date'], '%Y-%m-%d').date() if request.form.get('due_date') else None,
            priority=request.form.get('priority', 'medium'),
            tags=request.form.get('tags', ''),
            column_id=request.form['column_id']
        )
        db.session.add(card)
        db.session.commit()
        flash('Card created successfully!', 'success')
        return redirect(url_for('index'))
    
    columns = Column.query.order_by(Column.swimlane_id, Column.order).all()
    return render_template('card_form.html', columns=columns, action='Create')

@app.route('/card/<int:card_id>/edit', methods=['GET', 'POST'])
def edit_card(card_id):
    card = Card.query.get_or_404(card_id)
    
    if request.method == 'POST':
        card.title = request.form['title']
        card.description = request.form.get('description', '')
        card.due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d').date() if request.form.get('due_date') else None
        card.priority = request.form.get('priority', 'medium')
        card.tags = request.form.get('tags', '')
        card.column_id = request.form['column_id']
        db.session.commit()
        flash('Card updated successfully!', 'success')
        return redirect(url_for('index'))
    
    columns = Column.query.order_by(Column.swimlane_id, Column.order).all()
    return render_template('card_form.html', card=card, columns=columns, action='Edit')

@app.route('/card/<int:card_id>/delete', methods=['POST'])
def delete_card(card_id):
    card = Card.query.get_or_404(card_id)
    db.session.delete(card)
    db.session.commit()
    flash('Card deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/card/<int:card_id>/move', methods=['POST'])
def move_card(card_id):
    card = Card.query.get_or_404(card_id)
    card.column_id = request.form['column_id']
    db.session.commit()
    flash('Card moved successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/swimlane/create', methods=['GET', 'POST'])
def create_swimlane():
    if request.method == 'POST':
        swimlane = Swimlane(
            name=request.form['name'],
            order=request.form.get('order', 0)
        )
        db.session.add(swimlane)
        db.session.commit()
        flash('Swimlane created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('swimlane_form.html', action='Create')

@app.route('/swimlane/<int:swimlane_id>/edit', methods=['GET', 'POST'])
def edit_swimlane(swimlane_id):
    swimlane = Swimlane.query.get_or_404(swimlane_id)
    
    if request.method == 'POST':
        swimlane.name = request.form['name']
        swimlane.order = request.form.get('order', swimlane.order)
        db.session.commit()
        flash('Swimlane updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('swimlane_form.html', swimlane=swimlane, action='Edit')

@app.route('/swimlane/<int:swimlane_id>/delete', methods=['POST'])
def delete_swimlane(swimlane_id):
    swimlane = Swimlane.query.get_or_404(swimlane_id)
    db.session.delete(swimlane)
    db.session.commit()
    flash('Swimlane deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/column/create', methods=['GET', 'POST'])
def create_column():
    if request.method == 'POST':
        column = Column(
            name=request.form['name'],
            swimlane_id=request.form['swimlane_id'],
            order=request.form.get('order', 0)
        )
        db.session.add(column)
        db.session.commit()
        flash('Column created successfully!', 'success')
        return redirect(url_for('index'))
    
    swimlanes = Swimlane.query.order_by(Swimlane.order).all()
    return render_template('column_form.html', swimlanes=swimlanes, action='Create')

@app.route('/column/<int:column_id>/edit', methods=['GET', 'POST'])
def edit_column(column_id):
    column = Column.query.get_or_404(column_id)
    
    if request.method == 'POST':
        column.name = request.form['name']
        column.swimlane_id = request.form['swimlane_id']
        column.order = request.form.get('order', column.order)
        db.session.commit()
        flash('Column updated successfully!', 'success')
        return redirect(url_for('index'))
    
    swimlanes = Swimlane.query.order_by(Swimlane.order).all()
    return render_template('column_form.html', column=column, swimlanes=swimlanes, action='Edit')

@app.route('/column/<int:column_id>/delete', methods=['POST'])
def delete_column(column_id):
    column = Column.query.get_or_404(column_id)
    db.session.delete(column)
    db.session.commit()
    flash('Column deleted successfully!', 'success')
    return redirect(url_for('index'))

def init_db():
    with app.app_context():
        db.create_all()
        
        # Create default swimlanes if none exist
        if Swimlane.query.count() == 0:
            swimlanes = [
                Swimlane(name='High Priority', order=0),
                Swimlane(name='Medium Priority', order=1),
                Swimlane(name='Low Priority', order=2)
            ]
            db.session.add_all(swimlanes)
            db.session.commit()
            
            # Create default columns for each swimlane
            for swimlane in swimlanes:
                columns = [
                    Column(name='To Do', swimlane_id=swimlane.id, order=0),
                    Column(name='In Progress', swimlane_id=swimlane.id, order=1),
                    Column(name='Done', swimlane_id=swimlane.id, order=2)
                ]
                db.session.add_all(columns)
            db.session.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
