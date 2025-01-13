from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_DIR: str
    HUGGING_FACE_TOKEN: str
    URL_DATASET: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='allow')

environment = Settings()