import matplotlib.pyplot as plt
import matplotlib as mpl

# linux根据fname查不到matplotlib的文件夹，只能直接查到matplotlibrc，改里面的文件无法有效修改中文显示
# 索性直接用英文了。。
# mpl.rcParams['font.sans-serif'] = ["Droid Sans Fallback"]
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    # xy和xytext都以数据坐标为单位
    # nodeTxt箭头标记指向数据位置
    # xycoords 箭头尾部起点
    # xytext 对方框的设置参数

    # textcoodrd xytext位置的确定方法
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction',
                            # 字体位置 还有一个size未设置 采用默认参数
                            va="center", ha="center",
                            # bbox={}  代表对方框的设置
                            #         {
                            #             boxstyle= '' 代表边框的类型
                            #                     round 圆形方框
                            #                     rarrow箭头
                            #             fc  背景颜色   英文首字母 w -whiite r-red
                            #             ec 边框线的透明度  数字或颜色的首字母
                            #             alpha 字体的透明度
                            #             lw 线的粗细
                            #             rotation  角度
                            #         }
                            bbox=nodeType,
                            # 箭头参数设置 map
                            arrowprops=arrow_args)


def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    #创建子图块
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode(U'decisionNode', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode(U'treeNode', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()


def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = list(myTree.keys())
    secondDict = myTree[firstStr[0]]
    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


def getTreeDepth(myTree):
    maxDepth = 0
    thisDepth = 0
    firstStr = list(myTree.keys())
    secondDict = myTree[firstStr[0]]
    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            thisDepth += getTreeDepth(secondDict[key])
        else:
            thisDepth += 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth


def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                   {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
    return listOfTrees[i]

