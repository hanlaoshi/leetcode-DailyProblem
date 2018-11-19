--c++-------------这是运行速度最快的 ，大牛写的 ，看不懂 不会c [囧]
static const auto init = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return nullptr;
}();
class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m == 1 || n == 1)
			return 1;
		vector<vector<int>> p;
        for (int i = 0; i < m; i++)
		{
			vector<int> vec(n);
			p.push_back(vec);
		}
		p[0][0] = 0;
		p[1][0] = 1;
		p[0][1] = 1;
		//p[1][1] = 0;
		for (int i = 0; i < n; i++)
		{
			p[0][i] = 1;
		}
		for (int i = 0; i < m; i++)
		{
			p[i][0] = 1;
		}
		for (int i = 1; i < m; i++)
		{
			for (int j = 1; j < n; j++)
			{
				p[i][j] = p[i - 1][j] + p[i][j - 1];
			}
		}
		return p[m - 1][n - 1];
    }
};
