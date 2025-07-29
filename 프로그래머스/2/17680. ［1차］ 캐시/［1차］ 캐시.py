def solution(cacheSize, cities):
    page = []
    hit = 0
    if cacheSize > 0:
        for city in cities:
            city = city.lower()
            if city in page:
                hit += 1
                page.remove(city)
                page.append(city)
                page = page[-cacheSize:]
            else: # page에 없다면
                hit += 5
                page.append(city)
                page = page[-cacheSize:]
        return hit
    else:  
        return len(cities)*5