#!/usr/bin/python
import unittest
from explode_json_data import flatten


class ExplodeTestCase(unittest.TestCase):
    """ test cases to check if `explode_json_data.py` module is
    Correct: Does it work as expected?
    Robust: Does the module cover edge cases and fail gracefully?
    Legible: Is it well commented
    Coding Style: does it follow common coding conventions?
    """

    # test case 1: if no nested objects the output should be same as input
    def test_not_to_explode(self):
        d = {'a': '1', 'b': '2', 'c': 3}
        exp_output = d
        act_input = flatten(d)
        self.assertEqual(exp_output, act_input)

    # test case 2: explode if it finds a list
    def test_explode_list(self):
        d = {'a': '1', 'b': '2', 'c': {'c1': '3', 'c2': '4'}}
        exp_output = {'a': '1', 'b': '2', 'c.c1': '3', 'c.c2': '4'}
        act_input = flatten(d)
        self.assertEqual(exp_output, act_input)

    # test case 3: explode if it finds a list
    def test_explode_nested_list(self):
        d = {
            'a': 1,
            'b': [{'c': [2, 3]}]
        }
        exp_output = {'a': 1, 'b.0.c.0': 2, 'b.0.c.1': 3}
        act_input = flatten(d)
        self.assertEqual(exp_output, act_input)

    # test case 4: explode when dict and list with multilevel nesting
    def test_explode_list_and_dict(self):
        d = {
            'a': 1,
            'b': 2,
            'c': [{'d': [2, 3, 4], 'e': [{'f': 1, 'g': 2}]}]
        }
        exp_output = {'a': 1, 'b': 2, 'c.0.d.0': 2, 'c.0.d.1': 3, 'c.0.d.2': 4, 'c.0.e.0.f': 1, 'c.0.e.0.g': 2}
        act_input = flatten(d)
        self.assertEqual(exp_output, act_input)

    # test case 5: when you empty list and dictionary
    def test_empty_list_and_dict(self):
        d = {
            'a': {},
            'b': [],
            'c': '',
            'd': None,
            'e': [{'f': [], 'g': [{'h': {}, 'i': [], 'j': '', 'k': None}]}]
        }
        exp_output = {'a': {},
                      'b': [],
                      'c': '',
                      'd': None,
                      'e.0.f': [],
                      'e.0.g.0.h': {},
                      'e.0.g.0.i': [],
                      'e.0.g.0.j': '',
                      'e.0.g.0.k': None
                      }

        act_input = flatten(d)
        self.assertEqual(exp_output, act_input)

    # test case 6: test a nested dictionary
    def test_nested_dict(self):
        nested_dict = {'dictA': {'key_1': 'value_1'}, 'dictB': {'key_2': 'value_2'}}
        exp_output = {'dictA.key_1': 'value_1', 'dictB.key_2': 'value_2'}
        act_input = flatten(nested_dict)
        self.assertEqual(exp_output, act_input)

    # test case 7: check if the dictionary is empty
    def empty_dict(self):
        d = {}
        exp_output = "__main__.EmptyDictionary"
        act_input = flatten(d)
        self.assertEqual(exp_output, act_input)

    # test case 8 : explode a list with utf-8
    def test_explode_list_utf8(self):
        d = {'a': '1',
             u'ñ': u'áéö',
             'c': {u'c1': '3', 'c2': '4'}}
        exp_output = {'a': '1', u'ñ': u'áéö', 'c.c1': '3', 'c.c2': '4'}
        act_input = flatten(d)
        self.assertEqual(exp_output, act_input)

    def test_one_flatten_utf8_dif(self):
        a = {u'eñe': 1}
        info = dict(info=a)
        exp_output = {u'info.{}'.format(u'eñe'): 1}
        act_input = flatten(info)
        self.assertEqual(act_input, exp_output)


if __name__ == '__main__':
    unittest.main()