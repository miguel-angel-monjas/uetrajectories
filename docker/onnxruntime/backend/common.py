#!/usr/bin/env python
# coding: utf-8

import logging
import os
import warnings

import numpy as np
import onnxruntime as rt

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
            self._sess = rt.InferenceSession(model_file)
            self._input_name = self._sess.get_inputs()[0].name
            self._label_name = self._sess.get_outputs()[0].name
            log.info("Model uploaded")

    def predict(self, data):
        log.info(data)
        data = np.array(data)
        return self._sess.run([self._label_name], {self._input_name: data})[0]


prediction_engine = PredictionEngine()
