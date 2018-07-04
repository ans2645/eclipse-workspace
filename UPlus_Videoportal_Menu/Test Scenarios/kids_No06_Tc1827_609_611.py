# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC1827_609_611()
    
@stepResult(descriptionMsg=u"키즈 > 키즈 월정액 > 세로메뉴로 하위카테고리 제공하는지 확인, 리스트 영역에 포스터, 제목 제공하는지 확인")       
def TC1827_609_611():
    
    rc = DEV1.LauchApp()
    if rc != AT_SUCCESS:
        return rc

    rc = DEV1.CheckMainDisplayLoaded()
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(1000)
    
    #더보기 나타났는지
    rc = DEV1.CheckMoreMenuShown()
    if rc != AT_SUCCESS:
        return rc
    
    #더보기 클릭
    rc = DEV1.ClickMoreMenu()
    if rc != AT_SUCCESS:
        return rc 
    
    rc = DEV1.CheckKidsWorldMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc 
    
    rc = DEV1.ClickKidsWorldMenu()
    if rc != AT_SUCCESS:
        return rc
    
    #아이들세상 메뉴 진입 확인
    rc = DEV1.CheckKidsWorldMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc   

        
    return AT_SUCCESS

#- 카테고리 상하 flicking 스크롤 제공
#- 하위 카테고리 선택 시 선택한 카테고리 표시"


#- 포스터 선택 시 상세페이지로 이동
#- 리스트 영역 상하 flicking 스크롤 제공"

