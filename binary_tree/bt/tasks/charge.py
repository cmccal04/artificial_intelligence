#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Cullen McCaleb
# charge.py
#

import bt_library as btl
from ..globals import CHARGING
from ..globals import BATTERY_LEVEL


class Charge(btl.Task):
    """
    Implementation of the Task "Charge".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Charging!')

        blackboard.set_in_environment(CHARGING, True)
        blackboard.set_in_environment(BATTERY_LEVEL, 100)
        return self.report_succeeded(blackboard)