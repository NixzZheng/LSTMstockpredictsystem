# 训练逻辑
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from tqdm import tqdm


class StockTrainer:
    def __init__(self, config, model, data_loader):
        self.config = config
        self.model = model.to(config.device)
        self.data_loader = data_loader
        self.criterion = nn.MSELoss()
        self.optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)

        # 准备数据
        (X_train, y_train), (X_val, y_val), (X_test, y_test) = data_loader
        self.train_loader = self._create_loader(X_train, y_train, shuffle=True)
        self.val_loader = self._create_loader(X_val, y_val)
        self.test_loader = self._create_loader(X_test, y_test)

        # 训练记录
        self.history = {'train_loss': [], 'val_loss': []}
        self.best_loss = float('inf')

    def _create_loader(self, X, y, shuffle=False):
        dataset = TensorDataset(
            torch.FloatTensor(X).to(self.config.device),
            torch.FloatTensor(y).to(self.config.device))
        return DataLoader(dataset, batch_size=self.config.batch_size, shuffle=shuffle)

    def train_epoch(self):
        self.model.train()
        total_loss = 0
        for X_batch, y_batch in self.train_loader:
            # print(f"X_batch shape: {X_batch.shape}")  # 打印输入数据形状
            self.optimizer.zero_grad()
            outputs = self.model(X_batch)
            loss = self.criterion(outputs, y_batch)
            loss.backward()
            self.optimizer.step()
            total_loss += loss.item()
        return total_loss / len(self.train_loader)

    def validate(self):
        self.model.eval()
        total_loss = 0
        with torch.no_grad():
            for X_batch, y_batch in self.val_loader:
                outputs = self.model(X_batch)
                loss = self.criterion(outputs, y_batch)
                total_loss += loss.item()
        return total_loss / len(self.val_loader)

    def run(self):
        #for epoch in range(self.config.epochs):
        #for epoch in tqdm(range(epochs), desc="Training"):
        for epoch in tqdm(range(self.config.epochs), desc="Training"):
            train_loss = self.train_epoch()
            val_loss = self.validate()

            # 记录训练过程
            self.history['train_loss'].append(train_loss)
            self.history['val_loss'].append(val_loss)

            # 保存最佳模型
            if val_loss < self.best_loss:
                self.best_loss = val_loss
                torch.save(self.model.state_dict(),
                           f"{self.config.save_dir}/models/best_model.pth")

            # 打印进度
            print(f'Epoch {epoch + 1}/{self.config.epochs} | '
                  f'Train Loss: {train_loss:.5f} | Val Loss: {val_loss:.5f}')