from dotenv import load_dotenv
from pydantic import Field, field_validator, ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load environment variables from .env file
load_dotenv()


class Config(BaseSettings):
    """
    Configuration class that loads settings from environment variables.
    Utilizes pydantic for validation and type enforcement.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",
    )

    # Discord Bot Token
    discord_bot_token: str = Field(..., env="DISCORD_BOT_TOKEN")

    # Secret Seed (must match the one in your MediaWiki settings)
    secret_seed: str = Field(..., env="SECRET_SEED")

    # Key Length (number of characters expected in the user's key)
    key_length: int = Field(16, env="KEY_LENGTH")

    # Answer Length (number of characters to return as the secret key)
    answer_length: int = Field(8, env="ANSWER_LENGTH")

    # Log Level
    log_level: str = Field("INFO", env="LOG_LEVEL")

    # Guild IDs
    guild_ids: list[str | int] = Field([], env="GUILD_IDS", parse=True)

    @field_validator("key_length", "answer_length")
    def positive_int(cls, v: int, info: ValidationInfo):
        if v <= 0:
            raise ValueError(f"{info.field_name} must be a positive integer")
        return v

    @field_validator("log_level")
    def valid_log_level(cls, v: str, info: ValidationInfo):
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if v.upper() not in valid_levels:
            raise ValueError(f"log_level must be one of {valid_levels}")
        return v.upper()

    @field_validator("guild_ids")
    def parse_guild_ids(cls, v: str, info: ValidationInfo):
        return [int(guild_id) for guild_id in v]


# Instantiate the Config class
config = Config()
