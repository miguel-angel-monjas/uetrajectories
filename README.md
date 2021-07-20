# UE Trajectories

The project contains three folders:

- `sources` contains the training notebook and all the datasets needed to carry out the model training. As a result, you should obtain two serialized model files, one uses `joblib` to serialize the `scikit-learn` model; the other transforms the model to the ONNX format and serializes it.
- `docker` contains the code and configuration needed to build and run two images: One runs the native scikit-learn model, the other runs the ONNX model. The configuration files in the `config/config.yaml` file state the name of the model file and the end-points (notice that the corresponding model obtained when running the training notebook must be copied to the `model` subfolder).
- `kubernetes` contains some manifests that can be used to run the model in a Kubernetes cluster.
