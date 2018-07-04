# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC232()
    
@stepResult(descriptionMsg=u"영상카드 > 카테고리 영역과 아래로 콘텐츠 리스트 노출")
def TC232():
    HELP_TEXT = ("select_category_layout","story_telling_recyclerview","story_telling_img","story_telling_title")
    
    for searchingObj in HELP_TEXT: 
            
        rc, result = DEV1.UIWaitForName(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
    
    return AT_SUCCESS