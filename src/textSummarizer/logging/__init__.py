import os
import sys
import logging

log_dir="logs"
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" ## the way details will be displayed

log_filepath = os.path.join(log_dir,"continuos_logs.log") ##joins paths of both file and directory

os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), ## to put logging content inside the file
        logging.StreamHandler(sys.stdout) ### to display in terminal
    ]
)

logger=logging.getLogger("summarizerlogger")
## instance for using logging