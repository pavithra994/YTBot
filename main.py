from fastapi import FastAPI
import json
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/channel_subscribe/{channel_id}")
async def channel_subscribe(channel_id: int):
    new_channel =  {"channel_id": channel_id}
    with open('data.json') as f:
        data = json.load(f)

    channel_list = data['channel_data']
    channel_list.append(new_channel)
    data['channel_data'] = channel_list

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)

    return new_channel


@app.get("/channel_list")
async def root():
    with open('data.json') as f:
        data = json.load(f)
    return data