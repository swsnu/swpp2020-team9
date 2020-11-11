import React, { ReactElement, useState } from "react";
import Carousel from "react-bootstrap/Carousel";

export interface Location {
  centerXY: [number, number];
  image: string;
  title: string;
  text: string;
}

interface Props {
  locations: Location[];
  setCenterXY: (centerXY: [number, number]) => any;
}

function Gallery(props: Props): ReactElement {
  const { locations, setCenterXY } = props;
  const [index, setIndex] = useState(0);

  const handleSelect = (idx: number, e: any) => {
    setIndex(idx);
    setCenterXY(locations[idx].centerXY);
  };
  const locationItems = locations.map((location) => {
    const { centerXY, image, title, text } = location;

    return (
      <Carousel.Item>
        <img className="d-block w-100 gallery-img" src={image} alt={title} />
        <Carousel.Caption>
          <h3>{title}</h3>
          <p>{text}</p>
        </Carousel.Caption>
      </Carousel.Item>
    );
  });

  return (
    <div className="Gallery col-sm-6">
      <Carousel activeIndex={index} onSelect={handleSelect}>
        {locationItems}
      </Carousel>
    </div>
  );
}

export default Gallery;
// <Carousel.Item>
//   <img className="d-block w-100 gallery-img" src={Image1} alt="alt" />
//   <Carousel.Caption>
//     <h3>First slide label</h3>
//     <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
//   </Carousel.Caption>
// </Carousel.Item>
// <Carousel.Item>
//   <img className="d-block w-100 gallery-img" src={Image2} alt="alt" />
//   <Carousel.Caption>
//     <h3>Second slide label</h3>
//     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
//   </Carousel.Caption>
// </Carousel.Item>
// <Carousel.Item>
//   <img className="d-block w-100 gallery-img" src={Image3} alt="alt" />
//   <Carousel.Caption>
//     <h3>Third slide label</h3>
//     <p>
//       Praesent commodo cursus magna, vel scelerisque nisl consectetur.
//     </p>
//   </Carousel.Caption>
// </Carousel.Item>
// <Carousel.Item>
//   <img className="d-block w-100 gallery-img" src={Image4} alt="alt" />
//   <Carousel.Caption>
//     <h3>Third slide label</h3>
//     <p>
//       Praesent commodo cursus magna, vel scelerisque nisl consectetur.
//     </p>
//   </Carousel.Caption>
// </Carousel.Item>
// <Carousel.Item>
//   <img className="d-block w-100 gallery-img" src={Image5} alt="alt" />
//   <Carousel.Caption>
//     <h3>Third slide label</h3>
//     <p>
//       Praesent commodo cursus magna, vel scelerisque nisl consectetur.
//     </p>
//   </Carousel.Caption>
// </Carousel.Item>
