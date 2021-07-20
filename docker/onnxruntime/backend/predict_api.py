#!/usr/bin/env python
# coding: utf-8

import logging

from fastapi import APIRouter, status
from prometheus_client import Summary

from backend.common import prediction_engine
from backend.models import PredictionRequest

log = logging.getLogger('mobility_model_predict')

REQUEST_TIME = Summary('prediction_request_processing_seconds',
                       'Time spent generating a prediction',
                       ['pod', 'node', 'namespace', 'model_id', 'model_version'])

router = APIRouter()


@router.post("/predict", status_code=status.HTTP_200_OK)
def predict(req: PredictionRequest):
    req = req.dict()
    log.info("Prediction request:")
    log.info(req)
    prediction = prediction_engine.predict(req['data']['ndarray'])
    log.info("Prediction:")
    log.info(prediction)
    return prediction.tolist()
