#!/bin/bash

echo "=========================================="
echo "🚀 开始配置服务器环境 (venv 模式)..."
echo "=========================================="

# 1. 检查并安装 python3-venv 工具 (防止服务器精简过头)
# 如果是 root 用户，尝试安装 venv 支持
if [ "$(id -u)" -eq 0 ]; then
    apt-get update && apt-get install -y python3-venv python3-pip unzip
fi

# 2. 创建虚拟环境 (文件夹名为 my_env)
if [ ! -d "my_env" ]; then
    echo "正在创建虚拟环境 my_env..."
    python3 -m venv my_env
else
    echo "虚拟环境 my_env 已存在。"
fi

# 3. 激活环境
echo "正在激活虚拟环境..."
source my_env/bin/activate

# 4. 升级 pip
pip install --upgrade pip

# 5. 安装 Linux 版 PyTorch (CUDA 12.1)
echo "正在安装 PyTorch..."
pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu121

# 6. 安装 requirements.txt
if [ -f "requirements.txt" ]; then
    echo "正在安装依赖库..."
    # 使用阿里云镜像加速，飞快
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
else
    echo "❌ 错误：没找到 requirements.txt"
    exit 1
fi

echo "=========================================="
echo "✅ 环境配置完成！"
echo "请按以下步骤运行："
echo "1. 激活环境: source my_env/bin/activate"
echo "2. 开始训练: nohup python run_ner.py --config conf/conll03.json > run.log 2>&1 &"
echo "=========================================="