# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC559()
    
@stepResult(descriptionMsg=u"영화 > 19금 > 성인 로그인 + 성인 잠금 OFF 상태- 리스트 선택 시 진입 가능")       
def TC559():
    
    result = False
    for i in range(0,3):
        rc = DEV1.ScrollLeft("avwObject", 9001)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
            
        searchingText = u"19금"
        rc, result = DEV1.UIWaitForText(searchingText, 2000, 0, UITarget.TopWindow)
        if rc != AT_SUCCESS:
            System.Debug(u"Failed to UIWaitForText")
            return rc
        
        if result == True:
            break
        
    if result == False:
        System.Debug(u"Failed to find the text : "+searchingText)
        return AT_NOT_FOUND
    
    
    rc = DEV1.UIClickByText(u"19금")
    if rc != AT_SUCCESS:
        return rc
    
    """
    #상단에 19금 텍스트 있는지 확인
    rc, result = DEV1.UIWaitForText(u"19금", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #부끄 19금 진입
    rc = DEV1.UIClickByText(u"19금")
    if rc != AT_SUCCESS:
        return rc
    """
    
    HELP_TEXT = (u"NEW / HOT",u"한국관",u"일본관",u"해외관",u"추천 콜렉션")
    
    for searchingObj in HELP_TEXT: 
        rc, result = DEV1.UIWaitForText(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
        
    return AT_SUCCESS
    
    
    
    
    
    
   
        
    