from torch import nn

size_IMG = 24
depth_1 = 16
depth_2 = 16
num_classes = 1950

class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, depth_1, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(depth_1, depth_2, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.drop_out = nn.Dropout()
        self.fc1 = nn.Linear(int(size_IMG ** 2 / 16) * depth_2, 100)
        self.fc2 = nn.Linear(100, num_classes)

    def forward(self, x):
        out = self.layer1(x)
        # conv_x = self.layer2[0](out)

        out = self.layer2(out)
        # max_pool_x = out

        out = out.reshape(out.size(0), -1)
        out = self.drop_out(out)

        out = self.fc1(out)
        out = self.fc2(out)

        return out #, conv_x, max_pool_x