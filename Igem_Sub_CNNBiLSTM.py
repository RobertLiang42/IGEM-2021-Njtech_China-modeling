import keras
import pandas as pd
import numpy as np
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.callbacks import ReduceLROnPlateau


def CNNBiLSTM():
    df = pd.read_csv('Data.csv')
    X = df['Promoter sequence'].values
    Y = df['cluster'].values

    # 混合模型，先用CNN的方法处理数据
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

        cb = models.Sequential()
        cb.add(layers.Conv1D(filters=16, kernel_size=6, activation='relu', padding='same', input_shape=(2935, 4)))
        cb.add(layers.Conv1D(filters=16, kernel_size=12, activation='relu', padding='same'))

        cb.add(layers.Flatten())
        cb.add(layers.Dense(32, activation='relu'))
        cb.add(layers.Dense(16, activation='softmax'))

        # 强行更改输入维度，将两模型链接，目前的情况是，虽然不管怎么调结果都是0.5294左右，但是将cnn放在上面训练速度与cnn相似，将lstm放在上面则训练时间接近于lstm（2分钟）
        cb.add(keras.layers.Reshape((1, 16)))

        cb.add(
            layers.Bidirectional(
                layers.LSTM(64, return_sequences=True, activation='tanh')
            )
        )

        cb.add(layers.Dense(32, activation='relu'))

        cb.add(layers.Dense(16, activation='softmax'))

        reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.5, patience=5, mode='auto')

        print(cb.summary())

        from Igem_Sub_LossHistory import LossHistory
        history = LossHistory()

        cb.compile(
            loss='sparse_categorical_crossentropy',
            optimizer=keras.optimizers.Adam(lr=0.0001),
            metrics=["accuracy"]
        )

        cb.fit(X_train, Y_train, batch_size=16, epochs=10, verbose=2, callbacks=[reduce_lr])
        # cb.fit(X_train, Y_train, batch_size=16, epochs=10, verbose=2, callbacks=[history])

        # history.loss_plot('epoch')  # 作acc-loss图

        evaluate = cb.evaluate(X_test, Y_test)

        Y_pred = cb.predict(X_test)
        a = len(Y_pred)
        Y_pred = Y_pred.reshape(a, 16)  # 从(43,1,16)改成·(43,16)

        Y_score = [np.argmax(element) for element in Y_pred]

        from sklearn.metrics import classification_report
        import warnings

        warnings.simplefilter('ignore')
        print("Classification Report: \n", classification_report(Y_test, Y_score))

        Y_score = pd.DataFrame(Y_score, columns=['Pred'])
        Y_test = pd.DataFrame(Y_test, columns=['Real'])
        Fold_result = pd.concat([Y_test, Y_score], axis=1)
        result.append(Fold_result)

    CNNBiLSTM_result = pd.concat(result, axis=0)
    CNNBiLSTM_result.to_csv('CNNBiLSTM_result.csv')

    import Igem_Sub_ROC as roc
    roc.ROC('CNNBiLSTM_result.csv', 'CNN - Bidirectional LSTM')


