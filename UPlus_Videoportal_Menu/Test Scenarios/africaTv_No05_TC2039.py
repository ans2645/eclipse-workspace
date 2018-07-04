# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC2039()
    
@stepResult(descriptionMsg=u"아프리카TV > 핫이슈/Top30 > 리스트 정보 > 썸네일/제목/조회수/재생시간 노출되는지 확인")       
def TC2039():
    """
    핫이슈 메뉴는 2단리스트 / TOP 메뉴는 1단 리스트로 노출
    """
    
    '''
   Top 30 
    '''
    
    #핫이슈 찾기
    rc, result = DEV1.UIGetObjectByTypeIndex('avwObject', 9012)
    if rc != AT_SUCCESS:
        return rc
    
    #핫이슈 클릭
    rc = DEV1.UIClickByTypeIndex("avwObject", 9012)
    if rc != AT_SUCCESS:
        return rc
    
    #썸네일 찾기
    #rc, result = DEV1.UIGetObjectByTypeIndex('avwObject', 9035)
    #if rc != AT_SUCCESS:
     #   return rc
    
    
    #제목 찾기
    #rc, result = DEV1.UIGetObjectByTypeIndex('avwObject', 9042)
    #if rc != AT_SUCCESS:
     #   return rc
    
    #조회수 찾기
    #rc, result = DEV1.UIGetObjectByTypeIndex('avwObject', 9046)
    #if rc != AT_SUCCESS:
     #   return rc
    
    #재생시간 찾기
    #rc, result = DEV1.UIGetObjectByTypeIndex('avwObject', 9040)
    #if rc != AT_SUCCESS:
     #   return rc
    
    
    '''
   Top 30 
    '''
   #Top 30  찾기 02 6928 8017 02 6964 8866
   
    rc, result = DEV1.UIGetObjectByTypeIndex('avwObject', 9016)
    if rc != AT_SUCCESS:
        return rc
    
    #Top 30  클릭
    rc = DEV1.UIClickByTypeIndex("avwObject", 9016)
    if rc != AT_SUCCESS:
        return rc
    

    
    return AT_SUCCESS
    
    
    