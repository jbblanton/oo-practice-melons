import sys

############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, 
                is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = False
        self.is_bestseller = False
        


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        return self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        return self.code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk','Muskmelon', '1998', 'green', True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba',  '2003', 'orange', False, False)
    cas.add_pairing('mint')
    cas.add_pairing('strawberries')
    all_melon_types.append(cas)

    cren = MelonType('cren', 'Crenshaw',  '1996', 'green', False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon',  '2013', 'yellow', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types
    

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with') 
        for pair in melon.pairings:
            print(f'-{pair}')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_codes = {}

    for melon in melon_types:
        if melon.code not in melon_codes:
            melon_codes[melon.code] = melon

            # {'Name:': melon.name, 'Reporting Code:': 
            # melon.code, 'Color:': melon.color, 'First Harvest:': melon.first_harvest, 
            # 'Food Pairings:': melon.pairings, 'Is Seedless:': melon.is_seedless}

    return melon_codes



############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Initialize objects
    def __init__(self, m_type, shape, color_rating, harvest_field, harvested_by):

        self.type = m_type
        self.shape = shape
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvested_by = harvested_by

    # Determine if sellable or not (T/F)
    def is_sellable():

        if melon.harvest_field != 3:
            if melon.shape > 5 and melon.color_rating > 5:
                return True
        else:
            return False        


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_codes = make_melon_type_lookup(melon_types)
    harvested_melons = []

    melon_1 = Melon(melon_codes['yw'], 8, 7, 2, 'Sheila')
    harvested_melons.append(melon_1)
    melon_2 = Melon(melon_codes['yw'], 3, 4, 2, 'Sheila')
    harvested_melons.append(melon_2)
    melon_3 = Melon(melon_codes['yw'], 9, 8, 3, 'Sheila')
    harvested_melons.append(melon_3)
    melon_4 = Melon(melon_codes['cas'], 10, 6, 35, 'Sheila')
    harvested_melons.append(melon_4)
    melon_5 = Melon(melon_codes['cren'], 8, 9, 35, 'Michael')
    harvested_melons.append(melon_5)
    melon_6 = Melon(melon_codes['cren'], 8, 2, 35, 'Michael') 
    harvested_melons.append(melon_6)
    melon_7 = Melon(melon_codes['cren'], 2, 3, 4, 'Michael')
    harvested_melons.append(melon_7)
    melon_8 = Melon(melon_codes['musk'], 6, 7, 4, 'Michael')
    harvested_melons.append(melon_8)
    melon_9 = Melon(melon_codes['yw'], 7, 10, 3, 'Sheila')
    harvested_melons.append(melon_9)

    return harvested_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in harvested_melons:
        if melon.is_sellable():
            print(f'Harvested by {harvested_by} from Field {harvest_field} (CAN BE SOLD)')
        else:
            print(f'Harvested by {harvested_by} from Field {harvest_field} (DO NOT SELL)')    
        
