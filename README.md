# UE Trajectories

The project contains three folders:

- `sources` contains the training notebook and all the datasets needed to carry out the model training. As a result, you should obtain two serialized model files, one uses `joblib` to serialize the `scikit-learn` model; the other transforms the model to the ONNX format and serializes it.
- `docker` contains the code and configuration needed to build and run two images: One runs the native scikit-learn model (`sklearn` subfolder), the other runs the ONNX model (`onnxruntime` subfolder). The configuration files in the `config/config.yaml` file state the name of the model file and how to build the end-points to query the model (notice that the corresponding model obtained when running the training notebook must be copied to the `model` subfolder). Finally, the `tests` subfolder contains a script to query the model (a `docker-compose` file is provided for convenience).
- `kubernetes` contains some manifests that can be used to run the model in a Kubernetes cluster.
