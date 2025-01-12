from flask import Blueprint, flash, render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Competitor, Product
from . import db
import json

views = Blueprint('views', __name__)

# Home Route (Existing)
@views.route("/", methods=['GET'])
@login_required
def home():
    return redirect(url_for('views.competitors'))


@views.route('/competitors', methods=['GET', 'POST'])
@login_required
def competitors():
    if request.method == 'POST':
        name = request.form.get('name')
        website = request.form.get('website')

        if len(name) < 1:
            flash('Competitor name is too short!', category='error')
        else:
            new_competitor = Competitor(name=name, website=website, user_id=current_user.id)
            db.session.add(new_competitor)
            db.session.commit()
            flash('Competitor added successfully!', category='success')

    competitors = Competitor.query.filter_by(user_id=current_user.id).all()
    return render_template('competitors.html', competitors=competitors)




# Delete Competitor Route (New)
@views.route('/delete-competitor/<int:id>', methods=['POST'])
@login_required
def delete_competitor(id):
    competitor = Competitor.query.get_or_404(id)
    
    if competitor.user_id != current_user.id:
        flash('You are not authorized to delete this competitor!', category='error')
        return redirect(url_for('views.competitors'))
    
    db.session.delete(competitor)
    db.session.commit()
    flash('Competitor deleted successfully!', category='success')
    return redirect(url_for('views.manage_competitors'))

@views.route('/competitors/<int:id>', methods=['GET', 'POST'])
@login_required
def competitor_detail(id):
    # Fetch the competitor
    competitor = Competitor.query.get_or_404(id)

    # Ensure the competitor belongs to the logged-in user
    if competitor.user_id != current_user.id:
        flash("You are not authorized to view this competitor's details!", category='error')
        return redirect(url_for('views.competitors'))

    # Fetch all products associated with this competitor
    products = Product.query.filter_by(competitor_id=competitor.id).all()
    return render_template('competitor_detail.html', competitor=competitor, products=products)




# Visualization route
@views.route('/visualize/<int:competitor_id>', methods=['GET'])
@login_required
def visualize_data(competitor_id):
    # Get the competitor
    competitor = Competitor.query.get_or_404(competitor_id)
    
    # Check if the competitor belongs to the logged-in user
    if competitor.user_id != current_user.id:
        flash("You are not authorized to view this data!", category='error')
        return redirect(url_for('views.home'))

    # Fetch products and their prices for this competitor
    products = Product.query.filter_by(competitor_id=competitor.id).all()
    product_data = [{"name": product.name, "price": product.price} for product in products]

    # Render the visualization template with data
    return render_template('visualize.html', competitor=competitor, product_data=product_data)

@views.route('/scrape/<int:competitor_id>', methods=['POST'])
@login_required
def scrape_data(competitor_id):
    # Placeholder logic for scraping
    flash("Scraping functionality is not implemented yet!", category="info")
    return redirect(url_for('views.home'))

