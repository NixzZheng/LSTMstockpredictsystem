#配置文件
import torch


class Config:
    # 数据配置
    data_path = "D:/Work_CS/backend/data/raw/stock.csv"  # 本地数据路径
    features = ['open', 'high', 'low', 'close', 'volume']  # 使用特征
    target = 'close'  # 预测目标
    seq_length = 60  # 时间窗口长度



    # 训练参数
    train_ratio = 0.8
    val_ratio = 0.1
    batch_size = 64
    epochs = 300
    learning_rate = 0.001
    hidden_size = 128  # LSTM隐藏层维度
    num_layers = 2  # LSTM层数

    # 系统参数
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    save_dir = "outputs/"


