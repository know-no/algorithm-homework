#include <iostream>
#include <string>
#include <map>
#include <set>
#include <limits>
#include <utility>
#include <vector>

using namespace std;

static auto f = [](){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    return true;
}();

int solve_rec(map<int,map<int,int>>& dp, vector<int>& books, int bIdx, int m){
    auto it = dp.find(bIdx);
    if (it != dp.end()){
        auto iit = it->second.find(m);
        if (iit != it->second.end()){
            return iit->second;
        }
    }
   
    if (m == books.size() - bIdx){
        int max_ = numeric_limits<int>::min();
        for (int i = bIdx; i < books.size(); ++i){
            max_ = max(max_, books[i]);
        }
        return dp[bIdx][m] = max_;
    }
   
    int min_ = numeric_limits<int>::max();
    int local_sum = 0;
    for (int i = 0; (books.size()-bIdx)-i > m-1; ++i){
        local_sum += books[bIdx+i];
        int m1 = solve_rec(dp, books, bIdx+1+i, m-1);
   
        min_ = min(min_, max(m1, local_sum));
    }
    return dp[bIdx][m] = min_;
}

int solve(vector<int>& books, int m){
    map<int,map<int,int>> dp;
    return solve_rec(dp, books, 0, m);
}

int main()
 {
	//code
	int t;
	cin >> t;
	for (int _ = 0; _ < t; ++_){
	    int n;
	    cin >> n;
	    vector<int> books;
	    for (int i = 0; i < n; ++i){
	       int v;
	       cin >> v;
	       books.push_back(v);
	    }
	    int m;
	    cin >> m;
	    cout << solve(books, m) << "\n";
	}
	return 0;
}
