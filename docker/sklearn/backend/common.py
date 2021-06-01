#!/usr/bin/env python
# coding: utf-8

import logging
import os
import warnings

from joblib import load

from config import get_configuration

log = logging.getLogger('mobility'
                        '_model_common')


class PredictionEngine:
    def __init__(self):
        self._configuration = get_configuration()
        model_file = os.path.join(os.getcwd(), 'model', self._configuration["model_file"])
        log.info(f"The ML model is available in {model_file}")
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=UserWarning)
            self._model = load(model_file)

    def predict(self, data):
        log.info(data)
        return self._model.predict(data)


prediction_engine = PredictionEngine()
