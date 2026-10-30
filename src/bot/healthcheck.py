"""Docker HEALTHCHECK: healthy while the poller has finished a poll recently."""

import sys
import time

from .config import Config


def main() -> int:
    config = Config.from_env(require_token=False)
    max_age = config.poll_interval_minutes * 60 * 3 + 120
    try:
        age = time.time() - config.heartbeat_path.stat().st_mtime
    except OSError:
        return 1
    return 0 if age < max_age else 1


if __name__ == "__main__":
    sys.exit(main())
