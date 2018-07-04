# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC767()
    
@stepResult(descriptionMsg=u"아트&클래식 > 홈 버튼, 타이틀, 검색, GNB 버튼")       
def TC767():
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
    
    #GNB 쿨릭
    rc = DEV1.ClickMainMenuGNB()
    if rc != AT_SUCCESS:
        return rc
    
    #GNB 진입 확인
    rc = DEV1.CheckMainMenuGNBLoaded()
    if rc != AT_SUCCESS:
        return rc 
    
    
    #아트&클래식  찾기
    result = False
    for i in range(0,50):
        rc = DEV1.ScrollDown("avwSubWindow", 9085)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
            
        searchingText = u"아트&클래식"
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
    rc = DEV1.UIClickByText(u"아트&클래식")
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.ScrollDown("avwSubWindow", 9085)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
            
    #클릭 후 공연 무용 있는지 확인    
    rc, result = DEV1.UIWaitForText(u'공연 무용', 500)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #찾으면 클릭
    rc = DEV1.UIClickByText(u"공연 무용")
    if rc != AT_SUCCESS:
        return rc
    
    #상단 확인
    SPORTS_TV = ("btn_gotomain", "tv_title", "btn_search", "btn_menu")        
    
    #튜플 이용해 아트&클래식 상단에 홈버튼, 검색  , GNB 있는지 확인
    for searchingObj in SPORTS_TV: 
        rc, result = DEV1.UIWaitForName(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
    
    
    SPORTS_TV = (u"공연 무용", u"미술 전시", u"클래식 콘서트", u"오페라", u"팝 콘서트", u"예술 다큐")        
    
    #튜플 이용해 실시간TV 상단에 홈버튼, 검색  , GNB 있는지 확인
    for searchingObj in SPORTS_TV: 
        
        rc, result = DEV1.UIWaitForText(searchingObj, 500)
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
        
        rc = DEV1.UIClickByText(searchingObj)
        if rc != AT_SUCCESS:
            return rc
        
        #정렬버튼 찾기
        rc, result = DEV1.UIWaitForName("rlBottomButtonLayout", 3000)
        if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
            return rc
        
        if result == False:   # 오브젝트가 나타났는지 확인
            return AT_NOT_FOUND
        
        #정렬버튼 눌러보기
        rc = DEV1.UIClickByName('rlBottomButtonLayout')
        if rc != AT_SUCCESS:
            return rc
        
        System.Sleep(1000)
        """
        rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9018)
        if rc != AT_SUCCESS:
            return rc
        
        System.Sleep(3000)
        
        DEV1.KeyPressByAlias('back')
        
        System.Sleep(1000)"""
        
        #avwSubWindow 9018
    return AT_SUCCESS