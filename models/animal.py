class Animal():

    def __init__(self, id, name, species, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.species = species
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id
        self.location = None
        self.customer = None