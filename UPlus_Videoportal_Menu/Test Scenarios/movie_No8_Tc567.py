# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC567()
    
@stepResult(descriptionMsg=u"영화 > 무료 > 배너형식으로 표시되는지 확인한다.- 영화/해외 드라마 관련 월정액/무료 상품 노출")       
def TC567():
    #월정액별 무료 탭 찾기
    result = False
    for i in range(0,3):
        rc = DEV1.ScrollRight("avwObject", 9001)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
            
        searchingText = u"월정액별 무료"
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
    rc = DEV1.UIClickByText(u"월정액별 무료")
    if rc != AT_SUCCESS:
        return rc
    
    return AT_SUCCESS