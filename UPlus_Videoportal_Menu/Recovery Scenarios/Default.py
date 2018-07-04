# -*- coding: utf-8 -*- 

from ATS.Core.Enums import ReturnCode
from ATS.Core.Enums import ExecutionResult
from ATS.System import ManageJob

def Recovery(dev, method_name, args, kwargs, return_code):
    if return_code == ReturnCode.AT_PORT_ERROR:
        if dev.config.TerminateOnPortError:
            System.Finish(ExecutionResult.T_FAILED, u"AT_PORT_ERROR occurred on " + dev.ObjectName, ManageJob.JOB_STOP)
        else:
            System.Finish(ExecutionResult.T_FAILED, u"AT_PORT_ERROR occurred on " + dev.ObjectName)
    return ReturnCode.AT_SUCCESS
