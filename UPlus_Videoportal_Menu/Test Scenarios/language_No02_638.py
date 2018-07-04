# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC638()
    
@stepResult(descriptionMsg=u"원어자막 > 홈, 영어, 중국어, 일본어 (서버편성에 따라 달라질 수 있음)- 카테고리가 n개 이상시 좌우 flicking 가능")       
def TC638():      
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

    
    
    DEV1.KeyPressByAlias('back')
    
    #더보기 나타났는지
    rc = DEV1.CheckMenuCloseShown()
    if rc != AT_SUCCESS:
        return rc
      
    #더보기 클릭
    rc = DEV1.ClickMenuClose()
    if rc != AT_SUCCESS:
        return rc 
        
    return AT_SUCCESS
        
        
        
        