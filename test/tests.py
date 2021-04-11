tests = [ {'description': 'Good Weight, Good Balance [20, 30, 20] (70 kg)',
    'steps': [ {'inputs': [('PINA',20), ('PINB',30), ('PINC',20)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x10)],  # 0001 0000
    },
    {'description': 'Good Weight, Bad Balance A-C [100, 10, 10] (120 kg)',
    'steps': [ {'inputs': [('PINA',100), ('PINB',10), ('PINC',10)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x1E)],  # 0001 1110
    },
    {'description': 'Good Weight, Bad Balance C-A [10, 10, 100] (120 kg)',
    'steps': [ {'inputs': [('PINA',10), ('PINB',10), ('PINC',100)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x1E)],  # 0001 1110
    },
    {'description': 'Bad Weight, Good Balance [60, 50, 80] (190 kg)',
    'steps': [ {'inputs': [('PINA',60), ('PINB',50), ('PINC',80)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x2D)],  # 0010 1101
    },
    {'description': 'Bad Weight, Bad Balance A-C [120, 50, 20] (190 kg)',
    'steps': [ {'inputs': [('PINA',120), ('PINB',50), ('PINC',20)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x2F)],  # 0010 1111
    },
    {'description': 'Bad Weight, Bad Balance C-A [20, 50, 120] (190 kg)',
    'steps': [ {'inputs': [('PINA',20), ('PINB',50), ('PINC',120)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x2F)],  # 0010 1111
    },
    {'description': 'Large Number [200, 200, 200] (600 kg)',
    'steps': [ {'inputs': [('PINA',200), ('PINB',200), ('PINC',200)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x95)],  # 1001 0101
    },
    {'description': 'TESTING FAIL: Bad Weight, Bad Balance -> Correct: 190 kg + D0 & D1; Testing: 0 kg + !D0 & !D1',  # This test will get a fail on purpose
    'steps': [ {'inputs': [('PINA',20), ('PINB',50), ('PINC',120)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x00)],  
    },
    {'description': 'TESTING FAIL: Good Weight, Good Balance -> Correct: 70 kg + !D0 & !D1; Testing 0 kg + D0 & D1',  # This test will get a fail on purpose
    'steps': [ {'inputs': [('PINA',20), ('PINB',30), ('PINC',20)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x03)],  
    },
    ]
#watch = ['PORTB']

