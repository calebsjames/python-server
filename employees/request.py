EMPLOYEES = [
    {
      "id": 1,
      "name": "Jack Johnson",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "John Jackson",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Daniel Jameson",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "James Danielson",
      "locationId": 2
    },
    {
      "name": "Some Dude",
      "locationId": 1,
      "id": 5
    }
]


def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee