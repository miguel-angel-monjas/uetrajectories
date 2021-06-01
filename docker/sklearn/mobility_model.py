#!/usr/bin/env python
# coding: utf-8

import logging

import uvicorn
from fastapi import FastAPI

from config import get_configuration
from backend.predict_api import router

log = logging.getLogger('mobility_model')

configuration = get_configuration()


app = FastAPI()
app.include_router(router,
                   prefix=configuration["api_basepath"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=configuration["exposed_port"])
