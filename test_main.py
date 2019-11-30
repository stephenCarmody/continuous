"""
Unit tests for the main library
"""

import main


class TestMain:

    def test_count_list(self):
	    assert 2 == main.count_list(['a', 'b'])
