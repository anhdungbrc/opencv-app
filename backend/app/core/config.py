"""Application configuration settings."""


class Settings:
    """Application runtime configurations."""

    PROJECT_NAME: str = "OpenCV Studio Backend"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # Allowed CORS origins for Frontend development
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "*",
    ]


settings = Settings()
