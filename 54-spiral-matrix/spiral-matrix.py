class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        resposta = []
        while matrix:
            resposta += matrix.pop(0)
            
            if matrix and matrix[0]:
                for row in matrix:
                    resposta.append(row.pop())
            if matrix:
                resposta += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    resposta.append(row.pop(0))
        return resposta