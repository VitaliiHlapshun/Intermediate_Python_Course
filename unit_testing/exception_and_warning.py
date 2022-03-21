"""
assertRaises(exc, fun, *args, **kwds) -------> fun(*args, **kwds) raises exc

assertRaisesRegex(exc, r, fun, *args, **kwds) -------> fun(*args, **kwds)
raises exc and the message matches regex r

assertWarns(warn, fun, *args, **kwds) -------> fun(*args, **kwds) raises warn

assertWarnsRegex(warn, r, fun, *args, **kwds) -------> fun(*args, **kwds)
raises warn and the message matches regex r

assertLogs(logger, level) -------> The with block logs on logger with minimum
level

assertNoLogs(logger, level) -------> The with block does not log on logger
with minimum level
"""

import unittest
import alerts


# Write your code here:
class SystemAlertTests(unittest.TestCase):
    def test_power_outage_alert(self):
        self.assertRaises(alerts.PowerError, alerts.power_outage_detected,
                          True)

    def test_water_levels_warning(self):
        self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check,
                         150)


unittest.main()
