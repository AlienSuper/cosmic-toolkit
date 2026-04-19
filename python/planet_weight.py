# python/planet_weight.py
import sys

# 星球重力转换因子 (地球 = 1.0)
# 外星小怪数据局提供，精确到小数点后两位，因为再多也记不住了
GRAVITY_FACTORS = {
    "水星": 0.38,
    "金星": 0.91,
    "火星": 0.38,
    "木星": 2.34,
    "土星": 1.06,
    "天王星": 0.92,
    "海王星": 1.19,
    "冥王星": 0.06, # 就算被开除球籍，外星小怪也记得你！
    "月球": 0.166 # 月球不是行星，但谁不想在月球上轻盈地跳跃呢？
}

def calculate_weight(earth_weight, planet):
    """计算在目标星球上的重量"""
    factor = GRAVITY_FACTORS.get(planet)
    if factor is None:
        return None
    return earth_weight * factor

def get_alien_comment(planet, weight):
    """外星小怪的专属点评"""
    comments = {
        "木星": f"哇！你在木星上重达{weight:.2f}公斤！建议不要站着，趴着会舒服点。",
        "火星": f"恭喜！在火星上你只有{weight:.2f}公斤！你可以吹嘘自己减肥成功了。",
        "月球": f"{weight:.2f}公斤！在月球上，你可以轻松打破地球的跳高记录！",
        "冥王星": f"只有{weight:.2f}公斤... 在冥王星上，小心别一用力就跳到外太空去了。"
    }
    return comments.get(planet, f"在这个星球上，你的体重是 {weight:.2f} 公斤。星际旅行愉快！")

def main():
    print("🌍 欢迎使用外星小怪的星球体重计算器！")
    
    # 检查是否通过命令行参数传入了体重
    if len(sys.argv) > 1:
        try:
            earth_weight = float(sys.argv[1])
        except ValueError:
            print("❌ 请输入一个有效的数字作为体重。")
            return
    else:
        # 如果没有参数，则交互式询问
        while True:
            try:
                earth_weight = float(input("👉 请输入你在地球上的体重(公斤): "))
                break
            except ValueError:
                print("❌ 请输入一个有效的数字，比如 70。")

    print("\n--- 正在扫描太阳系 ---")
    for planet in GRAVITY_FACTORS:
        weight = calculate_weight(earth_weight, planet)
        if weight:
            print(f"🪐 {planet}: {weight:.2f} 公斤")

    # 选择一个星球进行额外点评
    print("\n--- 外星小怪的点评 ---")
    # 默认点评木星，你也可以改成其他星球
    jupiter_weight = calculate_weight(earth_weight, "木星")
    print(get_alien_comment("木星", jupiter_weight))

if __name__ == "__main__":
    main()
