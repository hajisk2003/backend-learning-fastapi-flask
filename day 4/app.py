import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Linear(3, 5),
            nn.ReLU(),
            nn.Linear(5, 1)
        )

    def forward(self, x):
        return self.layer(x)

model=nn.Linear(3,1)
x=torch.tensor([[1.0,2.0,3.0]])
output=model(x)
print(output)