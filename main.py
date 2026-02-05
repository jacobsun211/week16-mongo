from fastapi import FastAPI
from routers import users, orders, products  # Import all 3 routers
import os

app = FastAPI()

# Include each router with its own prefix
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
app.include_router(products.router, prefix="/products", tags=["products"])

@app.get("/")
async def root():
    """Check if API is running"""
    DATABASE_NAME = os.getenv("DATABASE_NAME", "exe2")
    return {"status": "API is running", "database": DATABASE_NAME}


# python -m uvicorn main:app --reload

# docker run -d --name mongo -p 27017:27017 -v mongo_data:/data/db mongo:latest

# oc login --token=sha256~zzQ5a1uARgdV9mGKuK31cB3FVf39Z2ezDncOsT45kL8 --server=https://api.rm1.0a51.p1.openshiftapps.com:6443

# docker build -t jacobsun211/fastapi-app:latest .






# ---------------------------------------------- fix for openshift
# oc create route edge --service=fastapi-service --port=8000

# oc get route



# oc expose service fastapi-service