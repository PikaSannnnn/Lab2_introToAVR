tests = [ {'description': 'Good Weight, Good Balance [20, 30, 20] (70 kg)',
    'steps': [ {'inputs': [('PINA',20), ('PINB',30), ('PINC',20)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x44)],  # 0100 0100
    },
    {'description': 'Good Weight, Bad Balance A-C [100, 10, 10] (120 kg)',
    'steps': [ {'inputs': [('PINA',100), ('PINB',10), ('PINC',10)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x7A)],  # 0111 1010
    },
    {'description': 'Good Weight, Bad Balance C-A [10, 10, 100] (120 kg)',
    'steps': [ {'inputs': [('PINA',10), ('PINB',10), ('PINC',100)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x7A)],  # 0111 1010
    },
    {'description': 'Bad Weight, Good Balance [60, 50, 80] (190 kg)',
    'steps': [ {'inputs': [('PINA',60), ('PINB',50), ('PINC',80)], 'iterations': 5 } ],
    'expected': [('PORTD', 0xBD)],  # 1011 1101
    },
    {'description': 'Bad Weight, Bad Balance A-C [120, 50, 20] (190 kg)',
    'steps': [ {'inputs': [('PINA',120), ('PINB',50), ('PINC',20)], 'iterations': 5 } ],
    'expected': [('PORTD', 0xBF)],  # 1011 1111
    },
    {'description': 'Bad Weight, Bad Balance C-A [20, 50, 120] (190 kg)',
    'steps': [ {'inputs': [('PINA',20), ('PINB',50), ('PINC',120)], 'iterations': 5 } ],
    'expected': [('PORTD', 0xBF)],  # 1011 1111
    },
    {'description': 'TESTING FAIL: Bad Weight, Bad Balance -> Correct: 190 kg + D0 & D1; Testing: 0 kg + !D0 & !D1',  # This test will get a fail on purpose
    'steps': [ {'inputs': [('PINA',20), ('PINB',50), ('PINC',120)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x00)],  # 1011 1111
    },
    {'description': 'TESTING FAIL: Good Weight, Good Balance -> Correct: 70 kg + !D0 & !D1; Testing 0 kg + D0 & D1',
    'steps': [ {'inputs': [('PINA',20), ('PINB',30), ('PINC',20)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x03)],  # 0100 0100
    },
    ]
#watch = ['PORTB']

