#include <string>
#include <vector>

using namespace std;

int result=987654321;

void Go(string name,string str,int idx,int cnt,int count){
    if(cnt>=result){return;}
    if(name==str){result=min(result,cnt);return;}
    if(count>name.size()){return;}

    if(idx==name.size()){idx=0;}
    if(idx==-1){idx=name.size()-1;}
    
    if(str[idx]!=name[idx]){
        int left=name[idx]-'A';
        int right='Z'-name[idx]+1;
        str[idx]=name[idx];
        cnt+=min(left,right);
    }
    string tmp=str;
    Go(name,str,idx+1,cnt+1,count+1);
    Go(name,tmp,idx-1,cnt+1,count+1);
}

int solution(string name) {
    string str;
    for(int i=0;i<name.size();i++){str.push_back('A');}
    Go(name,str,0,0,0);
    return result==0?0:result-1;
}
