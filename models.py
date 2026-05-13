class Transaction:
    """
    Represents a single financial transaction.

    Stores details about a transaction including amount,
    category, and type (earnings or expense). Provides a
    method to convert the object into a dictionary for saving.
    """
    
    def __init__(self, amount, category, t_type):
        self.amount = amount
        self.category = category
        self.type = t_type

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "type": self.type
        }