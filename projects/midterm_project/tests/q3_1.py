test = {   'name': 'q3_1',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> callable(in_cali) and isinstance(in_cali('San Diego'), bool)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> in_cali('San Diego')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> not in_cali('PA')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> not in_cali(ucsd_admit.get('Region').sort_values().iloc[-1])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> not in_cali('Unknown')\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
