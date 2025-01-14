#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        // Initialize a vector C to store the result and two frequency arrays to keep track of element counts
        vector<int> C(A.size());  
        vector<int> freq_Element_A(51), freq_Element_B(51);  // Using a fixed size of 50 assuming element values range from 1 to 50

        // Loop through each index of arrays A and B
        for(int i = 0; i < A.size(); ++i) {
            // Increment the frequency of elements in arrays A and B
            ++freq_Element_A[A[i]]; 
            ++freq_Element_B[B[i]];

            // Set C[i] to the previous value of C[i-1] if i > 0, otherwise initialize to 0
            C[i] = (i > 0) ? C[i-1] : 0;

            // If A[i] is present in B, increment the common prefix count at position i
            if(freq_Element_B[A[i]]) 
                ++C[i];

            // If B[i] is present in A, increment the common prefix count at position i
            if(freq_Element_A[B[i]]) 
                ++C[i];

            // If A[i] and B[i] are the same, decrement the common prefix count for this position
            // because both arrays contribute the same element, so we shouldn't double-count
            if(A[i] == B[i]) 
                --C[i];
        }

        // Return the result array C
        return C;
    }
};