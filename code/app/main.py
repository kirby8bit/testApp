from fastapi import FastAPI 
import uvicorn

app = FastAPI()

@app.get('/')
def get_operations(name: str ,message: str):
    some_str = "Hello" + name + " ! " + message
    return some_str


if __name__ == "__main__":
    print("app start !")