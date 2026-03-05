# 模拟学生数据：班级、姓名、各科成绩
students = [
    {"class": "计科1班", "name": "张三", "score": {"语文": 88, "数学": 92, "英语": 58}},
    {"class": "计科1班", "name": "李四", "score": {"语文": 76, "数学": 55, "英语": 89}},
    {"class": "计科2班", "name": "王五", "score": {"语文": 90, "数学": 95, "英语": 93}},
    {"class": "计科2班", "name": "赵六", "score": {"语文": 45, "数学": 65, "英语": 60}},
]

# ======================
# 功能1：计算平均分 + 排名
# ======================
def show_rank():
    print("===== 学生平均分排名 =====")
    stu_list = []
    for s in students:
        total = sum(s["score"].values())
        avg = total / len(s["score"])
        stu_list.append({
            "name": s["name"],
            "class": s["class"],
            "avg": round(avg, 2)
        })

    # 按平均分从高到低排序
    stu_list.sort(key=lambda x: x["avg"], reverse=True)

    for i, stu in enumerate(stu_list, 1):
        print(f"第{i}名：{stu['name']}({stu['class']})，平均分：{stu['avg']}")
    print()

# ======================
# 功能2：按班级打印成绩单
# ======================
def print_by_class():
    print("===== 按班级打印成绩单 =====")
    classes = set(s["class"] for s in students)
    for c in classes:
        print(f"\n【{c}】")
        for s in students:
            if s["class"] == c:
                print(f"姓名：{s['name']}，成绩：{s['score']}")
    print()

# ======================
# 功能3：打印补考名单（<60分）
# ======================
def print_makeup():
    print("===== 补考名单 =====")
    for s in students:
        name = s["name"]
        cls = s["class"]
        for subject, score in s["score"].items():
            if score < 60:
                print(f"班级：{cls}　姓名：{name}　补考科目：{subject}")
    print()

# ======================
# 主菜单
# ======================
while True:
    print("===== 学生成绩管理系统 =====")
    print("1. 查看平均分与排名")
    print("2. 按班级打印成绩单")
    print("3. 打印补考名单")
    print("0. 退出")
    choice = input("请输入功能编号：")

    if choice == "1":
        show_rank()
    elif choice == "2":
        print_by_class()
    elif choice == "3":
        print_makeup()
    elif choice == "0":
        print("退出系统")
        break
    else:
        print("输入错误，请重新输入！")