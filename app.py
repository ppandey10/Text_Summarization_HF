import os 
import sys
import uvicorn

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response

from starlette.responses import RedirectResponse

from txtsummarizer.pipeline.model_prediction import ModelPredictionPipeline


text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

#===============================================================================#
# For training
@app.get("/train")
async def training():
    try:
        os.system("python main.py") # detect as command and then run the file
        return Response("Training successful!!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    
#================================================================================#
# For prediction
@app.post("/predict")
async def predict_route(text):
    try:

        obj = ModelPredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    
#================================================================================#

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)