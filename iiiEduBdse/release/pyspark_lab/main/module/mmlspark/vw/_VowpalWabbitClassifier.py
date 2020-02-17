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
class _VowpalWabbitClassifier(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """


    Args:

        additionalFeatures (list): Additional feature columns (default: [Ljava.lang.String;@372a2a71)
        args (str): VW command line arguments passed (default: )
        featuresCol (str): features column name (default: features)
        hashSeed (int): Seed used for hashing (default: 0)
        ignoreNamespaces (str): Namespaces to be ignored (first letter only)
        initialModel (list): Initial model to start from
        interactions (list): Interaction terms as specified by -q
        l1 (double): l_1 lambda
        l2 (double): l_2 lambda
        labelCol (str): label column name (default: label)
        labelConversion (bool): Convert 0/1 Spark ML style labels to -1/1 VW style labels. Defaults to true. (default: true)
        learningRate (double): Learning rate
        numBits (int): Number of bits used (default: 18)
        numPasses (int): Number of passes over the data (default: 1)
        powerT (double): t power value
        predictionCol (str): prediction column name (default: prediction)
        probabilityCol (str): Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities (default: probability)
        rawPredictionCol (str): raw prediction (a.k.a. confidence) column name (default: rawPrediction)
        thresholds (list): Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
        weightCol (str): The name of the weight column
    """

    @keyword_only
    def __init__(self, additionalFeatures=[], args="", featuresCol="features", hashSeed=0, ignoreNamespaces=None, initialModel=None, interactions=None, l1=None, l2=None, labelCol="label", labelConversion=True, learningRate=None, numBits=18, numPasses=1, powerT=None, predictionCol="prediction", probabilityCol="probability", rawPredictionCol="rawPrediction", thresholds=None, weightCol=None):
        super(_VowpalWabbitClassifier, self).__init__()
        self._java_obj = self._new_java_obj("com.microsoft.ml.spark.vw.VowpalWabbitClassifier")
        self.additionalFeatures = Param(self, "additionalFeatures", "additionalFeatures: Additional feature columns (default: [Ljava.lang.String;@372a2a71)")
        self._setDefault(additionalFeatures=[])
        self.args = Param(self, "args", "args: VW command line arguments passed (default: )")
        self._setDefault(args="")
        self.featuresCol = Param(self, "featuresCol", "featuresCol: features column name (default: features)")
        self._setDefault(featuresCol="features")
        self.hashSeed = Param(self, "hashSeed", "hashSeed: Seed used for hashing (default: 0)")
        self._setDefault(hashSeed=0)
        self.ignoreNamespaces = Param(self, "ignoreNamespaces", "ignoreNamespaces: Namespaces to be ignored (first letter only)")
        self.initialModel = Param(self, "initialModel", "initialModel: Initial model to start from")
        self.interactions = Param(self, "interactions", "interactions: Interaction terms as specified by -q")
        self.l1 = Param(self, "l1", "l1: l_1 lambda")
        self.l2 = Param(self, "l2", "l2: l_2 lambda")
        self.labelCol = Param(self, "labelCol", "labelCol: label column name (default: label)")
        self._setDefault(labelCol="label")
        self.labelConversion = Param(self, "labelConversion", "labelConversion: Convert 0/1 Spark ML style labels to -1/1 VW style labels. Defaults to true. (default: true)")
        self._setDefault(labelConversion=True)
        self.learningRate = Param(self, "learningRate", "learningRate: Learning rate")
        self.numBits = Param(self, "numBits", "numBits: Number of bits used (default: 18)")
        self._setDefault(numBits=18)
        self.numPasses = Param(self, "numPasses", "numPasses: Number of passes over the data (default: 1)")
        self._setDefault(numPasses=1)
        self.powerT = Param(self, "powerT", "powerT: t power value")
        self.predictionCol = Param(self, "predictionCol", "predictionCol: prediction column name (default: prediction)")
        self._setDefault(predictionCol="prediction")
        self.probabilityCol = Param(self, "probabilityCol", "probabilityCol: Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities (default: probability)")
        self._setDefault(probabilityCol="probability")
        self.rawPredictionCol = Param(self, "rawPredictionCol", "rawPredictionCol: raw prediction (a.k.a. confidence) column name (default: rawPrediction)")
        self._setDefault(rawPredictionCol="rawPrediction")
        self.thresholds = Param(self, "thresholds", "thresholds: Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold")
        self.weightCol = Param(self, "weightCol", "weightCol: The name of the weight column")
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, additionalFeatures=[], args="", featuresCol="features", hashSeed=0, ignoreNamespaces=None, initialModel=None, interactions=None, l1=None, l2=None, labelCol="label", labelConversion=True, learningRate=None, numBits=18, numPasses=1, powerT=None, predictionCol="prediction", probabilityCol="probability", rawPredictionCol="rawPrediction", thresholds=None, weightCol=None):
        """
        Set the (keyword only) parameters

        Args:

            additionalFeatures (list): Additional feature columns (default: [Ljava.lang.String;@372a2a71)
            args (str): VW command line arguments passed (default: )
            featuresCol (str): features column name (default: features)
            hashSeed (int): Seed used for hashing (default: 0)
            ignoreNamespaces (str): Namespaces to be ignored (first letter only)
            initialModel (list): Initial model to start from
            interactions (list): Interaction terms as specified by -q
            l1 (double): l_1 lambda
            l2 (double): l_2 lambda
            labelCol (str): label column name (default: label)
            labelConversion (bool): Convert 0/1 Spark ML style labels to -1/1 VW style labels. Defaults to true. (default: true)
            learningRate (double): Learning rate
            numBits (int): Number of bits used (default: 18)
            numPasses (int): Number of passes over the data (default: 1)
            powerT (double): t power value
            predictionCol (str): prediction column name (default: prediction)
            probabilityCol (str): Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities (default: probability)
            rawPredictionCol (str): raw prediction (a.k.a. confidence) column name (default: rawPrediction)
            thresholds (list): Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
            weightCol (str): The name of the weight column
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    def setAdditionalFeatures(self, value):
        """

        Args:

            additionalFeatures (list): Additional feature columns (default: [Ljava.lang.String;@372a2a71)

        """
        self._set(additionalFeatures=value)
        return self


    def getAdditionalFeatures(self):
        """

        Returns:

            list: Additional feature columns (default: [Ljava.lang.String;@372a2a71)
        """
        return self.getOrDefault(self.additionalFeatures)


    def setArgs(self, value):
        """

        Args:

            args (str): VW command line arguments passed (default: )

        """
        self._set(args=value)
        return self


    def getArgs(self):
        """

        Returns:

            str: VW command line arguments passed (default: )
        """
        return self.getOrDefault(self.args)


    def setFeaturesCol(self, value):
        """

        Args:

            featuresCol (str): features column name (default: features)

        """
        self._set(featuresCol=value)
        return self


    def getFeaturesCol(self):
        """

        Returns:

            str: features column name (default: features)
        """
        return self.getOrDefault(self.featuresCol)


    def setHashSeed(self, value):
        """

        Args:

            hashSeed (int): Seed used for hashing (default: 0)

        """
        self._set(hashSeed=value)
        return self


    def getHashSeed(self):
        """

        Returns:

            int: Seed used for hashing (default: 0)
        """
        return self.getOrDefault(self.hashSeed)


    def setIgnoreNamespaces(self, value):
        """

        Args:

            ignoreNamespaces (str): Namespaces to be ignored (first letter only)

        """
        self._set(ignoreNamespaces=value)
        return self


    def getIgnoreNamespaces(self):
        """

        Returns:

            str: Namespaces to be ignored (first letter only)
        """
        return self.getOrDefault(self.ignoreNamespaces)


    def setInitialModel(self, value):
        """

        Args:

            initialModel (list): Initial model to start from

        """
        self._set(initialModel=value)
        return self


    def getInitialModel(self):
        """

        Returns:

            list: Initial model to start from
        """
        return self.getOrDefault(self.initialModel)


    def setInteractions(self, value):
        """

        Args:

            interactions (list): Interaction terms as specified by -q

        """
        self._set(interactions=value)
        return self


    def getInteractions(self):
        """

        Returns:

            list: Interaction terms as specified by -q
        """
        return self.getOrDefault(self.interactions)


    def setL1(self, value):
        """

        Args:

            l1 (double): l_1 lambda

        """
        self._set(l1=value)
        return self


    def getL1(self):
        """

        Returns:

            double: l_1 lambda
        """
        return self.getOrDefault(self.l1)


    def setL2(self, value):
        """

        Args:

            l2 (double): l_2 lambda

        """
        self._set(l2=value)
        return self


    def getL2(self):
        """

        Returns:

            double: l_2 lambda
        """
        return self.getOrDefault(self.l2)


    def setLabelCol(self, value):
        """

        Args:

            labelCol (str): label column name (default: label)

        """
        self._set(labelCol=value)
        return self


    def getLabelCol(self):
        """

        Returns:

            str: label column name (default: label)
        """
        return self.getOrDefault(self.labelCol)


    def setLabelConversion(self, value):
        """

        Args:

            labelConversion (bool): Convert 0/1 Spark ML style labels to -1/1 VW style labels. Defaults to true. (default: true)

        """
        self._set(labelConversion=value)
        return self


    def getLabelConversion(self):
        """

        Returns:

            bool: Convert 0/1 Spark ML style labels to -1/1 VW style labels. Defaults to true. (default: true)
        """
        return self.getOrDefault(self.labelConversion)


    def setLearningRate(self, value):
        """

        Args:

            learningRate (double): Learning rate

        """
        self._set(learningRate=value)
        return self


    def getLearningRate(self):
        """

        Returns:

            double: Learning rate
        """
        return self.getOrDefault(self.learningRate)


    def setNumBits(self, value):
        """

        Args:

            numBits (int): Number of bits used (default: 18)

        """
        self._set(numBits=value)
        return self


    def getNumBits(self):
        """

        Returns:

            int: Number of bits used (default: 18)
        """
        return self.getOrDefault(self.numBits)


    def setNumPasses(self, value):
        """

        Args:

            numPasses (int): Number of passes over the data (default: 1)

        """
        self._set(numPasses=value)
        return self


    def getNumPasses(self):
        """

        Returns:

            int: Number of passes over the data (default: 1)
        """
        return self.getOrDefault(self.numPasses)


    def setPowerT(self, value):
        """

        Args:

            powerT (double): t power value

        """
        self._set(powerT=value)
        return self


    def getPowerT(self):
        """

        Returns:

            double: t power value
        """
        return self.getOrDefault(self.powerT)


    def setPredictionCol(self, value):
        """

        Args:

            predictionCol (str): prediction column name (default: prediction)

        """
        self._set(predictionCol=value)
        return self


    def getPredictionCol(self):
        """

        Returns:

            str: prediction column name (default: prediction)
        """
        return self.getOrDefault(self.predictionCol)


    def setProbabilityCol(self, value):
        """

        Args:

            probabilityCol (str): Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities (default: probability)

        """
        self._set(probabilityCol=value)
        return self


    def getProbabilityCol(self):
        """

        Returns:

            str: Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities (default: probability)
        """
        return self.getOrDefault(self.probabilityCol)


    def setRawPredictionCol(self, value):
        """

        Args:

            rawPredictionCol (str): raw prediction (a.k.a. confidence) column name (default: rawPrediction)

        """
        self._set(rawPredictionCol=value)
        return self


    def getRawPredictionCol(self):
        """

        Returns:

            str: raw prediction (a.k.a. confidence) column name (default: rawPrediction)
        """
        return self.getOrDefault(self.rawPredictionCol)


    def setThresholds(self, value):
        """

        Args:

            thresholds (list): Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold

        """
        self._set(thresholds=value)
        return self


    def getThresholds(self):
        """

        Returns:

            list: Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
        """
        return self.getOrDefault(self.thresholds)


    def setWeightCol(self, value):
        """

        Args:

            weightCol (str): The name of the weight column

        """
        self._set(weightCol=value)
        return self


    def getWeightCol(self):
        """

        Returns:

            str: The name of the weight column
        """
        return self.getOrDefault(self.weightCol)





    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.ml.spark.vw.VowpalWabbitClassifier"

    @staticmethod
    def _from_java(java_stage):
        module_name=_VowpalWabbitClassifier.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".VowpalWabbitClassifier"
        return from_java(java_stage, module_name)

    def _create_model(self, java_model):
        return _VowpalWabbitClassificationModel(java_model)


class _VowpalWabbitClassificationModel(ComplexParamsMixin, JavaModel, JavaMLWritable, JavaMLReadable):
    """
    Model fitted by :class:`_VowpalWabbitClassifier`.

    This class is left empty on purpose.
    All necessary methods are exposed through inheritance.
    """

    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.ml.spark.vw.VowpalWabbitClassificationModel"

    @staticmethod
    def _from_java(java_stage):
        module_name=_VowpalWabbitClassificationModel.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".VowpalWabbitClassificationModel"
        return from_java(java_stage, module_name)

