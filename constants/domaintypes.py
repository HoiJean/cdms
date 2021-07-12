class DomainTypes:
    # User types
    Username = "^[a-zA-Z][a-zA-Z0-9.'-_]+$"

    # Client types
    full_name = "^[a-z '-]+$"
    street_address = "^[-a-zA-Z0-9-()]+(\s+[-a-zA-Z-()]+)*$"
    house_number = "([0-9a-])\w+"
    zip_code = "^([0-9]{4}[a-z]{2})$"
    email = "^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$"
    phone_number = "^[0-9]{8}$"
