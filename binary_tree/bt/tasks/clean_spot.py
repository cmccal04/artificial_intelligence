#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Cullen McCaleb
# clean_spot.py
#

import bt_library as btl
from ..globals import BATTERY_LEVEL

class CleanSpot(btl.Task):
    """
    Implementation of the Task "Clean Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Currently Cleaning Spot')
        
        if blackboard.get_in_environment(BATTERY_LEVEL, 0) < 30:
            self.print_message('Battery Low!')
            return self.report_failed(blackboard)
        
        return self.report_running(blackboard)