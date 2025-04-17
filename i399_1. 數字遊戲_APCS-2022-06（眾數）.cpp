#include "iostream"
using namespace std;

int main(void) {
    int input[3], current_num, current_num_count, max_num, max_num_count, input_count;
    /* 
        我一開始用 replit 寫，但編譯的時候有報錯：

        ./main.cpp:5:51: error: variable 'max_num' set but not used [-Werror,-Wunused-but-set-variable]
            5 |     int input[3], current_num, current_num_count, max_num, max_num_count, input_count;
              |                                                   ^
        1 error generated.
        make: *** [Makefile:10: main] Error 1

        我用同一份程式碼抓去 OnlineGDB、cpp.sh，都可以執行。

        我參考了 https://stackoverflow.com/a/50705574 ，使用 int max_num [[maybe_unused]]; 可以執行。
    */
    // 眾數
    max_num_count = 0; max_num = 0;
    cin >> input[0] >> input[1] >> input[2]; // 輸入數字，如："3 2 3"
    input_count = sizeof(input) / sizeof(input[0]); // 取得陣列長度（3）
    
    for (int i=0;i<input_count;i++){
        current_num = input[i];
        current_num_count = 0;
        for (int j=0;j<input_count;j++){
            if (input[j] == current_num){
                ++current_num_count;
            }
        }
        if (current_num_count >= max_num_count){
            max_num = current_num;
            max_num_count = current_num_count;
        }
    }

    // 排序
    for (int a=0;a<input_count-1;a++){
        for(int b=0;b<input_count-1-a;b++){
            if (input[b] < input[b+1]){
                swap(input[b], input[b+1]);
            }else if (input[b] == input[b+1]){
                input[b+1] = 0; // 標記為重複值
            }
        }
    }

    // 輸出
    if (input[1] == 0 && input[2] == 0){
        cout << max_num_count << " " << input[0];
    }else if (input[1] != 0 && input[2] == 0){
        cout << max_num_count << " " << input[0] << " " << input[1];
    }else if (input[1] == 0 && input[2] != 0){
        cout << max_num_count << " " << input[0] << " " << input[2];
    }else{
        cout << max_num_count << " " << input[0] << " " << input[1] << " " << input[2];
    }
    
    return 0;
} 