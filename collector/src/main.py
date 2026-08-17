import logging
import sys
from collector.src.config import CollectorConfig

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("soc_collector_agent")


def main():
    logger.info("Starting SOC Log Collector (Project 1: SOCUaTrace)...")
    config = CollectorConfig()
    logger.info(f"Collector configured for server at: {config.server_url}")
    logger.info(f"Collector platform: {sys.platform}")


if __name__ == "__main__":
    main()
