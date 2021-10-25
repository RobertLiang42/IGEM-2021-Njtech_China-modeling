import pandas as pd
import numpy as np
from tensorflow.keras import datasets, layers, models





def CNN():
    # 读取X,Y
    df = pd.read_csv('Data.csv')
    X = df['Promoter sequence'].values
    Y = df['cluster'].values

    # 数据处理

    # 对X静音
    import Igem_Sub_Mute as mt
    X = mt.mute(mt.pre(X))
    # 序列转2维平面
    import Igem_Sub_Seq2Array as s2a
    X = s2a.Seq2Array(X)

    from sklearn.model_selection import StratifiedKFold
    KFolds = StratifiedKFold(n_splits=5)  # 5 fold
    fold_counter = 0
    result = []

    for train, test in KFolds.split(X, Y):
        fold_counter += 1
        print(f"fold #{fold_counter}")

        X_train, X_test, Y_train, Y_test = X[train], X[test], Y[train], Y[test]

        cnn = models.Sequential([
            layers.Conv1D(filters=16, kernel_size=6, activation='relu', padding='same', input_shape=(2935, 4)),

            layers.Conv1D(filters=16, kernel_size=12, activation='relu', padding='same'),

            layers.Flatten(),
            layers.Dense(16, activation='relu'),
            layers.Dense(10, activation='softmax')
        ])

        print(cnn.summary())

        from Igem_Sub_LossHistory import LossHistory
        history = LossHistory()

        cnn.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

        cnn.fit(X_train, Y_train, epochs=10, callbacks=[history])

        evaluate = cnn.evaluate(X_test, Y_test)

        # history.loss_plot('epoch') #作acc-loss图

        Y_pred = cnn.predict(X_test)

        Y_score = [np.argmax(element) for element in Y_pred]

        from sklearn.metrics import confusion_matrix, classification_report
        import warnings
        warnings.simplefilter('ignore')
        print("Classification Report: \n", classification_report(Y_test, Y_score))

        Y_score = pd.DataFrame(Y_score, columns=['Pred'])
        Y_test = pd.DataFrame(Y_test, columns=['Real'])
        Fold_result = pd.concat([Y_test, Y_score], axis=1)
        result.append(Fold_result)

    CNN_result = pd.concat(result, axis=0)
    CNN_result.to_csv('CNN_result.csv')

    import Igem_Sub_ROC as roc
    roc.ROC('CNN_result.csv', 'CNN')