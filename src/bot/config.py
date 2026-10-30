import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    token: str
    poll_interval_minutes: int
    data_dir: Path
    log_level: str

    @classmethod
    def from_env(cls, require_token: bool = True) -> "Config":
        token = os.environ.get("DISCORD_TOKEN", "").strip()
        if require_token and not token:
            raise SystemExit("DISCORD_TOKEN is not set")
        return cls(
            token=token,
            poll_interval_minutes=max(1, int(os.environ.get("POLL_INTERVAL_MINUTES", "10"))),
            data_dir=Path(os.environ.get("DATA_DIR", "/data")),
            log_level=os.environ.get("LOG_LEVEL", "INFO").upper(),
        )

    @property
    def db_path(self) -> Path:
        return self.data_dir / "bot.db"

    @property
    def heartbeat_path(self) -> Path:
        return self.data_dir / "heartbeat"
