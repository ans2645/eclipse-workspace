# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC565()
    
@stepResult(descriptionMsg=u"영화 > 특집/할인 > 배너형식으로 표시되는지 확인")       
def TC565():
    #특집/할인 탭 찾기
    result = False
    for i in range(0,3):
        rc = DEV1.ScrollRight("avwObject", 9001)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
            
        searchingText = u"특집"
        rc, result = DEV1.UIWaitForText(searchingText, 2000, 0, UITarget.TopWindow)
        if rc != AT_SUCCESS:
            System.Debug(u"Failed to UIWaitForText")
            return rc
        
        if result == True:
            break
        
    if result == False:
        System.Debug(u"Failed to find the text : "+searchingText)
        return AT_NOT_FOUND
    
    #찾으면 클릭
    rc = DEV1.UIClickByText(u"특집")
    if rc != AT_SUCCESS:
        return rc
    
    #베너형식인지 알아보기
    rc, result = DEV1.UIWaitForName("banner", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    return AT_SUCCESS
    
    