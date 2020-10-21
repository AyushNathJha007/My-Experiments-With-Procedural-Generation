import os
import sys
        
#text_level_folder = "../levels_prediction_textfiles/"
#new_img_level_folder = "../Generated_levels/"

#predicted_level = sys.argv[1]

r = open("GenLev1Copy.txt", "r")
f = open("GenLev1Copy_upRight.txt", "w")
text = ""
#w, h = 2048, 13;
w, h = 257, 13;
itr = 0
copy = 0
trans = [[0 for x in range(h)] for y in range(w)]
for i in range(0, 257):
        text= r.readline()
        for c in text:
        	if(copy == 13): break
        	trans[i][copy] = c
        	copy += 1
        text = ""
        copy = 0

r.close()
print(trans)

for i in range(0,13):
        for j in range(0,257):
        	text += trans[j][i]
        f.write(text)
        f.write("\n")
        text = ""
f.close()