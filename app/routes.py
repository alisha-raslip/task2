from flask import Blueprint, request, jsonify
from app.models.item import Item
from app.schemas.item_schema import validate_item

bp = Blueprint('routes', __name__)

# In-memory data storage
items = []

@bp.route('/items', methods=['GET'])
def get_items():
    return jsonify([item.to_dict() for item in items]), 200

@bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item.id == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item.to_dict()), 200

@bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    errors = validate_item(data)
    if errors:
        return jsonify({"errors": errors}), 400

    new_item = Item(item_id=len(items) + 1, name=data['name'], description=data['description'])
    items.append(new_item)
    return jsonify(new_item.to_dict()), 201

@bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item.id == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    errors = validate_item(data)
    if errors:
        return jsonify({"errors": errors}), 400

    item.name = data['name']
    item.description = data['description']
    return jsonify(item.to_dict()), 200

@bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item.id != item_id]
    return jsonify({"message": "Item deleted"}), 200
