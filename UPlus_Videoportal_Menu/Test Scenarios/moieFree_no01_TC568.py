# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC558()
    
@stepResult(descriptionMsg=u"영화 > 무료 > 진입 > 배너 클릭 시 각 연결 카테고리로 이동되는지 확인한다.")       
def TC558():
    rc = DEV1.ClearAppData()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.LauchApp()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.ClearAppDataAgree()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.CheckMainDisplayLoaded()
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(1000) 
    #최신영화 진입
    rc = DEV1.ClickNewMovieMenu()
    if rc != AT_SUCCESS:
        return rc
    
    #영화 텍스트 찾기 
    rc = DEV1.CheckNewMovieMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc
    
    
    #최신작 탭 찾기
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
      
    #베너 선택 
    rc = DEV1.UIClickByTypeIndex('avwImageView', 9000)
    if rc != AT_SUCCESS:
        return rc
    
    
    System.Sleep(2000)
    
    DEV1.KeyPressByAlias('back')
    
    
    return AT_SUCCESS
    
    