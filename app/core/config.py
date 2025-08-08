from dotenv import load_dotenv
from os import getenv


load_dotenv()

class Config:
    """
    Configuration class to hold application settings.
    """
    # Gemini
    GEMINI_API_KEY: str = getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = getenv("GEMINI_MODEL", "gemini-1.5-flash")

    # Cloudfare Workers AI API
    CF_API_KEY: str = getenv("CF_API_KEY", "")
    CF_MODEL: str = getenv("CF_MODEL", "stable-diffusion-v1-5-inpainting")
    CF_ACCOUNT_ID: str = getenv("CF_ACCOUNT_ID", "")

    # Instagram
    INSTAGRAM_USERNAME: str = getenv("INSTAGRAM_USERNAME", "")
    INSTAGRAM_PASSWORD: str = getenv("INSTAGRAM_PASSWORD", "")

    USE_RCLONE: bool = getenv("USE_RCLONE", "false").lower() in ("true", "1", "yes")
    RCLONE_REMOTE: str = getenv("RCLONE_REMOTE", "gdrive")
    RCLONE_DIR: str = getenv("RCLONE_PATH", "instasmith")

    SCHED_DAY_OF_WEEK: str = getenv("SCHED_DAY_OF_WEEK", "mon")
    SCHED_HOUR: int = int(getenv("SCHED_HOUR", "09"))
    SCHED_MINUTE: int = int(getenv("SCHED_MINUTE", "00"))