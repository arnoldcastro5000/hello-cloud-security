import logging
import os

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def get_environment() -> str:
    return os.getenv("APP_ENV", "local")


def greet() -> str:
    env = get_environment()
    message = f"Hello from hello-cloud-security! (env={env})"
    logger.info(message)
    return message


def main() -> None:
    print(greet())


if __name__ == "__main__":
    main()
