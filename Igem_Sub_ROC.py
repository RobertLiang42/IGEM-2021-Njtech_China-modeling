import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score, auc, RocCurveDisplay
import pandas as pd



def ROC(modelfile, modelname):
    model_result = pd.read_csv(modelfile)
    real = model_result['Real'].values.tolist()
    pred = model_result['Pred'].values.tolist()

    class_0 = []
    class_1 = []
    class_2 = []
    class_3 = []
    class_4 = []

    # 一行一行添加数据，用字典加列表转换更方便
    # rows_list = []
    # for row in input_rows:
    #
    #         dict1 = {}
    #         # get input row in dictionary format
    #         # key = col_name
    #         dict1.update(blah..)
    #
    #         rows_list.append(dict1)
    #
    # df = pd.DataFrame(rows_list)

    # 对0组进行pull
    # 0组 real
    for i in range(len(real)):
        if real[i] == 0:
            if pred[i] == 0:
                dict = {'real': 1, 'pred': 1}
                class_0.append(dict)
                dict = {'real': 0, 'pred': 0}
                class_0.append(dict)
            else:
                dict = {'real': 1, 'pred': 0}
                class_0.append(dict)
                class_0.append(dict)
    # 0组 pred
    for i in range(len(real)):
        if pred[i] == 0:
            if real[i] == 0:
                dict = {'real': 1, 'pred': 1}
                class_0.append(dict)
                dict = {'real': 0, 'pred': 0}
                class_0.append(dict)
            else:
                dict = {'real': 0, 'pred': 1}
                class_0.append(dict)
                class_0.append(dict)

    class_0 = pd.DataFrame(class_0)

    # 对1组进行pull
    # 1组 real
    for i in range(len(real)):
        if real[i] == 1:
            if pred[i] == 1:
                dict = {'real': 1, 'pred': 1}
                class_1.append(dict)
                dict = {'real': 0, 'pred': 0}
                class_1.append(dict)
            else:
                dict = {'real': 1, 'pred': 0}
                class_1.append(dict)
                class_1.append(dict)
    # 1组 pred
    for i in range(len(real)):
        if pred[i] == 1:
            if real[i] == 1:
                dict = {'real': 1, 'pred': 1}
                class_1.append(dict)
                dict = {'real': 0, 'pred': 0}
                class_1.append(dict)
            else:
                dict = {'real': 0, 'pred': 1}
                class_1.append(dict)
                class_1.append(dict)

    class_1 = pd.DataFrame(class_1)

    # 对2组进行pull
    # 2组 real
    for i in range(len(real)):
        if real[i] == 2:
            if pred[i] == 2:
                dict = {'real': 1, 'pred': 1}
                class_2.append(dict)
                dict = {'real': 0, 'pred': 0}
                class_2.append(dict)
            else:
                dict = {'real': 1, 'pred': 0}
                class_2.append(dict)
                class_2.append(dict)
    # 1组 pred
    for i in range(len(real)):
        if pred[i] == 2:
            if real[i] == 2:
                dict = {'real': 1, 'pred': 1}
                class_2.append(dict)
                dict = {'real': 0, 'pred': 0}
                class_2.append(dict)
            else:
                dict = {'real': 0, 'pred': 1}
                class_2.append(dict)
                class_2.append(dict)

    class_2 = pd.DataFrame(class_2)

    # 对3组进行pull
    # 3组 real
    for i in range(len(real)):
        if real[i] == 3:
            if pred[i] == 3:
                dict = {'real': 1, 'pred': 1}
                class_3.append(dict)
                dict = {'real': 0, 'pred': 0}
                class_3.append(dict)
            else:
                dict = {'real': 1, 'pred': 0}
                class_3.append(dict)
                class_3.append(dict)
    # 1组 pred
    for i in range(len(real)):
        if pred[i] == 3:
            if real[i] == 3:
                dict = {'real': 1, 'pred': 1}
                class_3.append(dict)
                dict = {'real': 0, 'pred': 0}
                class_3.append(dict)
            else:
                dict = {'real': 0, 'pred': 1}
                class_3.append(dict)
                class_3.append(dict)

    class_3 = pd.DataFrame(class_3)

    # 对4组进行pull
    # 4组 real
    for i in range(len(real)):
        if real[i] == 4:
            if pred[i] == 4:
                dict = {'real': 1, 'pred': 1}
                class_4.append(dict)
                dict = {'real': 0, 'pred': 0}
                class_4.append(dict)
            else:
                dict = {'real': 1, 'pred': 0}
                class_4.append(dict)
                class_4.append(dict)
    # 1组 pred
    for i in range(len(real)):
        if pred[i] == 4:
            if real[i] == 4:
                dict = {'real': 1, 'pred': 1}
                class_4.append(dict)
                dict = {'real': 0, 'pred': 0}
                class_4.append(dict)
            else:
                dict = {'real': 0, 'pred': 1}
                class_4.append(dict)
                class_4.append(dict)

    class_4 = pd.DataFrame(class_4)

    # (55+15+9+3+2)/2 = 43 整个刚好被弄了两次

    class_all = pd.concat([class_0, class_1, class_2, class_3, class_4], axis=0)

    # print(roc_auc_score(class_0['real'], class_0['pred']))
    # print(roc_auc_score(class_1['real'], class_1['pred']))
    # print(roc_auc_score(class_2['real'], class_2['pred']))
    # print(roc_auc_score(class_3['real'], class_3['pred']))
    # print(roc_auc_score(class_4['real'], class_4['pred']))
    # print(roc_auc_score(class_all['real'], class_all['pred']))

    plt.figure(figsize=(10, 10))  # 放大图片，防止图例遮挡曲线
    fpr, tpr, _ = roc_curve(class_all['pred'], class_all['real'])
    AUC = auc(fpr, tpr)
    plt.plot(fpr, tpr,
             label='total ROC curve (area = {0:0.2f})'
                   ''.format(AUC),
             color='darkorange', linestyle='-', linewidth=4)

    fpr_0, tpr_0, _ = roc_curve(class_0['pred'], class_0['real'])
    AUC_0 = auc(fpr_0, tpr_0)
    plt.plot(fpr_0, tpr_0,
             label='class 0 ROC curve (area = {0:0.2f})'
                   ''.format(AUC_0),
             color='deeppink', linestyle=':', linewidth=2)

    fpr_1, tpr_1, _ = roc_curve(class_1['pred'], class_1['real'])
    AUC_1 = auc(fpr_1, tpr_1)
    plt.plot(fpr_1, tpr_1,
             label='class 1 ROC curve (area = {0:0.2f})'
                   ''.format(AUC_1),
             color='aqua', linestyle=':', linewidth=2)

    fpr_2, tpr_2, _ = roc_curve(class_2['pred'], class_2['real'])
    AUC_2 = auc(fpr_2, tpr_2)
    plt.plot(fpr_2, tpr_2,
             label='class 2 ROC curve (area = {0:0.2f})'
                   ''.format(AUC_2),
             color='cornflowerblue', linestyle=':', linewidth=2)

    fpr_3, tpr_3, _ = roc_curve(class_3['pred'], class_3['real'])
    AUC_3 = auc(fpr_3, tpr_3)
    plt.plot(fpr_3, tpr_3,
             label='class 3 ROC curve (area = {0:0.2f})'
                   ''.format(AUC_3),
             color='violet', linestyle=':', linewidth=2)

    fpr_4, tpr_4, _ = roc_curve(class_4['pred'], class_4['real'])
    AUC_4 = auc(fpr_4, tpr_4)
    plt.plot(fpr_4, tpr_4,
             label='class 4 ROC curve (area = {0:0.2f})'
                   ''.format(AUC_4),
             color='tomato', linestyle=':', linewidth=2)

    # Title
    plt.title('ROC Curve for {}'.format(modelname))
    # Axis labels
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    # Show legend
    plt.legend()  #
    # Show plot
    plt.show()

    class_all.to_csv('{} class all.csv'.format(modelname))