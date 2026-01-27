#%% 
# Timely Journey
red = [0, 0, 4, 2, 1, 2, 2, 8, 3, 0, 9, 6, 3, 3, 0, 9, 3, 1, 5, 9, 0, 1, 3, 6] 
blue = [5, 0, 7, 2, 4, 6, 6, 0, 4, 2, 1, 0, 3, 6, 1, 7, 5, 4, 7, 2, 3, 1, 9, 9, 0] 
black = [3, 2, 4, 6, 3, 2, 4, 0, 0, 2, 0, 0, 4, 5, 2, 9, 3, 1, 0, 9, 7, 2, 5, 4, 3, 5, 0, 1, 2, 1, 1, 4, 2, 3, 0, 7, 4, 2, 9, 4, 3, 5, 7, 3, 5, 5, 1, 1, 1, 1, 1, 2, 0, 6, 0, 0, 5, 6, 1, 9, 6, 5, 3, 4, 3, 0, 5, 4, 5, 3, 1, 9, 2, 4, 2, 5, 5, 2, 3, 0, 2, 9, 2, 0, 5, 7, 8, 5, 0, 3, 1, 7, 6, 4, 2, 1, 4, 8] 
#%%
t_red = sum(red)
t_blue = sum(blue)
t_black = sum(black)
total = t_red + t_blue + t_black
print(f"Red: {t_red}, Blue: {t_blue}, Black: {t_black}, Total: {total}")
# %%
# frequency
from collections import Counter
freq_red = Counter(red)
freq_blue = Counter(blue)
freq_black = Counter(black)
print("Red frequencies:", freq_red)
print("Blue frequencies:", freq_blue)
print("Black frequencies:", freq_black)
# %%
