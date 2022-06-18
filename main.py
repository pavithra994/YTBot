from fastapi import FastAPI, Response, Request, HTTPException, Query
import xmltodict

import json
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/channel_subscribe")
async def channel_subscribe_get(hub_challenge: str = Query(default=None,alias="hub.challenge")):
    # for key, value in kwargs.items():
    #     print("%s == %s" % (key, value))
    # print(hub_challenge)
    return Response(content=hub_challenge,status_code=200)


@app.post("/channel_subscribe")
async def channel_subscribe(request: Request):
    content_type = request.headers['Content-Type']
    print(content_type)
    if content_type == 'application/atom+xml':
        body = await request.body()
        body_data = xmltodict.parse(body)
        print(body_data)
        # return Response(content=body, media_type="application/xml")
        with open('data.json') as f:
            data = json.load(f)

        channel_list = data['channel_data']
        channel_list.append(body_data)
        data['channel_data'] = channel_list

        with open('data.json', 'w') as f:
            json.dump(data, f, indent=2)
        #
        # return new_channel

        return Response(status_code=204)
    else:
        raise HTTPException(status_code=400, detail=f'Content type {content_type} not supported')
    # new_channel =  {"channel_id": channel_id}
    # with open('data.json') as f:
    #     data = json.load(f)
    #
    # channel_list = data['channel_data']
    # channel_list.append(new_channel)
    # data['channel_data'] = channel_list
    #
    # with open('data.json', 'w') as f:
    #     json.dump(data, f, indent=2)
    #
    # return new_channel


@app.get("/channel_list")
async def channel_list():
    print("hoooo")
    with open('data.json') as f:
        data = json.load(f)
    return data


@app.post("/submit")
async def submit(request: Request):
    content_type = request.headers['Content-Type']
    if content_type == 'application/atom+xml':
        body = await request.body()
        body_data = xmltodict.parse(body)
        print(body_data)
        # return Response(content=body, media_type="application/xml")
        return body_data
    else:
        raise HTTPException(status_code=400, detail=f'Content type {content_type} not supported')