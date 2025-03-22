from fastapi import FastAPI
from routes.accounts import router as accounts_router
from fastapi.middleware.cors import CORSMiddleware

# Instantiate FastAPI application
app = FastAPI(
    title="TransferServiceAPI",
    description="RESTful API for mocking transfers between accounts. Internship Programming Assignment - Group Technology at Dialog.",
)

# Bind routers
app.include_router(accounts_router)


# Define allowed origins for CORS
origins = [
    "http://localhost:3000",
]
# NOTE
# Assumed that a client running on the above URL
# will require connecting to this service.

# Setup CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root route (to test service health)
@app.get("/", tags=["Internals"])
async def root():
    return {
        "message": "TransferService is up and running.",
    }
