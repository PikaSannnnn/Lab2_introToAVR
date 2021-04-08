tests = [ {'description': 'All Open (0000)',
    'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 5 } ],
    'expected': [('PORTC', 4)],
    },
    {'description': '2 Open (0110)',
    'steps': [ {'inputs': [('PINA', 0x06)], 'iterations': 5 } ],
    'expected': [('PORTC', 2)],
    },
    {'description': '1 Opened (1011)',
    'steps': [ {'inputs': [('PINA',0x0B)], 'iterations': 5 } ],
    'expected': [('PORTC', 1)],
    },
    {'description': '3 Opened (0010)',
    'steps': [ {'inputs': [('PINA',0x02)], 'iterations': 5 } ],
    'expected': [('PORTC', 3)],
    },
    {'description': 'All Taken (1111)',
    'steps': [ {'inputs': [('PINA',0x0F)], 'iterations': 5 } ],
    'expected': [('PORTC', 0)],
    },
    {'description': 'TESTING FAIL: 0100 -> Correct: 1; Testing: 0',     # This test will get a fail on purpose
    'steps': [ {'inputs': [('PINA',0x04)], 'iterations': 5 } ],
    'expected': [('PORTC', 0)],
    },
    ]
#watch = ['PORTB']

