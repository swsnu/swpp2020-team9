import React, { ReactElement, useState, useEffect } from "react";

declare global {
  interface Window {
    kakao: any;
  }
}

interface Props {
  centerXY: [number, number];
}

function MapView(props: Props): ReactElement {
  const { centerXY } = props;
  const [mapLoaded, setLoaded] = useState(false);
  const [mapController, setMapController] = useState({
    panTo: (latlng: any) => null,
  });

  useEffect(() => {
    if (!mapLoaded) {
      const mapContainer = document.getElementById("map");
      const mapOptions = {
        center: new window.kakao.maps.LatLng(...centerXY),
        level: 4,
      };
      setMapController(new window.kakao.maps.Map(mapContainer, mapOptions));
      setLoaded(true);
    } else if (mapController) {
      const moveLatLng = new window.kakao.maps.LatLng(...centerXY);
      mapController?.panTo(moveLatLng);
    }
  }, [mapLoaded, centerXY, mapController]);

  return (
    <div className="MapView col-sm-6">
      <div id="map" style={{ width: "45vw", height: "90vh" }} />
    </div>
  );
}

export default MapView;
