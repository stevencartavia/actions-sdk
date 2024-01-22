import numpy as np

from giza_actions.model import GizaModel


def test_predict_success():

    model = GizaModel(
        model_path="",
        orion_runner_service_url="http://localhost:8080")

    arr = np.array([[1, 2], [3, 4]], dtype=np.uint32)

    result = model.predict(
        input_feed={"arr_1": arr}, verifiable=True, output_dtype='tensor_uint')

    assert np.array_equal(result, arr)
