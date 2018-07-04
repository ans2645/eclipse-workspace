# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC944()
    
@stepResult(descriptionMsg=u"360도 영상 > 플레이어를 빠져나가 이전화면 표시한다.")       
def TC944():
    
    rc, result = DEV1.UIWaitForText(u"360도영상", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    rc, result = DEV1.UIWaitForName("btn_gotomain", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #재생하기 있는지 확인
    rc = DEV1.UIClickByName('btn_gotomain')
    if rc != AT_SUCCESS:
        return rc
    
    #더보기 나타났는지
    rc = DEV1.CheckMenuCloseShown()
    if rc != AT_SUCCESS:
        return rc
      
    #더보기 클릭
    rc = DEV1.ClickMenuClose()
    if rc != AT_SUCCESS:
        return rc 
                
    return AT_SUCCESS