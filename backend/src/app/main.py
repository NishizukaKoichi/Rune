"""
Main application entry point for the AI Cage-Driven Development backend.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI Cage-Driven Development API",
    description="Backend API for the cage-driven development system",
    version="1.0.0"
)


class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    message: str


class ItemResponse(BaseModel):
    """Sample item response model."""
    id: int
    name: str
    description: str


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "AI Cage-Driven Development API"}


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        message="Backend is running"
    )


@app.get("/api/v1/items", response_model=list[ItemResponse])
async def get_items() -> list[ItemResponse]:
    """Get sample items."""
    return [
        ItemResponse(id=1, name="Item 1", description="First item"),
        ItemResponse(id=2, name="Item 2", description="Second item"),
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)  # noqa: S104
