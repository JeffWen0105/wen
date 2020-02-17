# Copyright (C) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in project root for information.


import sys
if sys.version >= '3':
    basestring = str

from pyspark.ml.param.shared import *
from pyspark import keyword_only
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from mmlspark.core.serialize.java_params_patch import *
from pyspark.ml.wrapper import JavaTransformer, JavaEstimator, JavaModel
from pyspark.ml.common import inherit_doc
from mmlspark.core.schema.Utils import *

@inherit_doc
class StratifiedRepartition(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """


    Args:

        labelCol (str): The name of the label column
        mode (str): Specify equal to repartition with replacement across all labels, specify original to keep the ratios in the original dataset, or specify mixed to use a heuristic (default: mixed)
        seed (long): random seed (default: 539887434)
    """

    @keyword_only
    def __init__(self, labelCol=None, mode="mixed", seed=539887434):
        super(StratifiedRepartition, self).__init__()
        self._java_obj = self._new_java_obj("com.microsoft.ml.spark.stages.StratifiedRepartition")
        self.labelCol = Param(self, "labelCol", "labelCol: The name of the label column")
        self.mode = Param(self, "mode", "mode: Specify equal to repartition with replacement across all labels, specify original to keep the ratios in the original dataset, or specify mixed to use a heuristic (default: mixed)")
        self._setDefault(mode="mixed")
        self.seed = Param(self, "seed", "seed: random seed (default: 539887434)")
        self._setDefault(seed=539887434)
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, labelCol=None, mode="mixed", seed=539887434):
        """
        Set the (keyword only) parameters

        Args:

            labelCol (str): The name of the label column
            mode (str): Specify equal to repartition with replacement across all labels, specify original to keep the ratios in the original dataset, or specify mixed to use a heuristic (default: mixed)
            seed (long): random seed (default: 539887434)
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    def setLabelCol(self, value):
        """

        Args:

            labelCol (str): The name of the label column

        """
        self._set(labelCol=value)
        return self


    def getLabelCol(self):
        """

        Returns:

            str: The name of the label column
        """
        return self.getOrDefault(self.labelCol)


    def setMode(self, value):
        """

        Args:

            mode (str): Specify equal to repartition with replacement across all labels, specify original to keep the ratios in the original dataset, or specify mixed to use a heuristic (default: mixed)

        """
        self._set(mode=value)
        return self


    def getMode(self):
        """

        Returns:

            str: Specify equal to repartition with replacement across all labels, specify original to keep the ratios in the original dataset, or specify mixed to use a heuristic (default: mixed)
        """
        return self.getOrDefault(self.mode)


    def setSeed(self, value):
        """

        Args:

            seed (long): random seed (default: 539887434)

        """
        self._set(seed=value)
        return self


    def getSeed(self):
        """

        Returns:

            long: random seed (default: 539887434)
        """
        return self.getOrDefault(self.seed)





    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.ml.spark.stages.StratifiedRepartition"

    @staticmethod
    def _from_java(java_stage):
        module_name=StratifiedRepartition.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".StratifiedRepartition"
        return from_java(java_stage, module_name)
