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
class VowpalWabbitFeaturizer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """


    Args:

        inputCols (list): The names of the input columns (default: [Ljava.lang.String;@114dc88e)
        numBits (int): Number of bits used to mask (default: 30)
        outputCol (str): The name of the output column (default: features)
        prefixStringsWithColumnName (bool): Prefix string features with column name (default: true)
        preserveOrderNumBits (int): Number of bits used to preserve the feature order. This will reduce the hash size. Needs to be large enough to fit count the maximum number of words (default: 0)
        seed (int): Hash seed (default: 0)
        stringSplitInputCols (list): Input cols that should be split at word boundaries (default: [Ljava.lang.String;@2b8dec87)
        sumCollisions (bool): Sums collisions if true, otherwise removes them (default: true)
    """

    @keyword_only
    def __init__(self, inputCols=[], numBits=30, outputCol="features", prefixStringsWithColumnName=True, preserveOrderNumBits=0, seed=0, stringSplitInputCols=[], sumCollisions=True):
        super(VowpalWabbitFeaturizer, self).__init__()
        self._java_obj = self._new_java_obj("com.microsoft.ml.spark.vw.VowpalWabbitFeaturizer")
        self.inputCols = Param(self, "inputCols", "inputCols: The names of the input columns (default: [Ljava.lang.String;@114dc88e)")
        self._setDefault(inputCols=[])
        self.numBits = Param(self, "numBits", "numBits: Number of bits used to mask (default: 30)")
        self._setDefault(numBits=30)
        self.outputCol = Param(self, "outputCol", "outputCol: The name of the output column (default: features)")
        self._setDefault(outputCol="features")
        self.prefixStringsWithColumnName = Param(self, "prefixStringsWithColumnName", "prefixStringsWithColumnName: Prefix string features with column name (default: true)")
        self._setDefault(prefixStringsWithColumnName=True)
        self.preserveOrderNumBits = Param(self, "preserveOrderNumBits", "preserveOrderNumBits: Number of bits used to preserve the feature order. This will reduce the hash size. Needs to be large enough to fit count the maximum number of words (default: 0)")
        self._setDefault(preserveOrderNumBits=0)
        self.seed = Param(self, "seed", "seed: Hash seed (default: 0)")
        self._setDefault(seed=0)
        self.stringSplitInputCols = Param(self, "stringSplitInputCols", "stringSplitInputCols: Input cols that should be split at word boundaries (default: [Ljava.lang.String;@2b8dec87)")
        self._setDefault(stringSplitInputCols=[])
        self.sumCollisions = Param(self, "sumCollisions", "sumCollisions: Sums collisions if true, otherwise removes them (default: true)")
        self._setDefault(sumCollisions=True)
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, inputCols=[], numBits=30, outputCol="features", prefixStringsWithColumnName=True, preserveOrderNumBits=0, seed=0, stringSplitInputCols=[], sumCollisions=True):
        """
        Set the (keyword only) parameters

        Args:

            inputCols (list): The names of the input columns (default: [Ljava.lang.String;@114dc88e)
            numBits (int): Number of bits used to mask (default: 30)
            outputCol (str): The name of the output column (default: features)
            prefixStringsWithColumnName (bool): Prefix string features with column name (default: true)
            preserveOrderNumBits (int): Number of bits used to preserve the feature order. This will reduce the hash size. Needs to be large enough to fit count the maximum number of words (default: 0)
            seed (int): Hash seed (default: 0)
            stringSplitInputCols (list): Input cols that should be split at word boundaries (default: [Ljava.lang.String;@2b8dec87)
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

            inputCols (list): The names of the input columns (default: [Ljava.lang.String;@114dc88e)

        """
        self._set(inputCols=value)
        return self


    def getInputCols(self):
        """

        Returns:

            list: The names of the input columns (default: [Ljava.lang.String;@114dc88e)
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

            outputCol (str): The name of the output column (default: features)

        """
        self._set(outputCol=value)
        return self


    def getOutputCol(self):
        """

        Returns:

            str: The name of the output column (default: features)
        """
        return self.getOrDefault(self.outputCol)


    def setPrefixStringsWithColumnName(self, value):
        """

        Args:

            prefixStringsWithColumnName (bool): Prefix string features with column name (default: true)

        """
        self._set(prefixStringsWithColumnName=value)
        return self


    def getPrefixStringsWithColumnName(self):
        """

        Returns:

            bool: Prefix string features with column name (default: true)
        """
        return self.getOrDefault(self.prefixStringsWithColumnName)


    def setPreserveOrderNumBits(self, value):
        """

        Args:

            preserveOrderNumBits (int): Number of bits used to preserve the feature order. This will reduce the hash size. Needs to be large enough to fit count the maximum number of words (default: 0)

        """
        self._set(preserveOrderNumBits=value)
        return self


    def getPreserveOrderNumBits(self):
        """

        Returns:

            int: Number of bits used to preserve the feature order. This will reduce the hash size. Needs to be large enough to fit count the maximum number of words (default: 0)
        """
        return self.getOrDefault(self.preserveOrderNumBits)


    def setSeed(self, value):
        """

        Args:

            seed (int): Hash seed (default: 0)

        """
        self._set(seed=value)
        return self


    def getSeed(self):
        """

        Returns:

            int: Hash seed (default: 0)
        """
        return self.getOrDefault(self.seed)


    def setStringSplitInputCols(self, value):
        """

        Args:

            stringSplitInputCols (list): Input cols that should be split at word boundaries (default: [Ljava.lang.String;@2b8dec87)

        """
        self._set(stringSplitInputCols=value)
        return self


    def getStringSplitInputCols(self):
        """

        Returns:

            list: Input cols that should be split at word boundaries (default: [Ljava.lang.String;@2b8dec87)
        """
        return self.getOrDefault(self.stringSplitInputCols)


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
        return "com.microsoft.ml.spark.vw.VowpalWabbitFeaturizer"

    @staticmethod
    def _from_java(java_stage):
        module_name=VowpalWabbitFeaturizer.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".VowpalWabbitFeaturizer"
        return from_java(java_stage, module_name)
