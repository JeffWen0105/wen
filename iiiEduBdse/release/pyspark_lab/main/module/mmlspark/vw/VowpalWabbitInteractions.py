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
class VowpalWabbitInteractions(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """


    Args:

        inputCols (list): The names of the input columns
        numBits (int): Number of bits used to mask (default: 30)
        outputCol (str): The name of the output column
        sumCollisions (bool): Sums collisions if true, otherwise removes them (default: true)
    """

    @keyword_only
    def __init__(self, inputCols=None, numBits=30, outputCol=None, sumCollisions=True):
        super(VowpalWabbitInteractions, self).__init__()
        self._java_obj = self._new_java_obj("com.microsoft.ml.spark.vw.VowpalWabbitInteractions")
        self.inputCols = Param(self, "inputCols", "inputCols: The names of the input columns")
        self.numBits = Param(self, "numBits", "numBits: Number of bits used to mask (default: 30)")
        self._setDefault(numBits=30)
        self.outputCol = Param(self, "outputCol", "outputCol: The name of the output column")
        self.sumCollisions = Param(self, "sumCollisions", "sumCollisions: Sums collisions if true, otherwise removes them (default: true)")
        self._setDefault(sumCollisions=True)
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, inputCols=None, numBits=30, outputCol=None, sumCollisions=True):
        """
        Set the (keyword only) parameters

        Args:

            inputCols (list): The names of the input columns
            numBits (int): Number of bits used to mask (default: 30)
            outputCol (str): The name of the output column
            sumCollisions (bool): Sums collisions if true, otherwise removes them (default: true)
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    def setInputCols(self, value):
        """

        Args:

            inputCols (list): The names of the input columns

        """
        self._set(inputCols=value)
        return self


    def getInputCols(self):
        """

        Returns:

            list: The names of the input columns
        """
        return self.getOrDefault(self.inputCols)


    def setNumBits(self, value):
        """

        Args:

            numBits (int): Number of bits used to mask (default: 30)

        """
        self._set(numBits=value)
        return self


    def getNumBits(self):
        """

        Returns:

            int: Number of bits used to mask (default: 30)
        """
        return self.getOrDefault(self.numBits)


    def setOutputCol(self, value):
        """

        Args:

            outputCol (str): The name of the output column

        """
        self._set(outputCol=value)
        return self


    def getOutputCol(self):
        """

        Returns:

            str: The name of the output column
        """
        return self.getOrDefault(self.outputCol)


    def setSumCollisions(self, value):
        """

        Args:

            sumCollisions (bool): Sums collisions if true, otherwise removes them (default: true)

        """
        self._set(sumCollisions=value)
        return self


    def getSumCollisions(self):
        """

        Returns:

            bool: Sums collisions if true, otherwise removes them (default: true)
        """
        return self.getOrDefault(self.sumCollisions)





    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.ml.spark.vw.VowpalWabbitInteractions"

    @staticmethod
    def _from_java(java_stage):
        module_name=VowpalWabbitInteractions.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".VowpalWabbitInteractions"
        return from_java(java_stage, module_name)
