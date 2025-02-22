#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Cullen McCaleb
# done_general.py
#

import bt_library as btl
from ..globals import GENERAL_CLEANING

class DoneGeneral(btl.Task):
    """
    Implementation of the Task "Done General".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:

        self.print_message('General Cleaning is done!')
        blackboard.set_in_environment(GENERAL_CLEANING, False)

        return self.report_succeeded(blackboard)