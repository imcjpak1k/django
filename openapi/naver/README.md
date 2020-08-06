# naveropenapi
NAVER OPEN API

## 두 좌표간의 거리계산 (단위:미터)
[MapSystemProjection](https://navermaps.github.io/maps.js.ncp/docs/naver.maps.MapSystemProjection.html)
```javascript
let a = new naver.maps.LatLng(37.5142914, 126.9566194); 
let b = new naver.maps.LatLng(37.5204865, 126.9607178); 
let distince = map.getProjection().getDistance(a, b);   // 단위 meter 
// 778.8105806081434 meter

```
## 지도상의 대각선의 거리계산
```javascript
let distince = map.getProjection().getDistance(
    map.getBounds().getNE(), 
    map.getBounds().getSW()
);  
```
```
zoom 21 : 5m
zoom 20 : 10
zoom 19 : 20
zoom 18 : 30
zoom 17 : 50
zoom 16 : 100
zoom 15 : 300
zoom 14 : 500
zoom 13 : 1000
zoom 12 : 3000
zoom 11 : 5000
zoom 10 : 10000
zoom 9  : 20000
zoom 8  : 30000
zoom 7  : 50000
```

let lat_diff = marker_start.getPosition()._lat - marker_goal.getPosition()._lat;
let lng_diff = marker_start.getPosition()._lng - marker_goal.getPosition()._lng;
let latlng = new naver.maps.LatLng(marker_start.getPosition()._lat + lat_diff, marker_start.getPosition()._lng + lng_diff);
map.setCenter(latlng);




 lat_diff = marker_start.getPosition()._lat - marker_goal.getPosition()._lat / 2;
 lng_diff = marker_start.getPosition()._lng - marker_goal.getPosition()._lng / 2;
 latlng = new naver.maps.LatLng(marker_start.getPosition()._lat + lat_diff, marker_start.getPosition()._lng + lng_diff);
map.setCenter(latlng);

## 캘리더 정보 동기화(가져오기는 아래경로 참조???)
https://developers.naver.com/forum/posts/14294
https://calyfactory.github.io/caldav-sync-1/
https://calyfactory.github.io/caldav-sync-2/
https://github.com/CalyFactory/python-caldavclient