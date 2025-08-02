def factoryMaintenanceScheduling(production, output, cooldown):
    def can_produce(days):
        total_work = 0
        for o_i, c_i in zip(output, cooldown):
            days_of_work = days // (1 + c_i)
            extra_day_of_work = 1 if days % (1 + c_i) > 0 else 0
            total_work += (days_of_work + extra_day_of_work) * o_i

            if total_work >= production:
                return True
            
        return total_work >= production
    
    left, right = 1, 2*10**5
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if can_produce(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

production = 15
output = [5, 3]
cooldown = [2, 1]
print(factoryMaintenanceScheduling(production, output, cooldown))