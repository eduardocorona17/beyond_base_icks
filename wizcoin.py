# Wizcoin
# Denominatons =  Knuts
# Sickles = 29 knuts
# Galleons = 17 sickles, or 493 jnuts

class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # Note:  __init__() methods never have a return statement.

    def value(self):
        """The value in knuts of all the coins in this WizCoin Object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)
    
    def weight_in_grams(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
    