import React, { ReactElement, useState } from "react";
import Row from "react-bootstrap/Row";
import Gallery, { Location } from "./Gallery";
import MapView from "./MapView";

import Image1 from "./overwatch_busan.jpg";
import Image2 from "./overwatch_egypt.jpg";
import Image3 from "./overwatch_hanamura.jpg";
import Image4 from "./overwatch_hollywood.jpg";
import Image5 from "./overwatch_ilios.png";

function View(): ReactElement {
  const [mapCenterXY, setCenterXY] = useState([33.450701, 126.570667]);
  const locations: Location[] = [
    {
      centerXY: [33.450701, 126.570667],
      image: Image1,
      title: "Busan",
      text: "Busan, harbor city of Korea",
    },
    {
      centerXY: [33.447550459048266, 126.56959047375511],
      image: Image2,
      title: "Egypt",
      text: "Homeland of the Sphynx",
    },
    {
      centerXY: [33.455727838988146, 126.56182722742336],
      image: Image3,
      title: "Hanamura",
      text: "Ryuuga wagateki wo kurau!",
    },
    {
      centerXY: [33.45568967208916, 126.55115742096783],
      image: Image4,
      title: "Hollywood",
      text: "Revenge is a dish best served cold",
    },
    {
      centerXY: [33.44464460571318, 126.54362151010882],
      image: Image5,
      title: "Illios",
      text: "I love greek yogurt!",
    },
  ];

  return (
    <div className="View">
      <Row>
        <Gallery locations={locations} setCenterXY={(xy) => setCenterXY(xy)} />
        <MapView centerXY={mapCenterXY as [number, number]} />
      </Row>
    </div>
  );
}

export default View;
