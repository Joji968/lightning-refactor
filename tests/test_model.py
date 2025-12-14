import torch
from src.model import LightningModel


def test_forward_shape():
    model = LightningModel()
    x = torch.randn(1, 28 * 28)
    y = model(x)
    assert y.shape == (1, 10)
