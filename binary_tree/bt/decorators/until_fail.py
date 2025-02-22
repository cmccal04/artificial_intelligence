#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Cullen McCaleb
#  until_fail.py
#

from bt_library.blackboard import Blackboard
from bt_library.common import ResultEnum
from bt_library.decorator import Decorator
from bt_library.tree_node import TreeNode

class UntilFail(Decorator):
    """
    Specific implementation of the until-fail decorator.
    """
    def __init__(self, child: TreeNode):
        """
        Default constructor.

        :param child: Child associated with the decorator
        """
        super().__init__(child)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        # Evaluate the child node
        result_child = self.child.run(blackboard)

        # If the child fails, return SUCCESS
        if result_child == ResultEnum.FAILED:
            return self.report_succeeded(blackboard)

        # If the child is still running or succeeded, continue running
        return self.report_running(blackboard)
