"""
Unit tests for the main library
"""

import main


class TestMain:

    def test_count_list(self):
        assert 2 == main.count_list(['a', 'b'])


    def test_multiplication(self):
        assert 100 == main.multiply(10, 10)
