# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC530()
    
@stepResult(descriptionMsg=u"게임 > 게임관련 채널 미리보기 영상 제공하며 플레이 영역 선택 시 Full Player로 전환 확인 ")       
def TC530(): 
    
        
    rc, result = DEV1.UIWaitForText(u"실시간 채널", 5000)
    if rc != AT_SUCCESS:
        return rc
         
    if result == False:
        return AT_NOT_FOUND
    
    rc = DEV1.UIClickByText(u"실시간 채널")
    if rc != AT_SUCCESS:
        return rc
    
    rc, result = DEV1.UIWaitForName("playerView", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    return AT_SUCCESS
    
    