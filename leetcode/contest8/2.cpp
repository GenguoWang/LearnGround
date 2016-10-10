#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    bool canPartition(vector<int>& nums) {
      int n = nums.size();
      if (n<2) return false;
      int s = 0;
      for(int i=0;i<n;++i){
        s += nums[i];
      }
      if (s%2!=0) return false;
      int avg = s/2;
      bool f[5001][101];
      for(int j=0;j<avg+1;++j)
      for(int i=0;i<n+1;++i){
        f[j][i] = false;
      }
      for(int i=0;i<n+1;++i){
        f[0][i] = true;
      }
      for(int i=1;i<n+1;++i){
      for(int j=1;j<avg+1;++j){
        f[j][i] = f[j][i-1];
        if (j-nums[i-1]>=0) f[j][i] = f[j][i]|| f[j-nums[i-1]][i-1];
      }}
      return f[avg][n];
    }
};

int main(){
  Solution s;
  vector<int> v;
  v.push_back(1);
  v.push_back(5);
  v.push_back(11);
  v.push_back(5);
  cout << s.canPartition(v) << endl;
  return 0;
}
