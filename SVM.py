import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Train\Train.csv')
graph = 'Graphs\SVM_ALL.png' # 需要手动修改数字以确定是哪几种工况

# 提取特征和标签
X = data.iloc[:, 1:6]  # 特征列第二列到第六列
y = data['label']  # 标签列第一列

# 标签编码
# 如果标签是字符串类型，必须进行编码
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=40)

# 初始化SVM分类器
svm_classifier = SVC(kernel='linear')

# 训练模型
svm_classifier.fit(X_train, y_train)

# 预测
y_pred = svm_classifier.predict(X_test)

# 评估模型
Acc = accuracy_score(y_test, y_pred)
print(f'Accuracy: {Acc}')
# 获取所有类别标签
all_labels = label_encoder.classes_
# 评估报告
# 明确指定labels参数
# 设置zero_division=1以避免警告
print('Classification Report:')
print(classification_report(y_test, y_pred, 
                            target_names=all_labels.astype(str), 
                            labels=range(len(all_labels)), 
                            zero_division=1))

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred)

# 绘制混淆矩阵
plt.figure(figsize=(8, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=all_labels, yticklabels=all_labels)
plt.title(f'SVM Method Confusion Matrix\nAccuracy: {Acc:.4f}')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.savefig(graph)
plt.show()
