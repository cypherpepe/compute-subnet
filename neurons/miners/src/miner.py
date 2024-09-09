import asyncio
import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.config import settings
from core.miner import Miner
from routes.debug_routes import debug_apis_router
from routes.validator_interface import validator_router

# Set up logging
logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    miner = Miner()
    # Run the miner in the background
    task = asyncio.create_task(miner.start())

    try:
        yield
    finally:
        await miner.stop()  # Ensure proper cleanup
        await task  # Wait for the background task to complete
        logging.info("Miner exited successfully.")


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=app_lifespan,
)

app.include_router(validator_router)
app.include_router(debug_apis_router)

if __name__ == "__main__":
    uvicorn.run("miner:app", host="0.0.0.0", port=settings.INTERNAL_PORT, reload=True)
