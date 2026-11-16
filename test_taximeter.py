import unittest
import time
from taximeter import Taximeter, State
from unittest.mock import patch, mock_open

class TestTaximeter(unittest.TestCase):

    def test_load_valid_config(self):
        mock_json = '{"stopped_fare": 0.03, "moving_fare": 0.07}'
        
        with patch("builtins.open", mock_open(read_data=mock_json)):
            taxi = Taximeter(config_file="dummy.json")
            
        self.assertEqual(taxi.stopped_fare, 0.03)
        self.assertEqual(taxi.moving_fare, 0.07)

    def setUp(self):
        self.taximeter = Taximeter(config_file="archivo_inexistente.json")

    def test_initial_values(self):
        self.assertFalse(self.taximeter.is_running)
        self.assertEqual(self.taximeter.accumulated_cost, 0.0)

    def test_calculate_stopped_fare(self):
        self.taximeter.start_ride()
        
        self.taximeter.last_change_time = time.time() - 100
        
        total = self.taximeter.calculate_current_total()
        self.assertAlmostEqual(total, 2.00, places=2)

    def test_calculate_moving_fare(self):
        self.taximeter.start_ride()
        self.taximeter.change_state(State.MOVING)
        
        self.taximeter.last_change_time = time.time() - 100
        
        total = self.taximeter.calculate_current_total()
        self.assertAlmostEqual(total, 5.00, places=2)

if __name__ == '__main__':
    unittest.main()