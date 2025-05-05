import matplotlib.pyplot as plt
# 主程序入口
import os
import torch
import numpy as np
import matplotlib.pyplot as plt
from configs.default import Config
from src.data_loader import StockDataLoader
from src.model import LSTMModel
from src.trainer import StockTrainer
from src.utils.visualize import plot_training_history, plot_predictions

def main():
    # 初始化配置
    config = Config()
    os.makedirs(f"{config.save_dir}/models", exist_ok=True)
    os.makedirs(f"{config.save_dir}/figures", exist_ok=True)

    # 加载数据
    loader = StockDataLoader(config)
    df = loader.load_local_data()
    X, y = loader.preprocess_data(df)
    train_data, val_data, test_data = loader.split_data(X, y)

    # 初始化模型
    model = LSTMModel(
        input_size=len(config.features),
        hidden_size=config.hidden_size,
        num_layers=config.num_layers
    )

    # 开始训练
    trainer = StockTrainer(config, model, (train_data, val_data, test_data))
    trainer.run()

    # 可视化训练过程
    plot_training_history(trainer.history, f"{config.save_dir}/figures", config.epochs)

    # 测试集预测
    model.load_state_dict(torch.load(f"{config.save_dir}/models/best_model.pth",weights_only=True))
    model.eval()
    with torch.no_grad():
        test_X = torch.FloatTensor(test_data[0]).to(config.device)
        preds = model(test_X).cpu().numpy()

    # 提取最后一个时间步的特征
    test_X_last_step = test_data[0][:, -1, :]  # 形状为 (batch_size, input_size)

    # 打印形状以验证维度
    print(f"test_X_last_step shape: {test_X_last_step.shape}")  # 应输出 (batch_size, input_size)
    print(f"test_data[1] shape: {test_data[1].shape}")  # 应输出 (batch_size,)
    print(f"preds shape: {preds.shape}")  # 应输出 (batch_size,)

    # # 直接使用原始的真实值（假设 test_data[1] 是原始的收盘价）
    # actual_close = test_data[1]  # 真实值
    #
    # # # 反归一化预测值
    # # preds_reshaped = preds.reshape(-1, 1)  # 将 preds 的形状从 (92,) 调整为 (92, 1)
    # # predicted_close = loader.scaler.inverse_transform(preds_reshaped).flatten()  # 反归一化并展平
    #
    # # 反归一化时提取目标值
    # dummy_features = np.zeros((92, 4))  # 其他 4 个特征（open, high, low, volume）
    # input_to_scaler = np.concatenate([dummy_features, preds.reshape(-1, 1)], axis=1)  # 形状为 (92, 5)
    # predicted_close = loader.scaler.inverse_transform(input_to_scaler)[:, -1]  # 只取 close 列

    # 直接使用原始的真实值（假设 test_data[1] 是原始的收盘价）
    actual_close = test_data[1]  # 真实值

    # 反归一化预测值
    preds_reshaped = preds.reshape(-1, 1)  # 将 preds 的形状从 (batch_size,) 调整为 (batch_size, 1)
    predicted_close = loader.scaler.inverse_transform(
        np.concatenate([np.zeros((preds_reshaped.shape[0], 4)), preds_reshaped], axis=1)
    )[:, -1]  # 只取 close 列

    # 反归一化实际值
    actual_close_reshaped = actual_close.reshape(-1, 1)  # 将 actual_close 的形状从 (batch_size,) 调整为 (batch_size, 1)
    actual_close = loader.scaler.inverse_transform(
        np.concatenate([np.zeros((actual_close_reshaped.shape[0], 4)), actual_close_reshaped], axis=1)
    )[:, -1]  # 只取 close 列


    # 打印实际值和预测值
    # print("actual_close:", actual_close)
    # print("predicted_close:", predicted_close)



     # 生成关键参数信息字符串
    params = (
            f"Learning Rate: {config.learning_rate}\n"
            f"Hidden Size: {config.hidden_size}\n"
            f"Batch Size: {config.batch_size}\n"
            # f"Epoch: {epoch + 1}/{config.epochs}\n"
            # f"Train Loss: {train_loss:.4f}\n"
            # f"Val Loss: {val_loss:.4f}"
        )

     # 绘制对比图并保存
    save_path = f"{config.save_dir}/figures"
    plot_predictions(actual_close, predicted_close, save_path, params,config.epochs)


    # 绘制对比图并保存
    # plot_predictions(actual_close, predicted_close, f"{config.save_dir}/figures",params,epoch)
    # plot_predictions(actual_close, predicted_close,save_path)
    # save_path = f"{config.save_dir}/figures"
    # os.makedirs(save_path, exist_ok=True)


    # # 绘制对比图
    # plt.figure(figsize=(10, 6))
    # plt.plot(actual_close, label="Actual Close Price")
    # plt.plot(predicted_close, label="Predicted Close Price")
    # plt.legend()
    # plt.title("Actual vs Predicted Close Price")
    # plt.xlabel("Time Step")
    # plt.ylabel("Price")
    # plt.show()

#系统硬件使用和占用情况
    print(f"Using device: {config.device}")  #当前正在用GPU还是CPU
    print(torch.cuda.memory_allocated())  # 当前分配的显存
    print(torch.cuda.memory_reserved())  # 当前保留的显存


if __name__ == "__main__":
    main()