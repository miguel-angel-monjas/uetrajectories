#!/usr/bin/env python
# coding: utf-8

import logging

from fastapi import APIRouter, status

from backend.common import prediction_engine
from backend.models import PredictionRequest

log = logging.getLogger('mobility_model_predict')

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
