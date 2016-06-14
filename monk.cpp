#include <iostream>
using namespace std;

int main() {
int t;
scanf(“%d”,&t);
while(t>0){
int n;
scanf(“%d”,&n);
long long int a[n];
for(int i=0;i<n;i++){
scanf(“%lld”,&a[i]);}
int b[10];
for(int i=0;i<10;i++) b[i]=0;
for(int i=0;i<n;i++) b[a[i]%10]++;
long long int c=0;
for(int i=0;i<10;i++){
if(b[i]>1) c=c+(b[i]-1);}
printf(“%lld\n”,c);
t=t-1;
}
return 0;
}
