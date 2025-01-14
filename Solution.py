from typing import List

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