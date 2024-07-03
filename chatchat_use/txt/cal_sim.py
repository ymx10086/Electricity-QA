#coding=gbk
import requests
import json

API_KEY = "" # ���API_KEY
SECRET_KEY = "" # ���SECRET_KEY

def cal_main(text1, text2):
        
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v2/simnet?charset=&access_token=" + get_access_token()
    
    payload = json.dumps({
        "text_1": text1,
        "text_2": text2
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

def get_access_token():
    """
    ʹ�� AK��SK ���ɼ�Ȩǩ����Access Token��
    :return: access_token������None(�������)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    text1 = "��ϲ����ƻ��"
    text2 = "��ϲ������"
    cal_main(text1, text2)