class CustomerInfo:
    def __init__(self):
        self.id = None
        self.name = None
        self.telephone = None
        self.value = None
        self.address = None  # For storing the hashed address/index

def hash_id(id_number):
    """
    Returns the hash of the customer ID by taking (ID mod 1000).
    """
    return id_number % 1000

def validate_customer(customer):
    """
    Checks whether the customer's data meets the required constraints.
    Raises an Exception if invalid.
    """
    # Check ID range: 100001 <= ID <= 999999
    if customer.id < 100001 or customer.id > 999999:
        raise Exception("ID should be between 100001 and 999999.")

    # Name < 30 chars
    if len(customer.name) >= 30:
        raise Exception("Name should be less than 30 characters long.")

    # Telephone < 14 chars
    if len(customer.telephone) >= 14:
        raise Exception("Telephone should be less than 14 characters long.")

    # Value must be numeric (decimal). We can try converting to float:
    try:
        float(customer.value)
    except ValueError:
        raise Exception("Value should be a decimal (numeric) string.")

def add_record(id_number, name, telephone, value):
    """
    Creates a new customer record and stores it in the 'customers' array.
    Uses linear probing to handle collisions.
    """
    # Create a new customer object
    new_customer = CustomerInfo()
    new_customer.id = id_number
    new_customer.name = name
    new_customer.telephone = telephone
    new_customer.value = value

    # Validate the data
    validate_customer(new_customer)

    # Compute initial hash/index
    index = hash_id(id_number)

    # Linear probing in case of collision
    start_index = index
    for i in range(len(customers)):
        probe_index = (index + i) % len(customers)

        # If this slot is free (i.e. ID is None), place the record here
        if customers[probe_index].id is None:
            customers[probe_index] = new_customer
            customers[probe_index].address = probe_index
            print(f"Record added at index {probe_index}")
            return

    print("No space left in the hash table to add this record.")

def find_record(id_number):
    index = hash_id(id_number)

    for i in range(len(customers)):
        probe_index = (index + i) % len(customers)

        # If we hit an empty slot, the record does not exist
        if customers[probe_index].id is None:
            break

        # If we find a matching ID, return that record
        if customers[probe_index].id == id_number:
            return customers[probe_index]

    print("Customer not found.")
    return None

customers = [CustomerInfo() for _ in range(1000)]

add_record(100002, "Alice", "1234567", "200.50")
add_record(999999, "Bob", "987654321", "99.95")

# Find a record
record = find_record(100002)
if record:
    print(f"Found: {record.name} has orders worth {record.value}")

record = find_record(123456)  # Should not exist
