#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Cullen McCaleb
# clean_floor.py
#

import bt_library as btl
from ..globals import NUM_CLEANS

class CleanFloor(btl.Task):
    """
    Implementation of the Task "Clean Floor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Currently Cleaning Floor')
        blackboard.set_in_environment(NUM_CLEANS, blackboard.get_in_environment(NUM_CLEANS, 0) - 1)
        self.print_message('Cleans Remaining: ' + str(blackboard.get_in_environment(NUM_CLEANS, 0)))

        if blackboard.get_in_environment(NUM_CLEANS, 0) > 0:
            return self.report_running(blackboard)
        elif blackboard.get_in_environment(NUM_CLEANS, 0) == 0:
            return self.report_failed(blackboard)