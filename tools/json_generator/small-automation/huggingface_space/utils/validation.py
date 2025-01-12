from config import OBLIGATORY_FIELDS

def validate_obligatory_fields(data):
    """Validate that all required fields are present in the data."""
    def find_field(d, field):
        if field in d:
            return d[field]
        for k, v in d.items():
            if isinstance(v, dict):
                result = find_field(v, field)
                if result is not None:
                    return result
            elif isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        result = find_field(item, field)
                        if result is not None:
                            return result
        return None
    
    missing_fields = []
    for field in OBLIGATORY_FIELDS:
        value = find_field(data, field)
        if not value and value != 0:  # Allow 0 as a valid value
            missing_fields.append(field)
            
    if missing_fields:
        return False, f"The following fields are required: {', '.join(missing_fields)}"
    return True, "All required fields are filled."