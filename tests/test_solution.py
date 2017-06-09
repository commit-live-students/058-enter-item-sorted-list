from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        result = solution([1,2,5,4], 3)
        expected = [1,2,3,4,5]

        self.assertEqual(result, expected)