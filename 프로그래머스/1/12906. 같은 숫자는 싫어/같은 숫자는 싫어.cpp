#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    
    for (int i=0; i < size(arr); i++){
        if (answer.size() == 0 || arr[i] != arr[i-1])
        {
            answer.push_back(arr[i]);
        }
    }

    return answer;
}