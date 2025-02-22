#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt as bt
import bt_library as btl

# Instantiate the tree according to the assignment
tree_root = bt.Selection(
    [
        bt.Sequence(
            [
                bt.BatteryLessThan30(),
                bt.FindHome(),
                bt.GoHome(),
                bt.Charge()
            ]
        ),
        bt.Selection(
            [
                bt.Sequence(
                    [
                        bt.SpotCleaning(),
                        bt.Timer(20, bt.CleanSpot()),
                        bt.DoneSpot()
                    ]
                ),
                bt.Sequence(
                    [
                        bt.GeneralCleaning(),
                        bt.Sequence(
                            [
                                bt.Sequence(
                                    [
                                        bt.Selection(
                                            [
                                                bt.Sequence(
                                                    [
                                                        bt.DustySpot(),
                                                        bt.Timer(35, bt.CleanSpot()),
                                                        bt.AlwaysFail()
                                                    ]
                                                ),
                                                bt.CleanFloor()
                                            ]
                                        ),
                                        bt.DoneGeneral()
                                    ]
                                )
                            ]
                        ),
                    ]
                )

            ]
        ),
        bt.DoNothing()

    ]
)

# Store the root node in a behavior tree instance
robot_behavior = btl.BehaviorTree(tree_root)
