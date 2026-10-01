#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define all(x) (x).begin(), (x).end()
const int M=1e9+7;
ll gcdll(ll a , ll b){
    if(b==0){
        return a;
    }
    return gcdll(b,a%b);
}
void fast(){
    ios::sync_with_stdio(0);
    cin.tie(0);
}


int main(){
    
    string s="hello";
    string s1="Hello";
    s1[0]='p';
    cout<<s1<<endl;


}


