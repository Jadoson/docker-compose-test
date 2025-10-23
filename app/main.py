from fastapi import FastAPI
app = FastAPI()

@app.get("/health") 
def health(): 
    return {"status": "ok"}

@app.get("/", include_in_schema=False) 
def root(): 
    return {"ok": True}