# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC235()
    
@stepResult(descriptionMsg=u"영상카드 > 카테고리 선택 시 선택된 카테고리에 따라 콘텐츠 노출")
def TC235():
    
    HELP_TEXT = (u"홈",u"영화",u"TV연예",u"라이프/스타일")
    for searchingObj in HELP_TEXT: 
        
        rc, result = DEV1.UIWaitForName('select_category_arrow', 500)
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForText")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND 
        
        System.Sleep(5000)
        
        rc = DEV1.UIClickByName("select_category_arrow")
        if rc != AT_SUCCESS:
            return rc
        
        rc = DEV1.UIClickByText(searchingObj)
        if rc != AT_SUCCESS:
            return rc
        
                   
        rc, result = DEV1.UIWaitForText(searchingObj, 500)
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForText")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND 
        
    rc = DEV1.UIClickByName("select_category_arrow")
    if rc != AT_SUCCESS:
        return rc
    
    rc, result = DEV1.UIWaitForText(u"홈", 500)
    if rc != AT_SUCCESS:
        return rc
         
    if result == False:
        return AT_NOT_FOUND 
        
    #다시홈으로 돌아옴
    rc = DEV1.UIClickByText(u"홈")
    if rc != AT_SUCCESS:
        return rc
        
    return AT_SUCCESS
        
