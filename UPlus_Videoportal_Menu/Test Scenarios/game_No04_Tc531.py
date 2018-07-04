# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC531()
    
@stepResult(descriptionMsg=u"게임 > 편성표, 멀티뷰, 새로고침 버튼 제공하는지 확인 ")       
def TC531(): 
#- 편성표 : 케이블 편성표로 이동

#편성표 name 있는지 확인
    rc, result = DEV1.UIWaitForName("imgProgramTable", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #편성표 클릭 (편성표 name : imgProgramTable)
    rc = DEV1.UIClickByName('imgProgramTable')
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(2000)
    
    #편성표 진입 후 타이틀 '실시간 TV 편성표' 텍스트 있는지 확인
    rc, result = DEV1.UIWaitForText(u"실시간 TV 편성표", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #'뒤로가기' 버튼
    rc, result = DEV1.UIWaitForName("imgBack", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    #'뒤로가기' 버튼 클릭
    rc = DEV1.UIClickByName('imgBack')
    if rc != AT_SUCCESS:
        return rc
    
# 멀티뷰 : 4:4 플레이 영역 확장"

    #멀티뷰 name : imgMultiView
    rc, result = DEV1.UIWaitForName("imgMultiView", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    System.Sleep(5000)
    
    #멀티뷰 클릭 
    rc = DEV1.UIClickByName('imgMultiView')
    if rc != AT_SUCCESS:
        return rc
    
    #4개 동영상 확인
    rc, result = DEV1.UIWaitForName("content", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    System.Sleep(5000)
    
    
    DEV1.KeyPressByAlias('back')
    
    
    rc, result = DEV1.UIWaitForName("imgRefresh", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    #새로고침 클릭 
    rc = DEV1.UIClickByName('imgRefresh')
    if rc != AT_SUCCESS:
        return rc
    
    return AT_SUCCESS
    
    