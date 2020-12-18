class Player:
    def __init__(self, nickname, money):
        self.map = [
            ['0', '1', '2'],
            ['3', '4-C', '5'],
            ['6', '7', '8'],
        ]

        self.troops = [
            {
                'code': 'S',
                'count': 0,
                'HP': 10,
                'Damage': 10,
            },
            {
                'code': 'T',
                'count': 0,
                'HP': 100,
                'Damage': 100,
            },
            {
                'code': 'F',
                'count': 0,
                'HP': 50,
                'Damage': 250,
            }
        ]
        self.buildings = [
            {
                'place': '0',
                'building': None,
                'hp': None,
                'mhp': None,
                'damage': None
            },
            {
                'place': '1',
                'building': None,
                'hp': None,
                'mhp': None,
                'damage': None
            },
            {
                'place': '2',
                'building': None,
                'hp': None,
                'mhp': None,
                'damage': None
            },
            {
                'place': '3',
                'building': None,
                'hp': None,
                'mhp': None,
                'damage': None
            },
            {
                'place': '4',
                'building': 'C',
                'hp': 3000,
                'mhp': 3000,
                'damage': None
            },
            {
                'place': '5',
                'building': None,
                'hp': None,
                'mhp': None,
                'damage': None
            },
            {
                'place': '6',
                'building': None,
                'hp': None,
                'mhp': None,
                'damage': None
            },
            {
                'place': '7',
                'building': None,
                'hp': None,
                'mhp': None,
                'damage': None
            },
            {
                'place': '8',
                'building': None,
                'hp': None,
                'mhp': None,
                'damage': None
            },
        ]
        self.nickname = nickname
        self.money = money
