from fastapi import FastAPI

# ----------------- Calculator Functions -----------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# ----------------- FastAPI App -----------------

app = FastAPI(title="Calculator API", description="Simple Calculator with FastAPI")

@app.get("/")
def root():
    return {"message": "Calculator API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/add")
def api_add(a: float, b: float):
    return {"result": add(a, b)}

@app.get("/subtract")
def api_subtract(a: float, b: float):
    return {"result": subtract(a, b)}

@app.get("/multiply")
def api_multiply(a: float, b: float):
    return {"result": multiply(a, b)}

@app.get("/divide")
def api_divide(a: float, b: float):
    return {"result": divide(a, b)}

# ----------------- CLI Calculator -----------------

def calculator():
    print("Simple Python Calculator")
    print("Operations: +  -  *  /")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(subtract(a, b))
    elif op == "*":
        print(multiply(a, b))
    elif op == "/":
        print(divide(a, b))
    else:
        print("Invalid operation!")

if __name__ == "__main__":
    calculator()
