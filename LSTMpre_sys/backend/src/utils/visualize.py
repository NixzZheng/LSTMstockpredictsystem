# 可视化模块
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

def plot_training_history(history, save_path,total_epochs):
    plt.figure(figsize=(12, 5))

    # 绘制损失曲线
    # plt.subplot(1, 2, 1)
    plt.plot(history['train_loss'], label='Train Loss')
    plt.plot(history['val_loss'], label='Validation Loss')
    plt.title(f'Training and Validation Loss (Total Epochs: {total_epochs})')
    plt.xlabel('Epoch')
    plt.ylabel('MSE Loss')
    plt.legend()

    # 保存图表
    plt.savefig(f"{save_path}/Total Epochs_{total_epochs}_training_curve.png")
    plt.show()


def plot_predictions(actual_close, predicted_close, save_path,params,total_epochs):
    """
        绘制实际值与预测值的对比图并保存

        参数：
        - actual_close: 实际值（一维数组）
        - predicted_close: 预测值（一维数组）
        - save_path: 图片保存路径
        - params: 训练的关键参数信息（字符串）

        """
    plt.figure(figsize=(12, 6))
    plt.plot(actual_close, label='Actual Price', alpha=0.7)
    plt.plot(predicted_close, label='Predicted Price', linestyle='--')
    plt.title(f'Actual vs Predicted Stock Prices (Total Epochs: {total_epochs})')
    plt.xlabel('Time Step')
    plt.ylabel('Price')
    plt.legend()

    # 计算模型拟合效果评估参数
    rmse = np.sqrt(mean_squared_error(actual_close, predicted_close))  # RMSE
    mae = mean_absolute_error(actual_close, predicted_close)  # MAE
    r2 = r2_score(actual_close, predicted_close)  # R²
    mape = np.mean(np.abs((actual_close - predicted_close) / actual_close)) * 100  # MAPE

    # 生成评估参数信息字符串
    eval_metrics = (
        f"RMSE: {rmse:.4f}\n"
        f"MAE: {mae:.4f}\n"
        f"R²: {r2:.4f}\n"
        f"MAPE: {mape:.2f}%"
    )



    # 在图表的右侧添加参数信息和评估参数
    plt.text(
        x=1.05,  # x 坐标（1.0 是图表的右边界，1.05 表示稍微超出右边界）
        y=0.5,  # y 坐标（0.5 表示垂直居中）
        s=f"{params}\n\n{eval_metrics}",  # 参数信息和评估参数
        transform=plt.gca().transAxes,  # 使用相对坐标
        verticalalignment='center',  # 垂直居中
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)  # 添加背景框
    )

    # 保存图片
    plt.tight_layout()  # 自动调整布局
    plt.savefig(f"{save_path}/Total Epochs_{total_epochs}_prediction_comparison.png")
    plt.show()