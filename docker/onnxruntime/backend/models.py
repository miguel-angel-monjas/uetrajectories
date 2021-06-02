#!/usr/bin/env python
# coding: utf-8

from typing import List

from pydantic import BaseModel, conlist


class PredictionRequestPayload(BaseModel):
    ndarray: List[conlist(int, min_items=18, max_items=18)]


class PredictionRequest(BaseModel):
    data: PredictionRequestPayload


class PredictionResponsePayload(BaseModel):
    ndarray: List[conlist(int, min_items=2, max_items=2)]


class PredictionResponse(BaseModel):
    data: PredictionResponsePayload
