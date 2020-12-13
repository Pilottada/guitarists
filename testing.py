import unittest
import guitarists as g

class TestName(unittest.TestCase):
    
    def test_check_band(self):
        result = g.check_band("Led Zeppelin")
        
        self.assertEqual(result, print("The guitar hero of {} is {}".format("Led Zeppelin", "Jimmy Page")))
        
    def test_check_guitarist(self):
        result = g.check_guitarist("Jimmy Page")
        
        self.assertEqual(result,print("{} plays for {}".format("Jimmy Page", "Led Zeppelin")))
    
    #def test_adding_process(self):
    #    result = g.check_band("Led Zeppelin")
    #    self.assertEqual(result, print("The guitar hero of {} is {}".format("Led Zeppelin", "Jimmy Page")))
        
        
        
if __name__ == "__main__":
    unittest.main()