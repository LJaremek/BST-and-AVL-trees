from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGraphicsSimpleTextItem, QGraphicsScene
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter
from ui_mapview import MapView

from node import Node

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Map of the tree")
        
        self.main_widget = QWidget()
        self.appBox = QVBoxLayout()
        self.appBox.maximumSize()
        self.main_widget.setLayout(self.appBox)

        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.map = MapView(self.page)
        self.appBox.addWidget(self.map)

        self._scene = QGraphicsScene()
        self.map.setScene(self._scene)
        self.map.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self.main_widget)


    def _get_width(self, height: int) -> int:
        return (2**(height-1))-1


    def _draw_node(self, node: Node, x: float, y: float):
        """
        Drawing the Node on the map.
        """
        text_item = QGraphicsSimpleTextItem()

        font = text_item.font()
        font.setPointSize(font.pointSize()-2)
        font.setPixelSize(self._font_size)

        text_item.setText(str(node.value()))
        text_item.setPos(x, y)
        text_item.setFont(font)

        self._scene.addItem(text_item)


    def _draw_line(self, x1: float, y1: float, x2: float, y2: float):
        """
        Drawing line from (x1, y1) point to (x2, y2) point.
        """
        self._scene.addLine(x1, y1, x2, y2)


    def draw_tree(self, tree, font_size=20):
        """
        Drawing tree.
        """
        self._font_size = font_size
        height = tree.height()
        width = self._get_width(height)*2
        top = tree.top()
        if top == None:
            return
        distance = 75
        start = y = 0
        x = -width*2
        deep = top.deep()
        sons = [top]
        while (sons != []) and (Node in [type(x) for x in sons]):
            son = sons.pop(0)
            if type(son) == int:
                sons += [son+1, son+1]
                if son != deep:
                    deep = son
                    width /= 2
                    start -= width
                    x = start
                    y += 1
                    continue
                else:
                    x += width*2
            else:
                if son.deep() != deep:
                    deep = son.deep()
                    width /= 2
                    start -= width
                    x = start
                    y += 1
                    son.set_x(x*distance)
                    son.set_y(y*distance)
                    self._draw_node(son, x*distance, y*distance)
                    if son.parent() != None:
                        self._draw_line(son.x(), son.y(), son.parent().x(), son.parent().y())
                else:
                    x += width*2
                    son.set_x(x*distance)
                    son.set_y(y*distance)
                    self._draw_node(son, x*distance, y*distance)
                    if son.parent() != None:
                        self._draw_line(son.x(), son.y(), son.parent().x(), son.parent().y())
                if son.left_son() == None:
                    sons.append(deep+1)
                else:
                    sons.append(son.left_son())
                if son.right_son() == None:
                    sons.append(deep+1)
                else:
                    sons.append(son.right_son())


def draw(tree, font_size=20):
    """
    Drawing tree in Qt window.
    """
    app = QApplication([])

    window = MainWindow()
    window.draw_tree(tree, font_size)
    window.show()

    app.exec_()
    exit()
