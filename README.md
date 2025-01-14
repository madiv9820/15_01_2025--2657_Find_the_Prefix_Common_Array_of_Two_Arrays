# 2657. Find the Prefix Common Array of Two Arrays

- ### Intuition
    The problem asks for the number of common elements between prefixes of two arrays, `A` and `B`, at each index `i`. The solution relies on tracking the frequency of elements that have appeared in the arrays `A` and `B` up to each index. By using frequency counts, we can efficiently determine how many common elements are present in the prefixes of the arrays at each step without the need for nested loops or excessive comparisons.

- ### Approach
    1. **Frequency Arrays**: We use two frequency arrays, `freq_Element_A` and `freq_Element_B`, to keep track of how many times each element has appeared in the prefixes of arrays `A` and `B`, respectively. These arrays are initialized to a fixed size (e.g., 50, assuming the values in the arrays range from 1 to 50).

    2. **Result Array**: We maintain an array `C`, where `C[i]` will store the count of common elements between the prefixes of `A` and `B` up to index `i`.

    3. **Iterate Through Arrays**:
        - For each index `i`, we update the frequencies of `A[i]` and `B[i]` in their respective frequency arrays.
        - We set `C[i]` to the number of common elements up to that index, using the previously calculated result `C[i-1]` (if `i > 0`).
        - If `A[i]` is found in `B` and `B[i]` is found in `A`, we update `C[i]` to reflect the commonality. If `A[i] == B[i]`, we decrement the count to avoid double-counting the same element.

    4. **Return Result**: After processing all elements, the array `C` will contain the number of common elements for each prefix of `A` and `B`.

- ### Code Implementation
    - **Python Solution**
        ```python3 []
        class Solution:
            def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
                # Get the length of the arrays
                n = len(A)
                
                # Initialize the result list C to store the number of common elements up to each index
                C = [0] * n
                
                # Frequency arrays to track the occurrence of elements in arrays A and B
                freq_Element_A = [0] * 51  # Assuming values in A are from 1 to 50
                freq_Element_B = [0] * 51  # Assuming values in B are from 1 to 50

                # Loop through each index in the arrays A and B
                for i in range(n):
                    # Increment the frequency of the current element in arrays A and B
                    freq_Element_A[A[i]] += 1
                    freq_Element_B[B[i]] += 1
                    
                    # Set C[i] to the value of the previous position C[i-1] if i > 0, otherwise initialize to 0
                    C[i] = C[i-1] if i > 0 else 0

                    # If element A[i] exists in B (i.e., it's present in the prefix of B), increment C[i]
                    if freq_Element_B[A[i]]:
                        C[i] += 1

                    # If element B[i] exists in A (i.e., it's present in the prefix of A), increment C[i]
                    if freq_Element_A[B[i]]:
                        C[i] += 1

                    # If A[i] and B[i] are the same element, decrement C[i] to avoid double-counting
                    if A[i] == B[i]:
                        C[i] -= 1

                # Return the result array C, which contains the number of common elements for each prefix
                return C
        ```
    - **C++ Solution**
        ```cpp []
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
        ```

- ### Time Complexity
    - **Initialization**: The initialization of arrays `C`, `freq_Element_A`, and `freq_Element_B` takes constant time, $O(n)$, where $n$ is the length of the input arrays.
    
    - **Main Loop**: We iterate through both arrays once, and each iteration involves constant-time operations (updating frequencies and checking conditions). Therefore, the time complexity of the loop is $O(n)$.
    
        Overall, the time complexity is **$O(n)$**, where $n$ is the size of the input arrays `A` and `B`.

- ### Space Complexity
    - **Frequency Arrays**: We use two frequency arrays of size 50, which occupy constant space. This is $O(1)$ in terms of space complexity since the array size is fixed.

    Overall, the space complexity is **$O(1)$**. 