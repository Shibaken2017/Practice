'''
K_measn法の実装。
各要素の特徴ベクトル、名前、一意に識別するためのidを保持するためのクラス
'''
import numpy as np
import math
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

class Element:
    def __init__(self,id,name,position):
        '''

        :param id:
        :param name:
        :param position:t位置ベクトル
        '''
        self.id=id
        self.name=name
        self.position=position
        #key:各重心のid
        # valuer:その重心との距離
        self.distance_dict={}
        #所属しているクラスタとの距離
        self.min_dist=0
