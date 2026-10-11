#!/usr/bin/env python3
"""
start.py - Main entry point for GitHub Actions macOS runner.
"""

import logging
import os
import platform
import sys

# Configure logging to output directly to the GitHub Actions console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


def main():
  logging.info("Starting execution on macOS runner...")

  # Print environment details for debugging or verification
  logging.info(f"Python Version: {sys.version}")
  logging.info(f"Platform System: {platform.system()} {platform.release()}")
  logging.info(f"Architecture: {platform.machine()}")

  # Check if running inside GitHub Actions
  is_ci = os.getenv("CI") == "true"
  logging.info(f"Running in CI/CD Environment: {is_ci}")

  # TODO: Add your main logic or script execution code here
  logging.info("start.py executed successfully.")


if __name__ == "__main__":
  try:
    main()
  except Exception as e:
    logging.error(f"An unexpected error occurred: {e}", exc_info=True)
    sys.exit(1)
