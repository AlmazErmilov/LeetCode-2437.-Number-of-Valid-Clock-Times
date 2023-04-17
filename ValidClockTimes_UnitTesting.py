import unittest
from ValidClockTimes_final import validClockTimes

test_cases = [
    ('01:05', 1),
    ('01:0?', 10),
    ('01:?0', 6),
    ('01:??', 60),
    ('0?:00', 10),
    ('0?:0?', 100),
    ('0?:?0', 60),
    ('0?:??', 600),
    ('2?:00', 4),
    ('2?:0?', 40),
    ('2?:?0', 24),
    ('2?:??', 240),
    ('?3:00', 3),
    ('?3:0?', 30),
    ('?3:?0', 18),
    ('?3:??', 180),
    ('?4:22', 2),
    ('?4:0?', 20),
    ('?4:?0', 12),
    ('?4:??', 120),
    ('??:00', 24),
    ('??:0?', 240),
    ('??:?1', 144),
    ('??:??', 1440)
]

class TestValidClockTimes(unittest.TestCase):
    def test_all(self):
        for time, expected in test_cases:
            with self.subTest(case=time, expected=expected):
                result = validClockTimes(time)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
