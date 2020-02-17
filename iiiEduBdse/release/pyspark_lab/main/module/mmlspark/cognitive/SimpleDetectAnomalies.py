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
from mmlspark.core.schema.TypeConversionUtils import generateTypeConverter, complexTypeConverter

@inherit_doc
class SimpleDetectAnomalies(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """


    Args:

        concurrency (int): max number of concurrent calls (default: 1)
        concurrentTimeout (double): max number seconds to wait on futures if concurrency >= 1 (default: 100.0)
        customInterval (object): Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.
        errorCol (str): column to hold http errors (default: [self.uid]_error)
        granularity (object): Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.
        groupbyCol (str): column that groups the series
        handler (object): Which strategy to use when handling requests (default: UserDefinedFunction(<function2>,StringType,None))
        maxAnomalyRatio (object): Optional argument, advanced model parameter, max anomaly ratio in a time series.
        outputCol (str): The name of the output column (default: [self.uid]_output)
        period (object): Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.
        sensitivity (object): Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted
        series (object): Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.
        subscriptionKey (object): the API key to use
        timeout (double): number of seconds to wait before closing the connection (default: 60.0)
        timestampCol (str): column representing the time of the series (default: timestamp)
        url (str): Url of the service
        valueCol (str): column representing the value of the series (default: value)
    """

    @keyword_only
    def __init__(self, concurrency=1, concurrentTimeout=100.0, customInterval=None, errorCol=None, granularity=None, groupbyCol=None, handler=None, maxAnomalyRatio=None, outputCol=None, period=None, sensitivity=None, series=None, subscriptionKey=None, timeout=60.0, timestampCol="timestamp", url=None, valueCol="value"):
        super(SimpleDetectAnomalies, self).__init__()
        self._java_obj = self._new_java_obj("com.microsoft.ml.spark.cognitive.SimpleDetectAnomalies")
        self._cache = {}
        self.concurrency = Param(self, "concurrency", "concurrency: max number of concurrent calls (default: 1)")
        self._setDefault(concurrency=1)
        self.concurrentTimeout = Param(self, "concurrentTimeout", "concurrentTimeout: max number seconds to wait on futures if concurrency >= 1 (default: 100.0)")
        self._setDefault(concurrentTimeout=100.0)
        self.customInterval = Param(self, "customInterval", "customInterval:  Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.")
        self.errorCol = Param(self, "errorCol", "errorCol: column to hold http errors (default: [self.uid]_error)")
        self._setDefault(errorCol=self.uid + "_error")
        self.granularity = Param(self, "granularity", "granularity:  Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.")
        self.groupbyCol = Param(self, "groupbyCol", "groupbyCol: column that groups the series")
        self.handler = Param(self, "handler", "handler: Which strategy to use when handling requests (default: UserDefinedFunction(<function2>,StringType,None))", generateTypeConverter("handler", self._cache, complexTypeConverter))
        self.maxAnomalyRatio = Param(self, "maxAnomalyRatio", "maxAnomalyRatio:  Optional argument, advanced model parameter, max anomaly ratio in a time series.")
        self.outputCol = Param(self, "outputCol", "outputCol: The name of the output column (default: [self.uid]_output)")
        self._setDefault(outputCol=self.uid + "_output")
        self.period = Param(self, "period", "period:  Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.")
        self.sensitivity = Param(self, "sensitivity", "sensitivity:  Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted")
        self.series = Param(self, "series", "series:  Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.")
        self.subscriptionKey = Param(self, "subscriptionKey", "subscriptionKey: the API key to use")
        self.timeout = Param(self, "timeout", "timeout: number of seconds to wait before closing the connection (default: 60.0)")
        self._setDefault(timeout=60.0)
        self.timestampCol = Param(self, "timestampCol", "timestampCol: column representing the time of the series (default: timestamp)")
        self._setDefault(timestampCol="timestamp")
        self.url = Param(self, "url", "url: Url of the service")
        self.valueCol = Param(self, "valueCol", "valueCol: column representing the value of the series (default: value)")
        self._setDefault(valueCol="value")
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, concurrency=1, concurrentTimeout=100.0, customInterval=None, errorCol=None, granularity=None, groupbyCol=None, handler=None, maxAnomalyRatio=None, outputCol=None, period=None, sensitivity=None, series=None, subscriptionKey=None, timeout=60.0, timestampCol="timestamp", url=None, valueCol="value"):
        """
        Set the (keyword only) parameters

        Args:

            concurrency (int): max number of concurrent calls (default: 1)
            concurrentTimeout (double): max number seconds to wait on futures if concurrency >= 1 (default: 100.0)
            customInterval (object): Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.
            errorCol (str): column to hold http errors (default: [self.uid]_error)
            granularity (object): Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.
            groupbyCol (str): column that groups the series
            handler (object): Which strategy to use when handling requests (default: UserDefinedFunction(<function2>,StringType,None))
            maxAnomalyRatio (object): Optional argument, advanced model parameter, max anomaly ratio in a time series.
            outputCol (str): The name of the output column (default: [self.uid]_output)
            period (object): Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.
            sensitivity (object): Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted
            series (object): Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.
            subscriptionKey (object): the API key to use
            timeout (double): number of seconds to wait before closing the connection (default: 60.0)
            timestampCol (str): column representing the time of the series (default: timestamp)
            url (str): Url of the service
            valueCol (str): column representing the value of the series (default: value)
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    def setConcurrency(self, value):
        """

        Args:

            concurrency (int): max number of concurrent calls (default: 1)

        """
        self._set(concurrency=value)
        return self


    def getConcurrency(self):
        """

        Returns:

            int: max number of concurrent calls (default: 1)
        """
        return self.getOrDefault(self.concurrency)


    def setConcurrentTimeout(self, value):
        """

        Args:

            concurrentTimeout (double): max number seconds to wait on futures if concurrency >= 1 (default: 100.0)

        """
        self._set(concurrentTimeout=value)
        return self


    def getConcurrentTimeout(self):
        """

        Returns:

            double: max number seconds to wait on futures if concurrency >= 1 (default: 100.0)
        """
        return self.getOrDefault(self.concurrentTimeout)


    def setCustomInterval(self, value):
        """

        Args:

            customInterval (object): Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.

        """
        self._java_obj = self._java_obj.setCustomInterval(value)
        return self


    def setCustomIntervalCol(self, value):
        """

        Args:

            customInterval (object): Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.

        """
        self._java_obj = self._java_obj.setCustomIntervalCol(value)
        return self




    def getCustomInterval(self):
        """

        Returns:

            object: Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.
        """
        return self._cache.get("customInterval", None)


    def setErrorCol(self, value):
        """

        Args:

            errorCol (str): column to hold http errors (default: [self.uid]_error)

        """
        self._set(errorCol=value)
        return self


    def getErrorCol(self):
        """

        Returns:

            str: column to hold http errors (default: [self.uid]_error)
        """
        return self.getOrDefault(self.errorCol)


    def setGranularity(self, value):
        """

        Args:

            granularity (object): Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.

        """
        self._java_obj = self._java_obj.setGranularity(value)
        return self


    def setGranularityCol(self, value):
        """

        Args:

            granularity (object): Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.

        """
        self._java_obj = self._java_obj.setGranularityCol(value)
        return self




    def getGranularity(self):
        """

        Returns:

            object: Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.
        """
        return self._cache.get("granularity", None)


    def setGroupbyCol(self, value):
        """

        Args:

            groupbyCol (str): column that groups the series

        """
        self._set(groupbyCol=value)
        return self


    def getGroupbyCol(self):
        """

        Returns:

            str: column that groups the series
        """
        return self.getOrDefault(self.groupbyCol)


    def setHandler(self, value):
        """

        Args:

            handler (object): Which strategy to use when handling requests (default: UserDefinedFunction(<function2>,StringType,None))

        """
        self._set(handler=value)
        return self


    def getHandler(self):
        """

        Returns:

            object: Which strategy to use when handling requests (default: UserDefinedFunction(<function2>,StringType,None))
        """
        return self._cache.get("handler", None)


    def setMaxAnomalyRatio(self, value):
        """

        Args:

            maxAnomalyRatio (object): Optional argument, advanced model parameter, max anomaly ratio in a time series.

        """
        self._java_obj = self._java_obj.setMaxAnomalyRatio(value)
        return self


    def setMaxAnomalyRatioCol(self, value):
        """

        Args:

            maxAnomalyRatio (object): Optional argument, advanced model parameter, max anomaly ratio in a time series.

        """
        self._java_obj = self._java_obj.setMaxAnomalyRatioCol(value)
        return self




    def getMaxAnomalyRatio(self):
        """

        Returns:

            object: Optional argument, advanced model parameter, max anomaly ratio in a time series.
        """
        return self._cache.get("maxAnomalyRatio", None)


    def setOutputCol(self, value):
        """

        Args:

            outputCol (str): The name of the output column (default: [self.uid]_output)

        """
        self._set(outputCol=value)
        return self


    def getOutputCol(self):
        """

        Returns:

            str: The name of the output column (default: [self.uid]_output)
        """
        return self.getOrDefault(self.outputCol)


    def setPeriod(self, value):
        """

        Args:

            period (object): Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.

        """
        self._java_obj = self._java_obj.setPeriod(value)
        return self


    def setPeriodCol(self, value):
        """

        Args:

            period (object): Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.

        """
        self._java_obj = self._java_obj.setPeriodCol(value)
        return self




    def getPeriod(self):
        """

        Returns:

            object: Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.
        """
        return self._cache.get("period", None)


    def setSensitivity(self, value):
        """

        Args:

            sensitivity (object): Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted

        """
        self._java_obj = self._java_obj.setSensitivity(value)
        return self


    def setSensitivityCol(self, value):
        """

        Args:

            sensitivity (object): Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted

        """
        self._java_obj = self._java_obj.setSensitivityCol(value)
        return self




    def getSensitivity(self):
        """

        Returns:

            object: Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted
        """
        return self._cache.get("sensitivity", None)


    def setSeries(self, value):
        """

        Args:

            series (object): Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.

        """
        self._java_obj = self._java_obj.setSeries(value)
        return self


    def setSeriesCol(self, value):
        """

        Args:

            series (object): Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.

        """
        self._java_obj = self._java_obj.setSeriesCol(value)
        return self




    def getSeries(self):
        """

        Returns:

            object: Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.
        """
        return self._cache.get("series", None)


    def setSubscriptionKey(self, value):
        """

        Args:

            subscriptionKey (object): the API key to use

        """
        self._java_obj = self._java_obj.setSubscriptionKey(value)
        return self


    def setSubscriptionKeyCol(self, value):
        """

        Args:

            subscriptionKey (object): the API key to use

        """
        self._java_obj = self._java_obj.setSubscriptionKeyCol(value)
        return self




    def getSubscriptionKey(self):
        """

        Returns:

            object: the API key to use
        """
        return self._cache.get("subscriptionKey", None)


    def setTimeout(self, value):
        """

        Args:

            timeout (double): number of seconds to wait before closing the connection (default: 60.0)

        """
        self._set(timeout=value)
        return self


    def getTimeout(self):
        """

        Returns:

            double: number of seconds to wait before closing the connection (default: 60.0)
        """
        return self.getOrDefault(self.timeout)


    def setTimestampCol(self, value):
        """

        Args:

            timestampCol (str): column representing the time of the series (default: timestamp)

        """
        self._set(timestampCol=value)
        return self


    def getTimestampCol(self):
        """

        Returns:

            str: column representing the time of the series (default: timestamp)
        """
        return self.getOrDefault(self.timestampCol)


    def setUrl(self, value):
        """

        Args:

            url (str): Url of the service

        """
        self._set(url=value)
        return self


    def getUrl(self):
        """

        Returns:

            str: Url of the service
        """
        return self.getOrDefault(self.url)


    def setValueCol(self, value):
        """

        Args:

            valueCol (str): column representing the value of the series (default: value)

        """
        self._set(valueCol=value)
        return self


    def getValueCol(self):
        """

        Returns:

            str: column representing the value of the series (default: value)
        """
        return self.getOrDefault(self.valueCol)




    def setLocation(self, value):
        self._java_obj = self._java_obj.setLocation(value)
        return self


    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.ml.spark.cognitive.SimpleDetectAnomalies"

    @staticmethod
    def _from_java(java_stage):
        module_name=SimpleDetectAnomalies.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".SimpleDetectAnomalies"
        return from_java(java_stage, module_name)
