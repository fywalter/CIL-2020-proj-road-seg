# encoding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path as osp
import sys
import time
import numpy as np
from easydict import EasyDict as edict
import argparse

import torch.utils.model_zoo as model_zoo

C = edict()
config = C
cfg = C

C.seed = 304

"""please config ROOT_dir and user when u first using"""
C.repo_name = 'TorchSeg'
C.abs_dir = osp.realpath(".")
C.this_dir = C.abs_dir.split(osp.sep)[-1]
C.root_dir = C.abs_dir[:C.abs_dir.index(C.repo_name) + len(C.repo_name)]
C.log_dir = osp.abspath(osp.join(C.root_dir, 'log', C.this_dir))
C.log_dir_link = osp.join(C.abs_dir, 'log')
C.snapshot_dir = osp.abspath(osp.join(C.log_dir, "all_snapshot"))

exp_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
C.log_file = C.log_dir + '/log_' + exp_time + '.log'
C.link_log_file = C.log_file + '/log_last.log'
C.val_log_file = C.log_dir + '/val_' + exp_time + '.log'
C.link_val_log_file = C.log_dir + '/val_last.log'

"""Data Dir and Weight Dir"""
C.dataset_path = osp.join(C.root_dir, 'cil')
# C.img_root_folder = osp.join(C.dataset_path, 'training/images/')
C.img_root_folder = C.dataset_path
C.gt_root_folder = C.dataset_path
# C.train_source = osp.join(C.dataset_path, "train_edge_midline.txt")
C.train_source = osp.join(C.dataset_path, "train_edge_midline_all.txt")
C.eval_source = osp.join(C.dataset_path, "val_edge_midline.txt")
C.test_source = osp.join(C.dataset_path, "test.txt")
C.is_test = False

"""Path Config"""


def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)


add_path(osp.join(C.root_dir, 'furnace'))

from utils.pyt_utils import model_urls

"""Image Config"""
C.num_classes = 2
C.background = -1
C.image_mean = np.array([0.485, 0.456, 0.406])  # 0.485, 0.456, 0.406
C.image_std = np.array([0.229, 0.224, 0.225])
C.image_height = 400
C.image_width = 400
C.gt_down_sampling = 1
# C.num_train_imgs = 90
C.num_train_imgs = 100
C.num_eval_imgs = 10

""" Settings for network, this would be different for each kind of model"""
C.fix_bias = True
C.fix_bn = False
C.sync_bn = True
C.bn_eps = 1e-5
C.bn_momentum = 0.1
C.pretrained_model = osp.join(C.root_dir, "model_zoo", "resnet101_v1c.pth")


"""Train Config"""
C.lr = 1e-3
C.lr_power = 0.9
C.momentum = 0.9
C.weight_decay = 1e-4
C.batch_size = 4
C.nepochs = 4000
C.niters_per_epoch = int(np.ceil(C.num_train_imgs // C.batch_size))
C.num_workers = 24
C.train_scale_array = [0.5, 0.75, 1, 1.5, 1.75, 2]

"""Eval Config"""
C.eval_iter = 30
C.eval_flip = False
C.eval_height = 400
C.eval_width = 400
# C.eval_base_size = 480
# C.eval_crop_size = 480

"""Display Config"""
C.snapshot_iter = 200
C.record_info_iter = 200
C.display_iter = 200


def open_tensorboard():
    pass


if __name__ == '__main__':
    print(config.epoch_num)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-tb', '--tensorboard', default=False, action='store_true')
    args = parser.parse_args()

    if args.tensorboard:
        open_tensorboard()
