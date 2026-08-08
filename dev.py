import uvicorn
from fastapi.staticfiles import StaticFiles
from api.index import app

# Mount the frontend webapp directory to serve static files
app.mount("/", StaticFiles(directory="webapp", html=True), name="webapp")

if __name__ == "__main__":
    print("Starting local server...")
    print("Web App: http://localhost:8000/")
    print("API:     http://localhost:8000/api/health")
    uvicorn.run("dev:app", host="127.0.0.1", port=8000, reload=True)
