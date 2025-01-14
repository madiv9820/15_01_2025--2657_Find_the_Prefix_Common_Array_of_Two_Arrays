#include <iostream>
#include "Solution.hpp"

struct testcase { vector<int> A, B, output; };

class UnitTest {
private:
    vector<testcase> testcases;
    Solution obj;
public:
    UnitTest() {
        testcases = {{{1,3,2,4}, {3,1,2,4}, {0,2,3,4}}, 
                     {{2,3,1}, {3,1,2}, {0,1,3}}, 
                     {{1}, {1}, {1}}};
    }

    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            vector<int> result = obj.findThePrefixCommonArray(testcases[i].A, testcases[i].B);
            bool matched = true;
            for(int j = 0; j < result.size(); ++j)
                if(testcases[i].output[j] != result[j]) { matched = false; break; }
            
            cout << "Testcase " << i+1 << ": " << (matched ? "passed":"failed") << endl;
        }
    }
};

int main() {
    UnitTest test;
    test.test();
}