from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI()

# Permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Math Olympiad App API is running!"}

# Endpoint para upload de PDF
@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_location = f"uploaded_files/{file.filename}"

    os.makedirs("uploaded_files", exist_ok=True)

    with open(file_location, "wb") as f:
        f.write(await file.read())

    return {
        "message": "PDF recebido com sucesso!",
        "saved_as": file_location
    }


# Rodar localmente (o Render ignora isso)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)

