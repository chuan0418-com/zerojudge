#include <iostream>
using namespace std;

int main(){
    int input_num[2], num[2], re, gcd, lcm, max_num, cur_num;
    cin >> input_num[0] >> input_num[1] >> input_num[2]; // 輸入2個數字
    num[0] = input_num[0]; num[1] = input_num[1];
    
    // 最大公因數 gcd
    for (int i=1;i<2;i++){
        do { // 算出 num1、num2 的 gcd
        	re = num[0]%num[i]; // 算出餘數
        	num[0] = num[i];
        	num[i] = re; 
        } while(re!=0); // 餘數是否為0
    }
    cout << num[0];
    return 0;
}