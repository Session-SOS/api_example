# # input from prompts
# def add(x,y):
#     return x + y

# x = int(input('x value: '))
# y = int(input('y value: '))

# print(f'result is {add(x,y)}')

# # input from command line call
# import sys

# def add(x,y):
#     return x + y

# if __name__ == '__main__':
#     x = int(sys.argv[1])
#     y = int(sys.argv[2])

#     print(f'result is {add(x,y)}')

# run it as a restAPI
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/add")
def add(x:float, y:float):
    return x + y

@app.get("/subtract")
def subtract(x:float, y:float):
    return x - y

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9321)
