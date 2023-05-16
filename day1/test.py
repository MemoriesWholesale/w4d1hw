from unittest import TestCase, main
from whiteboard import solution


class WhiteboardTestCase(TestCase):
    
    def test_1(self):
        self.assertEqual(solution("John loves to play baseball and Joanie loves to play basketball, but Jenny like to dance"),'l')
    
    def test_2_test_caps(self):
        self.assertEqual(solution("Hey You People maY I win pls You Knowpy"), 'y')

    def test_3_at_end(self):
        self.assertEqual(solution("ahhbablla"), "a")

    def test_3_cap_2(self):
        self.assertEqual(solution("HbbHllHyyHuu"), "h")
if __name__ == "__main__":
    main()