import unittest
import logging.config
from tensorflow.python.framework import dtypes
from .traffic_lenet import Lenet
from .traffic_data import TrafficDataSets
from .traffic_data import DataSet
from .traffic_data import DataSetWithGenerator
from .traffic_data import TrafficDataRealFileProvider
logging.config.fileConfig('logging.conf')

real_data_provider = TrafficDataRealFileProvider(split_validation_from_train=True)

normal_dataset_factory = lambda X, y, dtype, grayscale: DataSet(X, y, dtype, grayscale)
keras_image_generator_dataset_factory = lambda X, y, dtype, grayscale: DataSetWithGenerator(X, y, dtype, grayscale)


class TestLenetBenchmark(unittest.TestCase):
    def test_lenet_normal_no_grayscale(self):
        """
        2016-12-28 11:32:58,681 - EPOCH 100 ...
        2016-12-28 11:32:58,682 - Validation loss = 31.360
        2016-12-28 11:32:58,682 - Validation accuracy = 0.880
        2016-12-28 11:33:03,870 - Test loss = 119.563
        2016-12-28 11:33:03,870 - Test accuracy = 0.751
        """
        lenet = Lenet(TrafficDataSets(real_data_provider, dtype=dtypes.float32, grayscale=False,
                                      dataset_factory=normal_dataset_factory))
        lenet.train()