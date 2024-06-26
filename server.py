from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Computer(BaseModel):
    name: str
    graphics_card: str = None
    cpu : str | None
    n_of_cores: int
    ram : list

@app.post('/')
async def answer(item : Computer):
    if item.graphics_card:
        graphics_message = f"The computer has a {item.graphics_card} graphics card."
    else:
        graphics_message = "No graphics card specified."

    # Check the number of CPU cores
    if item.n_of_cores >= 8:
        cores_message = "This is a high-performance computer with many cores."
    elif 4 <= item.n_of_cores < 8:
        cores_message = "This is a mid-range computer."
    else:
        cores_message = "This is a low-end computer with fewer cores."

    ram = 0
    for r in item.ram:
        ram += r
    item.ram = [ram]

    # Create a response message
    response_message = (
        f"\n\nComputer Name: {item.name}\n"
        f"CPU: {item.cpu}\n"
        f"Number of Cores: {item.n_of_cores}\n"
        f"RAM: {', '.join(map(str, item.ram))} GB\n"
        f"{graphics_message}\n"
        f"{cores_message}"
    )

    return response_message

