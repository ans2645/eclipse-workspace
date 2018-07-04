# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC581()
    
@stepResult(descriptionMsg=u"대박영상 > 오늘의 대박 > 공유 > 공유버튼 tap 시 하위 메뉴 팝업 제공 (메시지/ 카카오톡/ 카카오스토리/ 페이스북) 확인")       
def TC581():
    #공유하기 
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9005)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #공유하기 
    rc = DEV1.UIClickByName('item_share')
    if rc != AT_SUCCESS:
        return rc
    
    rc, result = DEV1.UIWaitForText(u"공유", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    rc, result = DEV1.UIWaitForText(u"메시지", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    rc, result = DEV1.UIWaitForText(u"카카오스토리", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    rc, result = DEV1.UIWaitForText(u"페이스북", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    rc, result = DEV1.UIWaitForText(u"취소", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    rc = DEV1.UIClickByText(u"취소")
    if rc != AT_SUCCESS:
        return rc
    
    return AT_SUCCESS