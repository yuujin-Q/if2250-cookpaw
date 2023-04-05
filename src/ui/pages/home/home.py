from ui.components.card.recipe_card import *
from ui.components.card.article_card import *
from ui.utils import getFont
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class Home(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        #set dashboard size
        self.setFixedWidth(int(0.95 * parentWidth))
        self.setFixedHeight(parentHeight)

        print(self.width())
        print(int(0.015 * self.width()))
        ## HEADER ##
        # home title
        home_title = QtWidgets.QLabel()
        home_title.setFont(getFont("Bold", 32))
        home_title.setFixedHeight(int(0.053 * parentHeight))
        home_title.setText("Welcome to CookPaw!")
        home_title.setObjectName("home_title")
        home_title.setStyleSheet("#home_title{color: #FFCF52;}")

        ## RECIPE SECTION ##
        # recipe heading #
        recipe_heading = QtWidgets.QLabel()
        recipe_heading.setFont(getFont("Bold", 24))
        recipe_heading.setObjectName("recipe_heading")
        recipe_heading.setStyleSheet("#recipe_heading{color: #F15D36;}")
        recipe_heading.setText("Check out our latest recipe collection")

        # spacer #
        recipe_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        # see all recipe #
        see_all_recipe_button = QtWidgets.QPushButton()
        see_all_recipe_button.setFont(getFont("Bold", 12))
        see_all_recipe_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        see_all_recipe_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        see_all_recipe_button.setAutoFillBackground(False)
        see_all_recipe_button.setText("See All Recipes")
        see_all_recipe_button.setObjectName("see_all_recipe_button")
        see_all_recipe_button.setStyleSheet("#see_all_recipe_button{color:#F15D36; background-color:transparent;}")

        ## layout recipe 
        recipe_layout = QtWidgets.QGridLayout()
        recipe_layout.addWidget(recipe_heading, 0, 0, 1, 1)
        recipe_layout.addItem(recipe_spacer, 0, 1, 1, 1)
        recipe_layout.addWidget(see_all_recipe_button, 0, 2, 1, 1)
        ## recipe card
        recipe_card_layout = QtWidgets.QGridLayout()
        recipe_card_layout.setSpacing(20)
        recipe_card_layout.setContentsMargins(0,0,0,0)
        for i in range (3):
            recipe = RecipeCard("assets/images/images_recipe/image_pork_belly.png", i, int(0.8 * self.width() / 3))
            recipe_card_layout.addWidget(recipe, 0, i, 1, 1)
        recipe_layout.addLayout(recipe_card_layout, 1, 0, 1, 3)

        ## ARTICLE SECTION ##
        # article heading #
        article_heading = QtWidgets.QLabel()
        article_heading.setFont(getFont("Bold", 24))
        article_heading.setObjectName("article_heading")
        article_heading.setStyleSheet("#article_heading{color: #29B067;}")
        article_heading.setText("Check out our latest article collection")

        # spacer #
        article_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        # see all article #
        see_all_article_button = QtWidgets.QPushButton()
        see_all_article_button.setFont(getFont("Bold", 12))
        see_all_article_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        see_all_article_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        see_all_article_button.setAutoFillBackground(False)
        see_all_article_button.setText("See All Articles")
        see_all_article_button.setObjectName("see_all_article_button")
        see_all_article_button.setStyleSheet("#see_all_article_button{color:#29B067; background-color:transparent;}")

        ## layout recipe 
        article_layout = QtWidgets.QGridLayout()
        article_layout.addWidget(article_heading, 0, 0, 1, 1)
        article_layout.addItem(article_spacer, 0, 1, 1, 1)
        article_layout.addWidget(see_all_article_button, 0, 2, 1, 1)
        ## article card
        article_card_layout = QtWidgets.QGridLayout()
        article_card_layout.setSpacing(20)
        article_card_layout.setContentsMargins(0,0,0,0)
        for i in range (3):
            article = ArticleCard("assets/images/images_article/image_smart_fridge.png", i, int(0.8 * self.width() / 3))
            article_card_layout.addWidget(article, 0, i, 1, 1)
        article_layout.addLayout(article_card_layout, 1, 0, 1, 3)
        ## dashboard layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(50,0,50,0)
        self.layout.addWidget(home_title)
        self.layout.addLayout(recipe_layout)
        self.layout.addLayout(article_layout)
        self.setLayout(self.layout)
    

   