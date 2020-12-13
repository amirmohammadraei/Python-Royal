class Player:
    map = [
        ['0', '1', '2'],
        ['3', '4-C', '5'],
        ['6', '7', '8'],
    ]
    troops = []
    buildings = [
        {
            'place': 0,
            'building': None,
            'hp': None,
            'mhp': None
        },
        {
            'place': 1,
            'building': None,
            'hp': None,
            'mhp': None
        },
        {
            'place': 2,
            'building': None,
            'hp': None,
            'mhp': None
        },
        {
            'place': 3,
            'building': None,
            'hp': None,
            'mhp': None
        },
        {
            'place': 4,
            'building': 'C',
            'hp': 3000,
            'mhp': 3000
        },
        {
            'place': 5,
            'building': None,
            'hp': None,
            'mhp': None
        },
        {
            'place': 6,
            'building': None,
            'hp': None,
            'mhp': None
        },
        {
            'place': 7,
            'building': None,
            'hp': None,
            'mhp': None
        },
        {
            'place': 8,
            'building': None,
            'hp': None,
            'mhp': None
        },
    ]

    def __init__(self, nickname, money):
        self.nickname = nickname
        self.money = money

    def buildings_status(self, place, building):
        return 'salam'
