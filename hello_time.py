import datetime

def main():
    print("=" * 40)
    print("Hello World!")
    print("=" * 40)
    
    # 获取当前时间
    now = datetime.datetime.now()
    
    # 输出不同格式的时间信息
    print(f"当前日期和时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"当前日期: {now.strftime('%Y年%m月%d日')}")
    print(f"当前时间: {now.strftime('%H时%M分%S秒')}")
    
    # 星期几（中文）
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    print(f"今天是: {weekdays[now.weekday()]}")
    
    # 时间戳
    print(f"时间戳: {int(now.timestamp())}")
    
    print("=" * 40)

if __name__ == "__main__":
    main()
