import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score, auc, RocCurveDisplay
import pandas as pd



def ROC_ALL():
    class_RF = pd.read_csv('Random Forest class all.csv')
    class_CNN = pd.read_csv('CNN class all.csv')
    class_BiGRU = pd.read_csv('Bidirctional GRU class all.csv')
    class_CNNBiLSTM = pd.read_csv('CNN - Bidirectional LSTM class all.csv')


    plt.figure(figsize=(10, 10))  # 放大图片，防止图例遮挡曲线

    fpr_RF, tpr_RF, _ = roc_curve(class_RF['pred'], class_RF['real'])
    AUC_RF = auc(fpr_RF, tpr_RF)
    plt.plot(fpr_RF, tpr_RF,
             label='Random Forest ROC curve (area = {0:0.2f})'
                   ''.format(AUC_RF),
             color='aqua', linestyle='-', linewidth=4)

    fpr_CNN, tpr_CNN, _ = roc_curve(class_CNN['pred'], class_CNN['real'])
    AUC_CNN = auc(fpr_CNN, tpr_CNN)
    plt.plot(fpr_CNN, tpr_CNN,
             label='CNN ROC curve (area = {0:0.2f})'
                   ''.format(AUC_CNN),
             color='deeppink', linestyle='--', linewidth=4)

    fpr_BiGRU, tpr_BiGRU, _ = roc_curve(class_BiGRU['pred'], class_BiGRU['real'])
    AUC_BiGRU = auc(fpr_BiGRU, tpr_BiGRU)
    plt.plot(fpr_BiGRU, tpr_BiGRU,
             label='Bidirctional GRU ROC curve (area = {0:0.2f})'
                   ''.format(AUC_BiGRU),
             color='cornflowerblue', linestyle=':', linewidth=4)

    fpr_CNNBiLSTM, tpr_CNNBiLSTM, _ = roc_curve(class_CNNBiLSTM['pred'], class_CNNBiLSTM['real'])
    AUC_CNNBiLSTM = auc(fpr_CNNBiLSTM, tpr_CNNBiLSTM)
    plt.plot(fpr_CNNBiLSTM, tpr_CNNBiLSTM,
             label='CNN - Bidirectional LSTM ROC curve (area = {0:0.2f})'
                   ''.format(AUC_CNNBiLSTM),
             color='darkorange', linestyle='-.', linewidth=4)



    # Title
    plt.title('ROC Curve for all models')
    # Axis labels
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    # Show legend
    plt.legend()  #
    # Show plot
    plt.show()
