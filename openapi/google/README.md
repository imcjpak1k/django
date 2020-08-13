# 구글은 차량경로탐색이 안됨
# 기본 샘플소스
```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      /* Set the size of the div element that contains the map */
      #map {
        height: 400px;  /* The height is 400 pixels */
        width: 100%;  /* The width is the width of the web page */
       }
    </style>
  </head>
  <body>
    <h3>My Google Maps Demo</h3>
    <!--The div element for the map -->
    <div id="map"></div>
    <script>
        // Initialize and add the map
        function initMap() {
        // The location of Uluru
        var uluru = {lat: -25.344, lng: 131.036};
        // The map, centered at Uluru
        var map = new google.maps.Map(
            document.getElementById('map'), {zoom: 4, center: uluru});
        // The marker, positioned at Uluru
        var marker = new google.maps.Marker({position: uluru, map: map});
        }
    </script>
    <script defer
    src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
    </script>
  </body>
</html>
```


# 지도생성 및 마커생성
```javascript
// 지도로드 후 콜백함수
function initMap() {
    // 지도생성
    var uluru = {lat: -25.344, lng: 131.036};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: uluru
    });

    // 마커생성
    var marker = new google.maps.Marker({
        map: map,
        position: uluru,
    });
}
```
# 마커생성
```javascript
// 마커생성
var marker = new google.maps.Marker({
    map: map,
    position: uluru,
});

// title, 마우스오버시 타이틀 표시됨
var marker = new google.maps.Marker({
    map: map,
    position: uluru,
    title: '까치산역',
});

// icon
const image = "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
const beachMarker = new google.maps.Marker({
    position: {
    lat: -33.89,
    lng: 151.274
    },
    map,
    icon: image
});


// https://developers.google.com/maps/documentation/javascript/examples/icon-complex
// Adds markers to the map.
// Marker sizes are expressed as a Size of X,Y where the origin of the image
// (0,0) is located in the top left of the image.
// Origins, anchor positions and coordinates of the marker increase in the X
// direction to the right and in the Y direction down.
const image = {
    url: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
    // This marker is 20 pixels wide by 32 pixels high.
    size: new google.maps.Size(20, 32),
    // The origin for this image is (0, 0).
    origin: new google.maps.Point(0, 0),
    // The anchor for this image is the base of the flagpole at (0, 32).
    anchor: new google.maps.Point(0, 32)
}; // Shapes define the clickable region of the icon. The type defines an HTML
// <area> element 'poly' which traces out a polygon as a series of X,Y points.
// The final coordinate closes the poly by connecting to the first coordinate.

const shape = {
    coords: [1, 1, 1, 20, 18, 20, 18, 1],
    type: "poly"
};

const kkachisan_complx = new google.maps.LatLng(37.531169, 126.847566);
// const image = "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
const kkachisanMarkerComplx = new google.maps.Marker({
    map,
    position: kkachisan_complx,
    icon: image,
    shape: shape,
    title: '복잡한 아이콘'
});





// https://developers.google.com/maps/documentation/javascript/examples/marker-animations
// 애니메이션 효과
// 이벤트
// draggable
marker = new google.maps.Marker({
    map,
    draggable: true,
    animation: google.maps.Animation.DROP,      // 마커가 생성될때 DROP효과
    position: {
        lat: 59.327,
        lng: 18.067
    }
});

// click event 1
marker.addListener("click", ()=>{
    if (marker.getAnimation() !== null) {
        marker.setAnimation(null);
    } 
    else {
        marker.setAnimation(google.maps.Animation.BOUNCE);
    }
});

// click event 2
marker.addListener("click", toggleBounce);
function toggleBounce() {
    if (marker.getAnimation() !== null) {
        marker.setAnimation(null);
    } 
    else {
        marker.setAnimation(google.maps.Animation.BOUNCE);  // 마커 BOUNCE효과
    }
}



// click event and InfoWindow

let infowindow = new google.maps.InfoWindow({
    content: 'contentString'
});

// 마커추가
function addMarker(location) {
    const marker = new google.maps.Marker({
        position: location,
        map: map, 
        title: location.toString(),
    });

    marker.addListener("click", ()=>{ 
        // infowindow
        infowindow.setContent([
                '<div style="padding:10px;min-width:200px;line-height:150%;">',
                '<h4">좌표정보 - nomal</h4>',
                `<h4 style='color:blue;'>${location.toString()}</h4>`,
                '</div>'
            ].join('\n'));
        infowindow.open(map, marker);
    });
        
    markers.push(marker);
} // Sets the map on all markers in the array.
```



# 마커삭제
```javascript
const marker = new google.maps.Marker({
    position: location,
    map: map, 
    title: location.toString(),
});

// hide 
marker.setMap( null );

// show
marker.setMap( map );


```
# InfoWindow
```javascript
let infowindow = new google.maps.InfoWindow({
    content: 'contentString',   // text, html,...
    maxWidth: 400,              // maxWidth값을 넘기면 스크롤생성
});

```

[위경도 정보변경](https://developers.google.com/maps/documentation/javascript/geocoding#GetStarted)     
[Code Samples](https://developers.google.com/maps/documentation/javascript/examples)  