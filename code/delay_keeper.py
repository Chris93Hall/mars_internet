"""
delay_keeper.py
"""

class DelayKeeper:
    delay_seconds = 480

    @classmethod
    def get_delay_seconds(cls):
        return cls.delay_seconds

    @classmethod
    def set_delay_seconds(cls, delay):
        cls.delay_seconds = delay
        return

    @classmethod
    def get_delay(cls):
        return cls.get_delay_seconds()

    @classmethod
    def set_delay(cls, delay):
        cls.set_delay_seconds(delay)
        return

