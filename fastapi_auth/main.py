import uvicorn

if __name__=='__main__':
    uvicorn.run("fastapi_auth.server:create_app", host="0.0.0.0", port=8081, reload=True)
