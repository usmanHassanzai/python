import numpy as np

#finding minimum num in array
arr = np.array([10,2,50,40,60,100])
min_no_arr = np.min(arr)
print(arr,f"\nmin_no_arr : {min_no_arr}")

#finding maximum num in array
max_no_arr = np.max(arr)
print(arr,f"\nmax_no_arr : {max_no_arr}")

#finding the position of minimum and maximum number in array
pos_min_no_arr = np.argmin(arr)
pos_max_no_arr = np.argmax(arr)
print(f"Maximum no position : {pos_max_no_arr}\nMinimum no Position : {pos_min_no_arr}")

#finding the sqrt of a number in array
sqrt_arr = np.sqrt(arr)
print(sqrt_arr)

#finding the trignometric function of sin and cos
sin = np.sin(90)
print(f"sin90 : {round(sin,0)}")
cos = np.cos(90)
print(f"cos90 : {round(cos,0)}")

#finding the cumulative sum of an array
cum_sum_arr = np.cumsum(arr)
print(cum_sum_arr)