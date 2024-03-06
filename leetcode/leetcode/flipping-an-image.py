class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_col = []
        new_img = []
        for row in range(len(image)):
            for col in range(len(image[0])-1,-1,-1):
                if image[row][col] == 0:
                    image[row][col] = 1
                else:
                    image[row][col] = 0
                new_col.append(image[row][col])
            new_img.append(new_col)
            new_col = []
        return new_img

        