from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_item(height: float, weight: float):
    return {"BMI": bmi(height, weight),
                 "Label": label(bmi(height, weight))}

def bmi(height, weight):
    hasil = (weight) / ((height/100)**2)
    return hasil

def label(bmilabel): 
    if bmilabel > 24.9:
        return "Overweight"
    elif bmilabel < 18.5:
        return "Underweight"
    else:
        return "Normal"

if __name__ == "__main__":
    Union.run('main:app', host='127.0.0.1', port=8000, log_level="info", reload=True)
