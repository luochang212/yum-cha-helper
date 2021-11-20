# 饮茶提醒小助手

MacOS 版饮茶提醒小助手

还在为每天忘记饮茶而感到痛苦吗？还不快来试试这个！！！

## Features

- 当然她也可以是 刷题 / 健身 / 睡觉 提醒小助手
- 自带横幅效果，语音提醒可选（命令后加 `-s` 触发语音效果）
- 有其他口音，看你的喜好AND系统是否支持了

![](/img/screenshot.png)

## Directory tree

```bash
├── README.md
├── conf
│   └── set.conf
├── img
│   └── screenshot.png
├── log
│   ├── helper.err
│   └── helper.log
├── requirement.txt
└── src
    └── helper.py
```

## Usage

1. 确保 Python 版本 >= 3.7
2. 安装 pyttsx3 包（如果没安）：`pip install pyttsx3`
3. 打开配置文件 `./conf/set.conf`，设置提醒文案
4. 在 cron 中为主程序 `./src/helper.py` 添加定时任务

## Tips

工作期间启动此脚本可被动触发社牛效果
