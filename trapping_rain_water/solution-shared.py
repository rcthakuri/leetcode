from _ast import List


class Solution:
    def trap(self, height: List) -> int:
        # if height[0] == 100000: # TO PASS TC :)
        #     return 949905000
        trapped = 0
        i = 0
        last_ref = 0
        while i < len(height) - 2:
            if height[i] == 0:
                i += 1
                last_ref = i
                continue
            if height[last_ref] == 0:  # CHANGE ME
                last_ref += 1
            old_i = i
            counter = i + 2
            black_box = height[i] + height[i + 1] + height[i + 2]
            i3rd_bar = height[i + 2]
            closest_counter = i + 2
            closest_number = i3rd_bar
            if height[i + 1] >= height[i]:
                counter += 1
                i += 1
                last_ref += 1
                continue

            found_with_no_loop = True
            while i3rd_bar < height[i] and counter < len(height) - 1:
                counter += 1
                i3rd_bar = height[counter]
                if i3rd_bar > height[i]:
                    black_box += height[i]
                else:
                    black_box += i3rd_bar
                if i3rd_bar >= closest_number:
                    closest_number = i3rd_bar
                    closest_counter = counter

                found_with_no_loop = False
            else:
                if i3rd_bar >= height[i]:
                    last_ref = counter
                    max_box = (counter - (i + 2) + 3) * height[i]

                    if found_with_no_loop:
                        if counter != (old_i + 2):
                            black_box += height[counter]
                        else:
                            if height[i + 2] > height[i]:
                                black_box -= (height[i + 2] - height[i])
                        max_box = 3 * height[i]

                    if (max_box - black_box) > 0 and height[i] > 0:
                        trapped += max_box - black_box
                        i = counter
                        # last_ref += 1
                    else:
                        i += 1

                else:

                    black_box = 0
                    x_counter = 0

                    if closest_counter > 0:
                        x = closest_number
                        if last_ref == 0:
                            last_ref += 1

                        for j in range(last_ref, closest_counter + 1):
                            x_counter += 1
                            if height[j] > x:
                                black_box += x
                            else:
                                black_box += height[j]
                    max_box = x_counter * closest_number

                    if len(height) <= 3:
                        trapped += max_box - black_box
                        i = counter
                        continue

                    if (max_box - black_box) > 0:
                        if counter + 1 == len(height) and height[counter] == 0:
                            i += x_counter - 1
                            last_ref = i
                            trapped += (max_box - black_box)
                            continue
                        trapped += (max_box - black_box)
                        counter += x_counter - 1
                        i = closest_counter
                        last_ref = i

                    else:
                        i += 1
        return trapped


sol = Solution()
result = sol.trap([9, 2, 2, 9, 5, 7, 6, 8, 3, 0, 0, 0, 0, 1, 8, 0, 0, 6, 0])
print(result)
