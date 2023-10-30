import random
import time

from klym_telemetry.instrumenters import instrument_app
from klym_telemetry.utils import klym_telemetry, instrument

RUN_COUNT_METRIC = "run_counter_metric"
RUNP_COUNT_DESCRIPTION = "Count of executions"


@instrument(private_methods=True, attributes={"description": "Class to say hello"})
class RunRandomCounter:

    def __init__(self):
        self.random_sleep()
        self.random_counter()

    def random_sleep(self):
        time.sleep(random.randint(1,5))
        return None

    def random_counter(self):
        time.sleep(1)
        counter = random.randint(2,100)
        for i in range(1, counter):
            klym_telemetry.up(
                name=RUN_COUNT_METRIC, description=RUNP_COUNT_DESCRIPTION
            )

def main():
    instrument_app(app_type='python', service_name="python", endpoint="https://84b5-186-84-91-85.ngrok-free.app")
    RunRandomCounter()


if __name__ == '__main__':
    main()
