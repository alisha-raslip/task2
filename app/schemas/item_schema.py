def validate_item(data):
    errors = []
    if 'name' not in data or not isinstance(data['name'], str):
        errors.append("Field 'name' is required and must be a string.")
    if 'description' not in data or not isinstance(data['description'], str):
        errors.append("Field 'description' is required and must be a string.")
    return errors
