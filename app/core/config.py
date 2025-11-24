from pydantic_settings import SettingsConfigDict, BaseSettings

__all__ = ["settings"]


class DatabaseConfig(BaseSettings):
    user: str
    password: str
    name: str
    host: str
    port: int = 5432


class RunConfig(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 3003


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DatabaseConfig
    model_config = SettingsConfigDict(
        env_file=[".env.dev", ".env"],
        case_sensitive=False,
        env_nested_delimiter="__",
    )


settings = Settings()
