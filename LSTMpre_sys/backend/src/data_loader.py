# 数据加载与预处理
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


class StockDataLoader:
    def __init__(self, config):
        self.config = config
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def load_local_data(self):
        """加载本地CSV数据"""
        df = pd.read_csv(self.config.data_path)
        df = df[self.config.features ]
        return df.dropna()

    def preprocess_data(self, df):
        """数据预处理"""
        # 只使用 features 中定义的特征列
        df = df[self.config.features ]
        # df = df[self.config.features + [self.config.target]]

        # print(f"Data columns after filtering: {df.columns}")  # 打印筛选后的列名
        # print(f"Data shape after filtering: {df.shape}")  # 打印筛选后的数据形状

        # 检查是否有重复列
        if len(df.columns) != len(set(df.columns)):
            raise ValueError("数据列名重复，请检查 features 和 target 配置。")

        # 归一化处理
        scaled_data = self.scaler.fit_transform(df.values)
        # print(f"Scaled data shape: {scaled_data.shape}")  # 打印归一化后的数据形状

        # 创建时间序列样本
        X, y = [], []
        for i in range(len(scaled_data) - self.config.seq_length - 1):
            seq = scaled_data[i:i + self.config.seq_length]
            label = scaled_data[i + self.config.seq_length, df.columns.get_loc(self.config.target)]
            X.append(seq)
            y.append(label)

        return np.array(X), np.array(y)

    def split_data(self, X, y):
        """划分训练集、验证集、测试集"""
        total = len(X)
        train_end = int(total * self.config.train_ratio)
        val_end = train_end + int(total * self.config.val_ratio)

        return (X[:train_end], y[:train_end]), \
            (X[train_end:val_end], y[train_end:val_end]), \
            (X[val_end:], y[val_end:])

    def inverse_transform_close(self, data):
        """反归一化 close 列"""
        # 将 data 的形状从 (N,) 调整为 (N, 1)
        data_reshaped = data.reshape(-1, 1)

        # 拼接其他特征（假设其他特征为 0）
        dummy_features = np.zeros(
            (data_reshaped.shape[0], len(self.config.features) - 1))  # 其他 4 个特征（open, high, low, volume）
        input_to_scaler = np.concatenate([dummy_features, data_reshaped], axis=1)  # 形状为 (N, 5)

        # 反归一化并只取 close 列
        return self.scaler.inverse_transform(input_to_scaler)[:, -1]