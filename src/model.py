import torch
import torch.nn as nn


class LightningModel(nn.Module):
    def __init__(self, in_dim: int = 28 * 28, out_dim: int = 10) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 128),
            nn.ReLU(),
            nn.Linear(128, out_dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)
