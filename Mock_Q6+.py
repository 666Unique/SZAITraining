import pandas as pd
import numpy as np

# 生成20条简单的测试数据集
# 字段: Age(年龄), RiskLevel(风险等级)
data = pd.DataFrame({
    'Age': [23, 30, 28, 45, 52, 38, 61, 19, 47, 33,
            55, 42, 67, 25, 36, 50, 29, 58, 44, 31],
    'RiskLevel': ['低风险患者', '高风险患者', '低风险患者', '高风险患者', '低风险患者',
                  '低风险患者', '高风险患者', '低风险患者', '高风险患者', '低风险患者',
                  '高风险患者', '低风险患者', '高风险患者', '低风险患者', '低风险患者',
                  '高风险患者', '低风险患者', '高风险患者', '高风险患者', '低风险患者']
})

print("=" * 50)
print("生成的测试数据集（20条记录）：")
print("=" * 50)
print(data)
print(f"\n数据集行数: {len(data)}")
print(f"数据集列数: {len(data.columns)}")
print()

# ---------- Mock_Q6.py 中的代码逻辑 ----------
age_bins = [0, 26, 36, 46, 56, 66, np.inf]
age_labels = ['<=25', '26-35', '36-45', '46-55', '56-65', '<65']

# 1. 根据年龄值划分指定区间 
data["AgeRange"] = pd.cut(data['Age'], bins=age_bins, labels=age_labels, right=False) #cut

print("=" * 50)
print("添加 AgeRange 列后的数据：")
print("=" * 50)
print(data[['Age', 'AgeRange', 'RiskLevel']])
print()

# 2. 计算每个年龄区间高风险患者的比例
age_risk_rate = data.groupby('AgeRange')['RiskLevel'].apply(lambda x: (x == "高风险患者").mean()) # groupby

print("=" * 50)
print("每个年龄段高风险患者的比例：")
print("=" * 50)
print(age_risk_rate)
print()

# 3. 统计每个年龄区间的患者数量
age_patient_count = data['AgeRange'].value_counts().sort_index() #value_counts()

print("=" * 50)
print("每个年龄段的患者数量：")
print("=" * 50)
print(age_patient_count)
print()

# 汇总展示
print("=" * 50)
print("汇总结果：")
print("=" * 50)
summary = pd.DataFrame({
    '患者数量': age_patient_count,
    '高风险比例': age_risk_rate
})
print(summary)