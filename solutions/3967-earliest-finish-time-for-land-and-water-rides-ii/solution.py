class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land = sorted(zip(landStartTime, landDuration), key=lambda x: x[0])
        water = sorted(zip(waterStartTime, waterDuration), key=lambda x: x[0])
        
        n_land, n_water = len(land), len(water)

        min_land_dur = []
        curr = float('inf')
        for _, d in land:
            curr = min(curr, d)
            min_land_dur.append(curr)
            
        min_water_dur = []
        curr = float('inf')
        for _, d in water:
            curr = min(curr, d)
            min_water_dur.append(curr)

        suf_land_tot = [0] * n_land
        curr = float('inf')
        for i in range(n_land - 1, -1, -1):
            curr = min(curr, land[i][0] + land[i][1])
            suf_land_tot[i] = curr
            
        suf_water_tot = [0] * n_water
        curr = float('inf')
        for i in range(n_water - 1, -1, -1):
            curr = min(curr, water[i][0] + water[i][1])
            suf_water_tot[i] = curr

        minVal = float('inf')

        for l_start, l_dur in land:
            finished = l_start + l_dur
            
            l, r = 0, n_water - 1
            while l < r:
                m = l + ((r - l + 1) // 2)
                if water[m][0] <= finished:
                    l = m
                else:
                    r = m - 1
            
            if water[r][0] <= finished:
    
                minVal = min(minVal, finished + min_water_dur[r])
                
    
                if r + 1 < n_water:
                    minVal = min(minVal, suf_water_tot[r + 1])
            else:
    
                minVal = min(minVal, suf_water_tot[0])
                
        for w_start, w_dur in water:
            finished = w_start + w_dur
            
            l, r = 0, n_land - 1
            while l < r:
                m = l + ((r - l + 1) // 2)
                if land[m][0] <= finished:
                    l = m
                else:
                    r = m - 1
            
            if land[r][0] <= finished:
                minVal = min(minVal, finished + min_land_dur[r])
                if r + 1 < n_land:
                    minVal = min(minVal, suf_land_tot[r + 1])
            else:
                minVal = min(minVal, suf_land_tot[0])
        
        return minVal
