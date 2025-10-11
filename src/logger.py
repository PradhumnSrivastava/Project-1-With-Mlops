import logging
import os
from datetime import datetime

# Step 1: Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Define logs folder path
logs_path = os.path.join(os.getcwd(), "logs")

# Step 3: Create logs folder if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Step 4: Define full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Step 5: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [%(lineno)d] [%(name)s] - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Step 6: Test logging
if __name__ == "__main__":
    logging.info("Logging has started successfully.")
