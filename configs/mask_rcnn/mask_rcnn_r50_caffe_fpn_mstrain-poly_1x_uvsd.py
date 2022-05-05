# -*-coding:utf-8-*-
_base_ = 'mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'

# 我们需要对头中的类别数量进行修改来匹配数据集的标注
model = dict(
    roi_head=dict(
    bbox_head=dict(num_classes=1),
    mask_head=dict(num_classes=1)))

# 修改数据集相关设置
dataset_type = 'CocoDataset'
classes = ('car',)
data = dict(
    train=dict(
        img_prefix='dataset/train/train_COCO/JPEGImages/',
        classes=classes,
        ann_file='dataset/train/train_COCO/annotations.json'),
    val=dict(
        img_prefix='dataset/val/val_COCO/JPEGImages/',
        classes=classes,
        ann_file='dataset/val/val_COCO/annotations.json'),
    test=dict(
        img_prefix='dataset/test/test_COCO/JPEGImages/',
        classes=classes,
        ann_file='dataset/test/test_COCO/annotations.json'))

# 我们可以使用预训练的 Mask R-CNN 来获取更好的性能
load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'