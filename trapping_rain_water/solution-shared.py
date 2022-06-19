from _ast import List


class Solution:
    def trap(self, height: List) -> int:
        trapped = 0
        i = 0
        last_ref = 0
        while i < len(height) - 2:
            if height[i] == 0:
                i += 1
                last_ref = i
                continue
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

            foundWithNoLoop = True
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

                foundWithNoLoop = False
            else:
                if i3rd_bar >= height[i]:
                    last_ref = counter
                    max_box = (counter - (i + 2) + 3) * height[i]

                    if foundWithNoLoop:
                        if counter != (old_i + 2):
                            black_box += height[counter]
                        else:
                            if height[i + 2] > height[i]:
                                black_box -= (height[i + 2] - height[i])
                        max_box = 3 * height[i]

                    if (max_box - black_box) > 0 and height[i] > 0:
                        trapped += max_box - black_box
                        i = counter
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

                    if (max_box - black_box) > 0:
                        if counter + 1 == len(height) and height[counter] == 0:
                            i += x_counter - 1
                            last_ref += 2
                            trapped += (max_box - black_box)
                            continue
                        trapped += (max_box - black_box)

                        i += x_counter

                    else:
                        i += 1
        return trapped


sol = Solution()
result = sol.trap([0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2])
print(result)
