class DomainTypes:
    # User types
    Username = "^[a-zA-Z][a-zA-Z0-9.'-_]+$"
    password = "^[><?@+'`~^%&\*\[\]\{\}.!#|\\\"$';,:;=/\(\),\-\w\s+]+$"

    # Client types
    full_name = "^[a-z '-]+$"
    street_address = "^[-a-zA-Z0-9-()]+(\s+[-a-zA-Z-()]+)*$"
    house_number = "^([0-9])?([a-zA-Z0-9])+$"
    zip_code = "^([0-9]{4}[a-z]{2})$"
    email = "^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$"
    phone_number = "^[0-9]{8}$"
