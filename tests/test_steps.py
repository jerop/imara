import unittest

from pkg.tuner import steps

class TestSimple(unittest.TestCase):

    def test_aget_reward_model_train_steps(self):
        self.assertEqual(steps.get_reward_model_train_steps(), 1407)

if __name__ == '__main__':
    unittest.main()
