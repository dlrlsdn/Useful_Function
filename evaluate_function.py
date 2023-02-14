# function for data evaluation

from sklearn import metrics as mm

print('Accuracy == gq \nSensitivity == gSE \nSpecificity == gSP \nPrecision == gpr \nROAUC == roauc \nF1 score == gfs')


def gq(test, predict):
    accuracy = mm.accuracy_score(test, predict)
    return accuracy


def gSE(test, predict):
    SE = mm.recall_score(test, predict)
    return SE


def gSP(test, predict):
    cm = mm.confusion_matrix(test, predict)
    SP = cm[0, 0] / (cm[0, 0] + cm[0, 1])
    return SP


def gpr(test, predict):
    precision = mm.precision_score(test, predict)
    return precision


def roauc(test, predict):
    ROAUC = mm.roc_auc_score(test, predict)
    return ROAUC


def gfs(test, predict):
    fscore = mm.f1_score(test, predict)
    return fscore
