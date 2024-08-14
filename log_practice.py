import logging
import datetime as dt

now = dt.datetime.today()
filename = f"tracker_{now.year}-{now.month:02d}-{now.day}.log"
print(filename)

logging.basicConfig(level=logging.DEBUG)

logger1 = logging.getLogger("Mylogs")

gen_log_file = logging.FileHandler(filename)
gen_log_file.setLevel(logging.DEBUG)
format_file = logging.Formatter("%(asctime)s: %(levelname)s -- %(message)s")  # Corrected here

gen_log_file.setFormatter(format_file)

logger1.addHandler(gen_log_file)

logger1.debug("Debug msg")
logger1.info("INFO msg")
logger1.warning("WARNING msg")
logger1.error("ERROR MSG")
logger1.critical("CRITICAL msg")
