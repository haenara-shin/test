# utils 모듈의 'read_image' 함수와 'display' 함수를 임포트해 주세요
from cil.utils import read_image, display### 코드를 작성해 주세요 ###
# processing 모듈의 'invert' 함수를 'inv'로 임포트하고 'merge' 함수를 'mrg'로 임포트해 주세요
from cil.processing import invert as inv 
from cil.processing import merge as mrg
### 코드를 작성해 주세요 ###

logo = read_image('codeit_logo')
inverted_logo = inv(logo)
merged_img = mrg(logo, inverted_logo)

print('원본 이미지:')
display(logo)
print('\n색상 반전 이미지:')
display(inverted_logo)
print('\n합성 이미지:')
display(merged_img)

# 채점 코드
print()
dir_list = dir()
key_names = ['read_image', 'display', 'inv', 'mrg']
print(all(x in dir_list for x in key_names))
print('save_image' not in dir_list)