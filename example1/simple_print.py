import os
import time

ENV_VAR_1 = os.getenv('envvar1')
ENV_VAR_2 = os.getenv('envvar2')
while True:
    print(ENV_VAR_1)
    print(ENV_VAR_2)
    print("-----------------------------")
    time.sleep(1)