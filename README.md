# Leetcode 

## Python 环境设置

### 创建一个名为 leetcode 的 conda 环境

```bash
conda create --yes --name leetcode python=3.10
conda activate leetcode
```

### 设置 poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH" 
```

### 设置leetcode Python 环境

运行以下命令在 `leetcode` 的 Python 环境中安装 Python 包

```bash
poetry install
```

检查环境是否成功设置

```bash
poetry env info
```


```
python -m ipykernel install --name leetcode
```

## PostgreSQL 本地安装与设置

### 安装

```
brew install postgresql
```

### 启动

```
brew services start postgresql
```

```
psql -U postgres
```

```
CREATE USER leetcode WITH PASSWORD 'leetcode';
ALTER USER leetcode CREATEDB;


```
