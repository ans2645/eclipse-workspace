# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC525()
    
@stepResult(descriptionMsg=u"스포츠 > 골프  > 세로메뉴로 하위 카테고리를 제공하는지 확인(서버편성에 따라 다름)- 구성 : KLPGA, GTOUR, WGTOUR, 레슨")
def TC525():
    
    #우측 Flicking 
    rc = DEV1.ScrollRight("avwObject", 9001)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    
    #우측 Flicking 
    rc = DEV1.ScrollRight("avwObject", 9001)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    
    #골프 찾기
    rc, result = DEV1.UIWaitForText(u"골프", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    System.Sleep(1000)
    #골프 클릭 후 진입
    rc = DEV1.UIClickByText(u"골프")
    if rc != AT_SUCCESS:
        return rc
    
    #KLPGA 찾기
    rc, result = DEV1.UIWaitForText(u"KLPGA", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #GTOUR 찾기
    rc, result = DEV1.UIWaitForText(u"GTOUR", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #GTOUR 찾기
    rc, result = DEV1.UIWaitForText(u"WGTOUR", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #GTOUR 찾기
    rc, result = DEV1.UIWaitForText(u"레슨", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    return AT_SUCCESS
    
    
    
    